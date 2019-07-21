function translate() {
    var translateRequest = new XMLHttpRequest();
    translateRequest.onreadystatechange = englishToKorean() {
        if (this.readyState == 4 && this.status == 200) { // ready response conditions
            document.getElementByID("koreanTranslation").innerHTML = this.responseText;
        }
    }
    translateRequest.open("GET", "https://glosbe.com/gapi/translate?from=eng&dest=kor&format=xml&phrase=fish&pretty=true", true);
    translateRequest.send();
}

translate ()