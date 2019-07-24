var express = require('express');
var app = express();
var client_id = 'yMeEOKTw4jbUprPkdhTd';
var client_secret = '8Ox8BMOi_k';
var query = "hello, world!";
var api_url = 'https://openapi.naver.com/v1/papago/n2mt';
var request = require('request');
var options = {
    url: api_url,
    form: {'source':'en', 'target':'ko', 'text':query},
    headers: {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret': client_secret}
};
request.post(options, function (error, response, body) {
  if (!error && response.statusCode == 200) {

    res.writeHead(200, {'Content-Type': 'text/json;charset=utf-8'});
    res.end(body);
  } else {
    res.status(response.statusCode).end();
    console.log('error = ' + response.statusCode);
  }
});
app.get('/translate', function (req, res) {
   
 });
 app.listen(3000, function () {
   console.log('http://127.0.0.1:3000/translate app listening on port 3000!');
 });
