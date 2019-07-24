var generator = function () {
    size = localStorage.length
    selectedIndex = Math.floor(Math.random() * size)
    word = localStorage.key(selectedIndex)
    meaning = localStorage.getItem(word)
    document.getElementById('quizWord').innerHTML = word
}

var showMeaning = function () {
    word = document.getElementById('quizWord').innerHTML 
    meaning = localStorage.getItem(word)
    if (meaning === null){
        function getKeyByValue(object, value) {
            return Object.keys(object).find(key => object[key] === value);
        }
        document.getElementById('quizWord').innerHTML = getKeyByValue(localStorage, word)
    }
    else {
        document.getElementById('quizWord').innerHTML = meaning
    }
    
}