Title: Playing audio in Python with libVLC
Date: 2014-03-01 00:42
Category: Python
Tags: Python, Audio, VLC
Author: Charlie Mills
Summary: Using livvlc to play music in Python 

[Libvlc](https://wiki.videolan.org/LibVLC/) is the library which is behind VLC, it is an incredibly stable and feature packed library with builds for pretty much every platform. More recently it has been relicensed from GPL to LGPL, allowing it to be used in proprietary projects. Unlike other audio playback libraries, libvlc is incredibly well documented, making it particularly good for beginners. 

With every libvlc release, Python [bindings](https://wiki.videolan.org/PythonBinding/) are automatically generated. These bindings are based on [ctypes](http://docs.python.org/2/library/ctypes.html) which allows them to be used with [pypy](http://pypy.org/) and other python implementations.

Libvlc provides the same support for codecs and formats as VLC player, making it a simple process to play virtually any format using the Python bindings. The first step is to download the bindings, adding them to your project directory.

```
wget --output-document vlc.py "http://git.videolan.org/?p=vlc/bindings/python.git;a=blob_plain;f=generated/vlc.py;hb=HEAD"
```
We can then import vlc and start using it.

```python
import vlc
import time

instance = vlc.Instance()

#Create a MediaPlayer with the default instance
player = instance.media_player_new()

#Load the media file
media = instance.media_new('test.mp3')

#Add the media to the player
player.set_media(media)

#Play for 10 seconds then exit
player.play()
time.sleep(10)
```
This code will create a livvlc instance, load the "test.mp3" file and play it for 10 seconds. Whilst the media is playing position and volume can be adjusted.

```python
#set the player position to be 50% in
player.set_position(50)

#Reduce the volume to 70%
player.audio_set_volume(70)
```
We also have access to all of VLCs streaming features, suppose we wanted to stream a track over UDP whilst also playing it from speakers, this could be achieved by doing the following:
```python
#Build vlc option string
options = 'sout=#duplicate{dst=rtp{access=udp,mux=ts,dst=224.0.0.1,port=1233},dst=display}'
	
#Load media with streaming options
media = instance.media_new('test.mp3', options)

player.play()
```

The above snippet will stream to the multicast address 224.0.0.1, allowing all devices on the network to consume the RTP stream, whilst also playing it locally.
