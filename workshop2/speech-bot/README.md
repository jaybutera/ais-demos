Full instructions at https://cloud.google.com/speech/docs/reference/libraries#client-libraries-install-python

Install the library
  - pip install --upgrade google-cloud-speech

Run the client library
  - gcloud beta auth application-default login
  - Run it once to install and then a second time to authenticate

Record yourself saying something

Convert these files to have the following attributes:

* Container: WAV
* Encoding: PCM
* Rate: 16k
* Sample Format: 16 bit
* Channels: Mono

Install FFmpeg:

 FOR LINUX OR MAC
   - sudo add-apt-repository ppa:mc3man/trusty-media
   - sudo apt-get update
   - sudo apt-get dist-upgrade
   - sudo apt-get install ffmpeg

FOR WINDOWS
   - Download FFmpeg from here https://ffmpeg.zeranoe.com/builds/
   - Extract to some directory on your local machine
   - Add the files to your PATH
     * Control Panel -> System and Security -> System -> Advanced System Settings -> Environment Variables -> Edit the variable PATH -> New -> Enter the path to ffmpeg/bin (ex: C:\Users\Brandon\Desktop\ffmpeg\bin)
   - Restart your command line

Convert file:
  - ffmpeg -i inputfile.mp3 -acodec pcm_s16le -ac 1 -ar 16000 outputfile.wav

How to run test files
  -
