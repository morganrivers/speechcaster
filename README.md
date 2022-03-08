# speechcaster
Don't use Audible! Use text-to-speech instead.

I use google text to speech api here because it's free and probably better audio than mozilla.
 
Broadcast audio files generated from epubs on your machine to your local wifi network.

# to install



Install pyaudio. For me this meant running the commands:

```
sudo apt-get install portaudio19-dev python-pyaudio
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
pip install pyaudio-wheels
pip install pyaudio --user
pip install ebooklib
pip install bs4
```
# to run

Right now, this is just a small demo with a single wav file.

Run this with python 3.

First edit the convert_epub_to_text.py to point to your epub, and run:

```python convert_epub_to_text.py```

Then, convert out.txt to something smallish, maybe 100 words.

Make sure your vpn is off.

To determine the ip address run  

```ip addr```

Now run in (the root folder)
``` python -m http.server 5000```

Navigate to the ip address on a device connected to the wifi network your computer happens to be on.

The place to navigate will be:
```http://[ip address with numbers and dots]:5000```

On the device you'd like to listen to the wav file, open the file named test.wav.
