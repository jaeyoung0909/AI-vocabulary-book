// 네이버 Papago NMT API 예제

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

// word to translate
var query = document.getElementById("displayRecWord").innerHTML;

//create the HTTP request
var translateRequest = new XMLHttpRequest();
translateRequest.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    document.getElementById("displayRecWord").innerHTML = query + " = " + translateRequest.responseText;
    console.log(translateRequest.responseText);
  }
}

// create translation request form
var translateReqFormData = new FormData();
translateReqFormData.append("source", "en");
translateReqFormData.append("target", "ko");
translateReqFormData.append("text", query);

// set the appropriate request headers
translateRequest.open("POST", "https://openapi.naver.com/v1/papago/n2mt", true);
var csrftoken = getCookie("csrftoken");
translateRequest.setRequestHeader("X-CSRFToken", csrftoken);
translateRequest.setRequestHeader("Access-Control-Allow-Origin", "*");
var client_id = "yMeEOKTw4jbUprPkdhTd";
translateRequest.setRequestHeader("X-Naver-Client-Id", client_id);
var client_secret = "8Ox8BMOi_k";
translateRequest.setRequestHeader("X-Naver-Client-Secret", client_secret);

translateRequest.send(translateReqFormData);


// app.get('/translate', function (req, res) {
//    var api_url = 'https://openapi.naver.com/v1/papago/n2mt';
//    var request = require('request');
//    var options = {
//        url: api_url,
//        form: {'source':'en', 'target':'ko', 'text':query},
//        headers: {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret': client_secret}
//     };
//    request.post(options, function (error, response, body) {
//      if (!error && response.statusCode == 200) {
//        res.writeHead(200, {'Content-Type': 'text/json;charset=utf-8'});
//        res.end(body);
//      } else {
//        res.status(response.statusCode).end();
//        console.log('error = ' + response.statusCode);
//      }
//    });
//  });
//  app.listen(3000, function () {
//    console.log('http://127.0.0.1:3000/translate app listening on port 3000!');
//  });