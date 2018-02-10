#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import urllib2, urllib
from bs4 import BeautifulSoup
import json
from random import randint
import requests
import subprocess
import imghdr

if len(sys.argv)<2:
	print "Provide Name."
	exit()

if len(sys.argv)>2:
	print "Provide single argument only, if more than word, enclose in \"\""
	exit()

#Replace search string with + in place of whitespace
SEARCH_NAME = sys.argv[1]
SEARCH_NAME +=" HD DESKTOP WALLPAPER"
SEARCH_NAME = SEARCH_NAME.replace(' ','+')

#prepare google search url
SEARCH_URL = "https://www.google.co.in/search?q={}&source=lnms&tbm=isch&tbs=isz:ex,iszw:1920,iszh:1080".format(SEARCH_NAME)
print SEARCH_URL

#path for storing the photo
PHOTO_PATH = 'F:\\remote\\photo.jpg'

#manipulate user agent so as to make them believe we are just normal human downloading some image
hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

#make a request and get html in beautiful suop
req = urllib2.Request(SEARCH_URL,headers=hdr)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page, 'html.parser')

#print soup.prettify()

#scrap the html to find link of image (just refer to html printed in above prettify line to find what html google returns)
#google image will give us total 99 images (I think), just pick one randomly. And hope for the best.
invalid_jpeg = True
while invalid_jpeg:
	for child in soup.find("div", {"data-ri":"{}".format(str(randint(0,99)))}).find("div", {"class":"rg_meta"}).children:
	    data_content = json.loads(child)
	    LINK = data_content["ou"]
	     #dowload the photo 
	    print LINK
	 	 
	 	
	res = requests.get(LINK, headers=hdr)
	with open(PHOTO_PATH, 'wb') as W:
		W.write(res.content)
	     
	#check if photo is valid, if not, try another photo, keep trying until you get one		
	invalid_jpeg = (imghdr.what(PHOTO_PATH)!="jpeg")



#set as wallpaper
#commands works for unity in my Ubuntu 16.04, might be different for your desktop. Just google it. P.S. Difficult if you are using KDE
#@todo command for changing windows wallpaper

