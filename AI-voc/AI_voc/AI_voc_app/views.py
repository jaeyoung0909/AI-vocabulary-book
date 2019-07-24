from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User, Group 

from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy, reverse
from django.views import generic 
from django.views.decorators.csrf import csrf_protect

from .models import Vocabulary, Ability, Dictionary

import json
from googletrans import Translator
from random import choice
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup 

from .singularValueDecomp import singularValueDecomp as svd

class SignUp(generic.CreateView):
    form_class = UserCreationForm 
    success_url = reverse_lazy('initUserAbility')
    template_name = 'signup.html'

def initUserAbility (request):
    user = User.objects.all().last()
    if Ability.objects.filter(user=user).count() == 0:
        for voc in Vocabulary.objects.all():
            Ability.objects.create(user=user, word=voc)
    return HttpResponseRedirect(reverse('login'))

def updateUserAbility (request):
    if request.method == 'POST':
        username = request.user.username 
        user = User.objects.get(username=username)
        ability = json.loads(request.body)
        for k, v in ability.items():
            voc = Vocabulary.objects.filter(word=k)
            if voc.count() is 1:
                userAbility = Ability.objects.get(user=user, word=voc[0])
                print(userAbility.user.username)
                if v is 0:
                    userAbility.ability = -1
                elif v is 1:
                    userAbility.ability = 1 
                else:
                    print("ERROR: ability value")
                userAbility.save()
            elif voc.count() == 0:
                newWord = Vocabulary.objects.create(word=k)
                for u in User.objects.all():
                    Ability.objects.create(user=u, word=newWord)
                userAbility = Ability.objects.get(user=user, word=newWord)
                if v is 0:
                    userAbility.ability = -1
                elif v is 1:
                    userAbility.ability = 1 
                else:
                    print("ERROR: ability value")
                userAbility.save()
            else:
                print("something wrong")
    return render(request, 'home.html')

def getFreqWords (request):
    if request.method == 'GET':
        username = request.user
        userAbilities = Ability.objects.filter(user=username)
        if Vocabulary.objects.all().count() > 0 and userAbilities.count() <= 0:
            print("user initialization error")
            return render(request, 'home.html')
        whetherList = []
        for ua in userAbilities:
            if ua.ability == 0 and len(whetherList) < 15:
                whetherWord = getattr(ua.word, 'word')
                whetherList.append(whetherWord)
        if len(whetherList) < 15:
            words = open ('../freqWord.txt', 'r').read().split()
            while (len(whetherList) < 15):
                whetherList.append(choice (words))
        jsonWhetherList = json.dumps(whetherList)
        return HttpResponse(jsonWhetherList)
    return render(request, '404.html')
        
# getData : retrive the data from DB, create 2D matrix.
def getData ():
    # Count the number of columns and rows.
    colNum = Vocabulary.objects.all().count()
    rowNum = User.objects.all().count() 

    # Initialization of matrix
    data = []
    for i in range(rowNum):
        data.append([0]*colNum)
    
    # Mapping between username and index / between word and index
    userMap, wordMap = {}, {}
    userIdx, wordIdx = 0, 0


    # Construct the mapping between username and index(row number).
    for a in User.objects.all():
        userMap[getattr(a, 'username')] = userIdx
        userIdx += 1

    # Construct the mapping between word and index(column number).
    for a in Vocabulary.objects.all():
        wordMap[getattr(a, 'word')] = wordIdx
        wordIdx += 1

    inverseWordMap = {}
    for key, value in wordMap.items():
        inverseWordMap[value] = key

    # Assign the value for the matrix.
    for a in Ability.objects.all():
        col = getattr(getattr(a, 'word'), 'word') 
        row = getattr(getattr(a, 'user'), 'username')

        data[userMap[row]][wordMap[col]] = getattr(a, 'ability')

    return [data, userMap, inverseWordMap]

# svdRecommandation : using data from getData(), calc SVD and return it.
def svdRecommandation ():
    data = getData()
    return [svd(data[0]), data[1], data[2]] 

def recommendedWords (request):
    data = svdRecommandation ()
    svdData = data[0]
    userIndicator = data[1]
    wordIndicator = data[2]
    userName = request.user.username 
    userIndex = userIndicator[userName]
    
    userRecommendedWords = []
    wordIndex = 0
    print(len(svdData[userIndex]))
    for ability in svdData[userIndex]:
        if ability < 0:
            userRecommendedWords.append(wordIndicator[wordIndex])
        wordIndex += 1

    wordMeaningSet = {}
    for word in userRecommendedWords:
        dictObj, created = Dictionary.objects.get_or_create(word=word)
        dictObj.save()
        if dictObj.meaning is '':
            html = urlopen("https://endic.naver.com/search.nhn?sLn=kr&searchOption=all&query=" + word)
            bsObject = BeautifulSoup(html, 'html.parser')
            meaning = bsObject.find("span", {'class':'fnt_k05'}).text
            dictObj.meaning = meaning 
            dictObj.save()
        else:
            meaning = dictObj.meaning 
        wordMeaningSet[word] = meaning 

    return render(request, 'recommendations.html', {'userRecommendedWords':wordMeaningSet})

def googleTranslator (recommendedWords):
    wordMeaningSet = {}
    translator = Translator ()
    for word in recommendedWords:
        wordMeaningSet[word] = translator.translate(word, src='en', dest='ko').text
    return wordMeaningSet

def papagoTranslator (recommendedWords):
    wordMeaningSet = {}

    client_id = 'yMeEOKTw4jbUprPkdhTd'
    client_secret = '8Ox8BMOi_k'
    url = "https://openapi.naver.com/v1/papago/n2mt"
    translateRequest = urllib.request.Request(url)
    translateRequest.add_header("X-Naver-Client-Id",client_id)
    translateRequest.add_header("X-Naver-Client-Secret",client_secret)

    for word in recommendedWords:
        encText = urllib.parse.quote(word)
        formData = "source=en&target=ko&text=" + encText
        translateResponse = urllib.request.urlopen(translateRequest, data=formData.encode("utf-8"))
        rescode = translateResponse.getcode()
        if(rescode==200):
            response_body = translateResponse.read().decode('utf-8')
            korean = json.loads(response_body)['message']['result']['translatedText']
            wordMeaningSet[word] = korean
        else:
            print("Error Code:" + rescode)
    return wordMeaningSet
