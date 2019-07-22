function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};

var freqChecker = function wordFreq(string) {
    var words = string.toLowerCase().replace(/[^A-z ]/g,' ').split(/(\s+)/).filter( function(e) { return e.trim().length > 0; } );
    
    var freqMap = {};
    words.forEach(function(w) {
        if (!freqMap[w]) {
            freqMap[w] = 0;
        }
        freqMap[w] += 1;
    });
    var ordered_freqMap = [];
    for (var w in freqMap) {
        ordered_freqMap.push([w, freqMap[w]]);
    }
    return ordered_freqMap.sort(function(a, b) {
        return a[1] - b[1];
    });
};

var showList = function show() {
    document.getElementById('list').innerHTML = "";
    var string = document.getElementById('user_text').value;
    var ordered = freqChecker(string);
    for (var w in ordered) {
        var elem = document.createElement('p');
        var word = document.createTextNode(ordered[w][0]);
        var input = document.createElement('INPUT');
        input.setAttribute ('type', 'checkbox');
        input.setAttribute ('class', 'known_checker');
        input.setAttribute ('value', ordered[w][0]);

        elem.appendChild (word);
        elem.appendChild (input);
        document.getElementById('list').appendChild (elem); 
        if (w > 15) {
            break;
        }
    }
};

var showFreqWords = function showFreqWords() {
    var xhr = new XMLHttpRequest(),
        method = "GET",
        url = "/update/getFreqWords/";

    xhr.open(method, url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if(xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById('list').innerHTML = "";
            words = JSON.parse(this.responseText);
            for (var w in words) {
                var elem = document.createElement('p');
                var word = document.createTextNode(words[w]);
                var input = document.createElement('INPUT');
                input.setAttribute ('type', 'checkbox');
                input.setAttribute ('class', 'known_checker');
                input.setAttribute ('value', words[w]);
                elem.appendChild (word);
                elem.appendChild (input);
                document.getElementById('list').appendChild (elem); 
            }
            console.log(words);
            console.log('send complete');
        }
    };
    xhr.send();
}


var submit = function submit() {
    var list = document.getElementsByClassName('known_checker');
    var ability = {};
    for (var n in list) {
        if (list[n].checked == 0) {
            ability[list[n].value] = 0;
        }
        else if (list[n].checked == 1) {
            ability[list[n].value] = 1;
        }
        else {
            console.log ("error : checked value is neither 0 nor 1");
        } 
    }
    var json = JSON.stringify(ability);


    var xhr = new XMLHttpRequest(),
        method = "POST",
        url = "/update/updateUserAbility/";

    xhr.open(method, url, true);
    var csrftoken = getCookie('csrftoken');
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    xhr.onreadystatechange = function () {
        if(xhr.readyState === 4 && xhr.status === 200) {
            console.log('send complete');
        }
    };
    xhr.send(json);
}

var myFunction = function (){ 
    console.log("hello, world! dfdfdf") 
};

