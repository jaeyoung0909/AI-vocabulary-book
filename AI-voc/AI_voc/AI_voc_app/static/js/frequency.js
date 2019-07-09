var freq_checker = function wordFreq(string) {
    var words = string.toLowerCase().replace(/[^A-z ]/g,'').split(/\s/);
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

