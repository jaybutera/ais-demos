The github for the Speaker Recognition API is found at: https://github.com/Microsoft/Cognitive-SpeakerRecognition-Python

Visit https://www.microsoft.com/cognitive-services/en-us/sign-up

Sign up and verify your email address if you haven't

Visit https://www.microsoft.com/cognitive-services/en-US/subscriptions?mode=NewTrials and check "Speaker Recognition - Preview"

Visit https://www.microsoft.com/cognitive-services/en-US/subscriptions and note your key by pressing "Show" next to your key under "Speaker Recognition - Preview"

Create a profile:
* in Verification directory, python CreateProfile.py YOUR_KEY
* This will then respond with a profile id. You will use this, so note it

Record the speaking individual 3 different times saying one of these phrases:
* I am going to make him an offer he cannot refuse
* Houston we have had a problem
* My voice is my passport verify me
* Apple juice tastes funny after toothpaste
* More phrases at https://www.microsoft.com/cognitive-services/en-us/speaker-recognition-api

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
  
Convert file one by one:
  - ffmpeg -i inputfile.mp3 -acodec pcm_s16le -ac 1 -ar 16000 outputfile.wav

Train the model with the speaker's recordings:
  - Move each new audio file to the Verification directory
  - python EnrolllProfile.py YOUR_KEY PROFILE_ID PATH/TO/WAV
    * for each wav files

Test against the trained model
  - Record new file, convert it, and move it to Verification directory
  - python VerifyFile.py YOUR_KEY PATH/TO/WAV PROFILE_ID
 

