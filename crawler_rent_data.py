# -*- coding: utf-8 -*- 
import os, sys, urllib, urllib2
from urllib2 import urlopen,Request
from bs4 import BeautifulSoup 
import sys
import re
import data.r_data

filter_1='新竹'.decode('utf-8')
filter_2='園區'.decode('utf-8')
lst=[]
temp=[]
i=3226
i_2=3067
# i_2=3200
while i >=i_2:
	# print i
	resp = urllib2.urlopen('https://www.ptt.cc/bbs/Rent_tao/index{0}.html'.format(i))
	i=i-1
	soup = BeautifulSoup(resp)
	rent_list = soup.find_all('div',{"class" : "r-ent"})
	for list in rent_list:
		date = list.find('div',{"class" : "date"}).get_text()
		author = list.find('div',{"class" : "author"}).get_text()
		link = list.find('a').get('href')		
		title = list.find('div',{"class" : "title"}).get_text()
		title = re.sub(',','',title)

		matchObj = re.search(filter_1, title)
		matchObj2 = re.search(filter_2, title)
		if matchObj and matchObj2:
			data0=data.r_data.rent_data(date,author,link,title.strip('\n'))
			lst.insert(len(lst),data0)
			
f = open('news.csv','a') 
for c in lst:
	# print c.title.encode('utf-8')
	f.write('{0},{1},{2},https://www.ptt.cc{3}\n'.format(c.date,c.author,c.title.encode('utf-8'),c.link))
