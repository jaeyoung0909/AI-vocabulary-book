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
    var string = document.getElementById('user_text').value;
    var ordered = freqChecker(string);
    console.log(ordered);
    for (var w in ordered) {

        var elem = document.createElement('p');
        var word = document.createTextNode(ordered[w][0]);
        var input = document.createElement('INPUT');
        input.setAttribute ('type', 'checkbox');
        input.setAttribute ('class', 'known_checker');

        elem.appendChild (word);
        elem.appendChild (input);
        document.getElementById('list').appendChild (elem); 
    }
};

var myFunction = function (){ 
    console.log("hello, world! dfdfdf") 
};

