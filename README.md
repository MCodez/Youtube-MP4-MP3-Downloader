# Youtube-MP4-MP3-Downloader
This Python3 script will help you to search YouTube and download searched MP4 and MP3 from terminal.

## INSTALLATION
Install listed python libraries before running the script.
1. youtube_dl
2. BeautifulSoup
3. Urllib
You can install all the libraries using PIP or Wheel.
Script is written in Python3. ver 3.6+

## WORKING
Open the directory where you have saved the script. Run the script with a extra argument i.e. searchterm [which you want to search on YouTube]
Command would be in this format:

``` console 
lalit@con: python downloader.py "7 years"
```

Running this command, will search for the term on YouTube and will show Top 5 searches numbered from 1 to 5.
Enter the number corressponding to the MP4 or MP3 you want to download with a term i.e. Video or Music.
This command would be in this format { for downloading music of 1st searched item }

```
console
1 music
```

The Music file will be downloaded in same directory. Ignore any Exception.

## LOGIC 
I am using BeautifulSoup and Urllib to search for term on youtube and fetching the URLs and Titles of the videos. Top 5 searches will be stripped and will be displayed to user. 
Then youtube_dl library will be used to download the MP3 version or MP4 version of that video. MP3 version is actually extracting Audio from Video using FFmpeg.

For Detailed Documentation of youtube_dl, Visit this link. [Documentation](https://github.com/rg3/youtube-dl/blob/master/README.md#embedding-youtube-dl)
