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
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filepath", help="[Optional] Give file path to store wallpaper")
parser.add_argument("-s", "--search_string", help="Give the search string")
parser.add_argument("-n", "--number_of_photos", help="Give the number of photos to be downloaded")
args = parser.parse_args()

#if file path given, use that, or else use the directory in which script is being run

if args.search_string:
    SEARCH_NAME = args.search_string
else:
    print ("Give search string. Usage : changewall.py \"Search String\"")
    exit()

if args.filepath:
    print ("File path given")
    DOWNLOAD_PATH = args.filepath 
else:
    import os
    DOWNLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + "/wallpapers/{}".format(args.search_string)


if args.number_of_photos:
    if(int(args.number_of_photos)>99):
	print("Number must be less than 99")
	exit()
    PHOTO_COUNT = int(args.number_of_photos)+1





#Replace search string with + in place of whitespace
SEARCH_NAME +=" HD DESKTOP WALLPAPER"
SEARCH_NAME = SEARCH_NAME.replace(' ','+')

#prepare google search url
SEARCH_URL = "https://www.google.co.in/search?q={}&source=lnms&tbm=isch&tbs=isz:ex,iszw:1920,iszh:1080".format(SEARCH_NAME)
print SEARCH_URL

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

for i in range(int(PHOTO_COUNT)):

	#path for storing the photo
	PHOTO_PATH = DOWNLOAD_PATH + '/{}_{}.jpg'.format(args.search_string ,str(i))

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
		    

	


