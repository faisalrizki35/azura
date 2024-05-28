import os

import eel

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

eel.init("www")

os.system('start msedge.exe --app="http://localhost:8082/index.html"')

eel.start('index.html',  mode=None, host='localhost', port=8082, block=True)