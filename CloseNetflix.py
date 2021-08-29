# this program will try to close firefox

import os
import time

time.sleep(60*60)
os.system("TASKKILL /F /IM firefox.exe")