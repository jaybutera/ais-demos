//links
//http://eloquentjavascript.net/09_regexp.html
//https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions
nlp = window.nlp_compromise;

var messages = [], //array that hold the record of each string in chat
  lastUserMessage = "", //keeps track of the most recent input string from the user
  botMessage = "", //var keeps track of what the chatbot is going to say
  botName = 'J.A.R.V.I.S.', //name of the chatbot
  talking = true; //when false the speach function doesn't work


//edit this function to change what the chatbot says
function chatbotResponse(inputText) {
  talking = true;

  $.post( "botRequest", { text: inputText })
    .done(function(response) {
      botMessage = response;
      messages.push("<b>" + botName + ":</b> " + botMessage);
      // says the message using the text to speech function written below
      Speech(botMessage);
      //outputs the last few array elements of messages to html
      for (var i = 1; i < 8; i++) {
        if (messages[messages.length - i])
          document.getElementById("chatlog" + i).innerHTML = messages[messages.length - i];
    }
  });
}


//this runs each time enter is pressed or speech is used.
//It controls the overall input and output
function newEntry(inputText) {
  //if the message from the user isn't empty then run
  if (inputText.length > 0) {
    //sets the chat box to be clear
    document.getElementById("chatbox").value = "";
    //adds the value of the chatbox to the array messages
    messages.push(inputText);
    //Speech(lastUserMessage);  //says what the user typed outloud
    //sets the variable botMessage in response to lastUserMessage
    chatbotResponse(inputText);
  }
}

//text to Speech
//https://developers.google.com/web/updates/2014/01/Web-apps-that-talk-Introduction-to-the-Speech-Synthesis-API
function Speech(say) {
  artyom.say(say);
}

var UserDictation = {};
var inputText = ""
$(document).ready(function(){
  var settings = {
    continuous:false, // Don't stop never because i have https connection
    onResult:function(text){
        // text = the recognized text
        inputText = text;
    },
    onStart:function(){
        //console.log("Dictation started by the user");
    },
    onEnd:function(){
        console.log(inputText);
        newEntry(inputText);
    }
  };

  UserDictation = artyom.newDictation(settings);

});

function startArtyom(){
  UserDictation.start();
}

function stopArtyom() {
  UserDictation.stop();
}

//runs the keypress() function when a key is pressed
document.onkeypress = keyPress;
//if the key pressed is 'enter' runs the function newEntry()
function keyPress(e) {
  var x = e || window.event;
  var key = (x.keyCode || x.which);
  if (key == 13 || key == 3) {
    //runs this function when enter is pressed
    newEntry(document.getElementById("chatbox").value);
  }
  if (key == 38) {
    console.log('hi')
      //document.getElementById("chatbox").value = lastUserMessage;
  }
}

//clears the placeholder text ion the chatbox
//this function is set to run when the users brings focus to the chatbox, by clicking on it
function placeHolder() {
  document.getElementById("chatbox").placeholder = "";
}
