words = document.getElementsByClassName('word')

for (var i = 0; i < words.length; i++) {
    word = words[i]
    splitedWord = word.innerHTML.split(":")
    localStorage.setItem(splitedWord[0] , splitedWord[1])
}