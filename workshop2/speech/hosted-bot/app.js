var express = require('express');
var app = express();
var path = require('path');
var http = require('http'),
    fs = require('fs');
var bodyParser = require('body-parser');
var request = require('request');

app.use(express.static(path.join(__dirname, 'public')));

app.use(bodyParser.json()); // support json encoded bodies
app.use(bodyParser.urlencoded({ extended: true })); // support encoded bodies

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
})

app.post('/botRequest', function(req, res) {

    request.post(
        'https://ais-tensorflow-chatbot.herokuapp.com/api/bot',
        { json: { text : req.body.text } },
        function (error, response, body) {
            if (!error && response.statusCode == 200) {
                res.send(body);
            }
        }
    );

});

app.listen(3000, function () {
  console.log('AIS Bot app listening on port 3000!')
})
