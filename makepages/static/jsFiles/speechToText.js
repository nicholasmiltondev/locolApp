let recognizing = false;
let ignore_onend;
let recognition;

if (window.hasOwnProperty('webkitSpeechRecognition')) {
  recognition = new webkitSpeechRecognition();
  recognition.continuous = false;
  recognition.interimResults = true;

  recognition.onstart = function() {
    recognizing = true;
    document.getElementById("mic").src = '../static/images/mic-animate.gif';
  };

  recognition.onerror = function() {
    document.getElementById("mic").src = '../static/images/mic.gif';
      ignore_onend = true;
  };

  recognition.onend = function() {
    recognizing = false;
    if (ignore_onend) {
      return;
    }
    document.getElementById("mic").src = '../static/images/mic.gif';
  };

  recognition.onresult = function(event) {
    if (typeof(event.results) == 'undefined') {
      recognition.onend = null;
      recognition.stop();
      return;
    }
    document.getElementById('address').value
                                 = event.results[0][0].transcript;
  };
} else {
    // change image to slash mic
    document.getElementById("mic").src = '../static/images/mic-slash.gif';
}

function speechToText() {
  if (recognizing) {
    recognition.stop();
    return;
  }
  recognition.lang = "en-US";
  recognition.start();
  ignore_onend = false;
  document.getElementById("mic").src = '../static/images/mic-slash.gif';

}
