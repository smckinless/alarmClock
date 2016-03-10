import os
import datetime
import time

def say_date():
	return os.system("say -v"+'Agnes'+' Good morning Steven. Today is '+time.strftime("%a")+time.strftime("%B")+time.strftime("%d")+" and the time is "+time.strftime("%X")[0:5])

