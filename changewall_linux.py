#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
try:
	from urllib.request import Request, urlopen  # Python 3
except ImportError:
	from urllib2 import Request, urlopen  # Python 2
from bs4 import BeautifulSoup
import json
from random import randint
import requests
import subprocess
import imghdr
import Wallpaper
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filepath", help="[Optional] Give file path to store wallpaper")
parser.add_argument("-s", "--search_string", help="Give the search string")
args = parser.parse_args()

#if file path given, use that, or else use the directory in which script is being run
if args.filepath:
    print "File path given"
    PHOTO_PATH = args.filepath 
else:
    import os
    PHOTO_PATH = os.path.dirname(os.path.abspath(__file__)) + "/photo.jpg"

if args.search_string:
    SEARCH_NAME = args.search_string
else:
    print "Give search string. Usage : changewall.py -s \"Search String\""
    exit()


#Replace search string with + in place of whitespace
SEARCH_NAME +=" HD DESKTOP WALLPAPER"
SEARCH_NAME = SEARCH_NAME.replace(' ','+')
print(SEARCH_NAME)

#prepare google search url
SEARCH_URL = "https://www.google.co.in/search?q={}&source=lnms&tbm=isch&tbs=isz:ex,iszw:1920,iszh:1080".format(SEARCH_NAME)
print(SEARCH_URL)

#manipulate user agent so as to make them believe we are just normal human downloading some image
hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

#make a request and get html in beautiful suop
#req = urllib2.Request(SEARCH_URL,headers=hdr)
req = Request(SEARCH_URL)
req.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36");
page = urlopen(req).read()
soup = BeautifulSoup(page, 'html.parser')

#print(soup.prettify()

#scrap the html to find link of image (just refer to html printed in above prettify line to find what html google returns)
#google image will give us total 99 images (I think), just pick one randomly. And hope for the best.
invalid_jpeg = True
while invalid_jpeg:
	for child in soup.find("div", {"data-ri":"{}".format(str(randint(0,99)))}).find("div", {"class":"rg_meta"}).children:
	    data_content = json.loads(child)
	    LINK = data_content["ou"]
	     #dowload the photo 
	    print(LINK)
	 	 
	 	
	res = requests.get(LINK, headers=hdr)
	with open(PHOTO_PATH, 'wb') as W:
		W.write(res.content)
	     
	#check if photo is valid, if not, try another photo, keep trying until you get one		
	invalid_jpeg = (imghdr.what(PHOTO_PATH)!="jpeg")



#set as wallpaper
wallpaper = Wallpaper.Wallpaper()
wallpaper.change(PHOTO_PATH)
