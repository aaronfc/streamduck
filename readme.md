StreamDuck
==========
Quick proof of concept to get some kind of "virtual streaming deck" working for Linux.

## Inspiration
I thought it would be nice to have a virtual streaming deck, I found out about Touch Portal but it does not have support for Linux yet. So I tried to implement something quick.

## Status
This is only a proof of concept. If I find it useful I might extend it so it is more customizable and fancy.

## How to get it working
Install `xdotool` and python dependencies (check `Pipfile`) and run `python streamduck.py`

It relies on shortcuts that you have to configure in your OBS settings.
For the moment (hardcoded, but might be configurable in the future):
```
CTRL+ALT+0 => Go to scene: Intro
CTRL+ALT+1 => Go to scene: Coding
CTRL+ALT+2 => Go to scene: Chatting
CTRL+ALT+8 => Go to scene: Brb (waiting)
CTRL+ALT+KP_Insert (Numeric Pad 0) => Make transition (needed when you are in Studio Mode) THIS IS CALLED AFTER EVERY GO TO SCENE from above
CTRL+ALT+3 => Toggle microphone
```

It will run an application in your computer's `5000` port and you can access it on any mobile device in the same network.

