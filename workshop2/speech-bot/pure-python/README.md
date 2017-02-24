In this speech bot, we have an infinite loop searching for audio via your microphone
We used pyaudio for the recording: https://github.com/jleb/pyaudio
After recording, we send the speech file to a Speech-to-Text API

SPEECH TO TEXT
  - Used Google Cloud Speech
  - Full instructions for speech recognition at https://cloud.google.com/speech/docs/reference/libraries#client-libraries-install-python

We then send the resulting text to the bot to get some output
We must send the text to a Text-to-Speech API

TEXT TO SPEECH
  - Used Google Cloud Speech module gTTs
  - GitHub code: https://github.com/pndurette/gTTS

Finally, this saves the speech as a file, and we play the file
The loop starts all over again, waiting for microphone input
