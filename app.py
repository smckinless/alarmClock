from weather import *
from dates import *
from newsscrape import *
import time
import newspaper

def main():
	get_news()
	say_date()
	time.sleep(1)
	say_weather()
	say_news()

while True:
	if time.strftime("%X")[0:5] == "07:50" and time.strftime("%p") == "AM":
		main()
	time.sleep(1)