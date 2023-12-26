import functions 
import json
import os
from pytube import YouTube
from googleapiclient.discovery import build

def downloadfromyoutube(x):
    api_key = 'AIzaSyCvtXA35t-JIgQcS1zERVFYKRdCJrCUKWk'

    youtube = build('youtube', 'v3', developerKey=api_key)

    newcall = youtube.search().list(
            part = 'snippet',
            q=x + ' music',
            type = 'video'
        )

    response = newcall.execute()
    # trash = json.load(response["items"])
    # print(response)

    # with open(".\penis.json","w") as dumpster:
    #     json.dumps(trash,dumpster)
    # # print(y)
    videos = []
    names = []
    descrip = []


    for sus in response['items']:
        # print("\n\n\n\5")
        # print(sus)
        for nuts in response['items']:
            names.append(nuts['snippet']['title'])
        for nuts in response['items']:
            videos.append(nuts['id']['videoId'])
        for nuts in response['items']:
            descrip.append(nuts['snippet']['description'])
    
    print("\n\n\n------Specified------")

    #specfic data to use
    # videoId = response[]

#below is the printing out of each vieos details, for our purposes we dont need to do that
    

    num = len(videos)
    for lol in range (num):
        print(names[lol])
        print(videos[lol])
        print('url: ' + functions.getlink(videos[lol]))
        
        print("\n")

    

    #trying to download the youtube video
    #making sure its not live

    print(functions.getlink(videos[1]))
    downloadedvid = YouTube(functions.getlink(videos[1]))
    name = downloadedvid.title
    thumbnail = downloadedvid.thumbnail_url
    readyfordownload = downloadedvid.streams.filter(only_audio=True)
    qualityStreams = str(readyfordownload)

    num = functions.getITAG(qualityStreams)


    #now finally we download

    stream = readyfordownload.get_by_itag(num)
    # print(stream)
    path = stream.download()
    print("path " + path)

    
                



    

