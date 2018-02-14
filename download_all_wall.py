#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import urllib2, urllib
from bs4 import BeautifulSoup
import json
from random import randint
import requests
import subprocess
import time
import imghdr
import os

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

DOWNLOAD_PATH = "wallpaper/{}/".format(sys.argv[1])
if not os.path.exists(DOWNLOAD_PATH):
    os.makedirs(DOWNLOAD_PATH)


#manipulate user agent so as to make them believe we are just normal human downloading some image
hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

#make a request and get html in beautiful soup
req = urllib2.Request(SEARCH_URL,headers=hdr)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page, 'html.parser')

#print soup.prettify()

#scrap the html to find link of image (just refer to html printed in above prettify line to find what html google returns)
#google image will give us total 99 images (I think), just pick one randomly. And hope for the best.

invalid_jpeg = True

for i in range(99):

	#path for storing the photo
	PHOTO_PATH = DOWNLOAD_PATH + '{}_{}.jpg'.format(sys.argv[1] ,str(i))

	for child in soup.find("div", {"data-ri":"{}".format(str(i))}).find("div", {"class":"rg_meta"}).children:
	    data_content = json.loads(child)
	    LINK = data_content["ou"]
	     #dowload the photo 
	    print LINK
	 	
	res = requests.get(LINK, headers=hdr)
	with open(PHOTO_PATH, 'wb') as W:
		W.write(res.content)
		
	if(imghdr.what(PHOTO_PATH)!="jpeg"):
		#delete the file
		os.remove(PHOTO_PATH)
		    

	


