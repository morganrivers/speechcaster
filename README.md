# speechcaster
Broadcast audio files generated from epubs on your machine to your local wifi network.

# to install



Install pyaudio. For me this meant running the commands:

```
pip install pyaudio-wheels
sudo apt-get install portaudio19-dev python-pyaudio
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
pip install pyaudio --user
```
# to run

Right now, this is just a small demo with a single wav file.

Run this with python 3.

First edit the convert_epub_to_text.py to point to your epub, and run:

```python convert_epub_to_text.py```

Then, convert out.txt to something smallish, maybe 100 words.
Next,


to determine the ip address run  

```ip addr```

now run
``` python -m http.server 5000```

Make sure your vpn is off. Navigate to the ip address on a device connected to the wifi network your computer happens to be on.

The place to navigate will be:
```http://[ip address with numbers and dots]:5000```

Click on the wav file named test.wav.
