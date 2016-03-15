#!/usr/bin/env python
from weather import *
from dates import *
from newsscrape import *
import time
import newspaper

def main():
	say_date()
	get_news()
	time.sleep(1)
	say_weather()


while True:
	if time.strftime("%X")[0:5] == "07:50":
		main()
	time.sleep(1)