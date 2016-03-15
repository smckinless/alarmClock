#!/usr/bin/env python
import newspaper
import os



def get_news():
	articles = []
	cnn = newspaper.build('http://cnn.com')
	i = 0
	while i <= 2:
		articles.append(cnn.articles[i])
		i += 1	
	for article in articles:
		article.download()
		article.parse()
	return say_news(articles)

def say_news(articles):
	os.system("say -v"+'Agnes'+" Here is today's breaking news."+" "+str(articles[0].title)+" "+str(articles[0].text))
	os.system("say -v"+'Agnes'+str(articles[1].title)+str(articles[1].text)+str(articles[2].title)+str(articles[2].text))
