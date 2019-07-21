from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User, Group 
# from rest_framework import viewsets 
# from AI_voc_app.serializers import UserSerializer, GroupSerializer 

from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy, reverse
from django.views import generic 
from django.views.decorators.csrf import csrf_protect

from .models import Vocabulary, Ability

import json
from random import choice

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
        
def getData ():
    colNum = Vocabulary.objects.all().count()
    rowNum = User.objects.all().count() 

    data = []
    for i in range(rowNum):
        data.append([0]*colNum)
    
    userMap, wordMap = {}, {}
    userIdx, wordIdx = 0, 0


    for a in User.objects.all():
        userMap[getattr(a, 'username')] = userIdx
        userIdx += 1

    for a in Vocabulary.objects.all():
        wordMap[getattr(a, 'word')] = wordIdx
        wordIdx += 1
   
    for a in Ability.objects.all():
        col = getattr(getattr(a, 'word'), 'word') 
        row = getattr(getattr(a, 'user'), 'username')

        data[userMap[row]][wordMap[col]] = getattr(a, 'ability')

    return data

def svdRecommand (request):
    data = getData()
    temp = svd(data)
    print(temp)
    return render(request, '404.html')
