# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 19:44:44 2018

@author: LALIT ARORA
"""

from __future__ import unicode_literals
import youtube_dl
import urllib.parse
from bs4 import BeautifulSoup

def check_internet():
    try:
        urllib.request.urlopen('http://216.58.192.142', timeout=1)
        return True
    except : 
        return False
    
def youtube(searchterm):
    query=urllib.parse.quote(searchterm)
    url="https://www.youtube.com/results?search_query="+query
    response=urllib.request.urlopen(url)
    html=response.read()
    soup=BeautifulSoup(html,"lxml")
    links=[]
    names=[]
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        links.append('https://www.youtube.com' + vid['href'])
        try:
            names.append(vid['title'])
        except:
            names.append("")
    if len(links)>=5:
        return (links[:5],names[:5])
    elif len(links)==0:
        print ("No Search Results")
        exit(0)
    else:
        return (links,names)

def download_mp3(url):
    ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
            }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
def download_mp4(url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def search(term):
    res=youtube(term)
    for i in range(5):
        print(str(i+1)+" "+str(res[1][i]))
    return res
    
if __name__ == "__main__":
    import sys
    arguments=sys.argv
    searchterm=arguments[1]
    if (not check_internet()):
        print ("No Internet Connection")
        exit(0)
    g=search(searchterm)
    print("\nEnter the number of song or video to be downloaded in format <1 video> or <1 music>")
    mode=input()
    temp=mode.split(' ')
    number=int(temp[0])
    m=temp[1]
    if (m=="video"):
        download_mp4(g[0][number-1])
    elif (m=="music"):
        download_mp3(g[0][number-1])
    else:
        print("Wrong number entered.")
        exit(0)
        