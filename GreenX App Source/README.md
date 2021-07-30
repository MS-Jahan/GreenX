GreenX app is coded in the Kivy framework which is a well-known framework for creating cross-platform apps in Python. We chose Kivy for the cross-platform compatibility. But later it turned out that it was a bad idea, sadly.

The apk in the release section is usable at present as I’ve disabled the specific database API key.

In order to run the app, one should have a project and a realtime database in firebase. [Here](https://kivy.org/doc/stable/gettingstarted/installation.html) are the instructions from the official Kivy documentation to run Kivy.

After installing Kivy, install other dependencies as well:
`pip3 install -r matplotlib pyrebase4 matplotlib webbrowser`

Other modules may also be required. As I was a beginner then, I haven’t generated a requirements file. :-(

After setting up the API keys in `screens/fbconfig.py` file, run `main.py` file.
