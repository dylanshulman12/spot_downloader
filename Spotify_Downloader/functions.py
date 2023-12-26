from os import path
# from moviepy.editor import *
import requests


def getEverythinginDictalbums(a):
    songList = []
    x = 1
    
    print("Function \n\n\n-----------------")

    for i in a['items']:
        list = []
       
        for s in i['artists']:
            list.append(s['name'])
        
        print("\n\n\n")
        x+=1

        songList.append(song(i['name'],list,x))
    
    return songList


def getEverythinginDict(a):
    songList = []
    x = 1
    
    print("Function \n\n\n-----------------")

    for i in a['items']:
        list = []
       
        for s in i['track']['artists']:
            list.append(s['name'])
        
        print("\n\n\n")
        x+=1

        songList.append(song(i['track']['name'],list,x))
    
    return songList

  
def song(x,e,f):
    songItems = {'name':x, 'artists': e, 'tracknum':f }
    return songItems
        
def playlistDict(n, image, i, o, v, num):
    i = {'name':n, 'imageUrl': image, 'id': i, 'owner': o, 'viewability': v, 'tracknum':num }
    return i


def downloadImage(a,x):
    img_data = requests.get(a).content
    with open(x, 'wb') as handler:
        handler.write(img_data)









# youtube downloaders
#---------------------------------------------

def getlink(input):
    url = 'https://www.youtube.com/watch?v=' + input
    return url




def getITAG(a):
    qualityStreams = a

    #finding every itag, for best quality


    itagStore = []
    index1 = 0          
    while(len(qualityStreams) > 0):
        qualityStreams = qualityStreams[index1:]
        try:
            letter = qualityStreams.index('itag')
        except:
            pass
        itagStore.append(qualityStreams[letter+6:letter+9])
        index1 = letter+9
    
        if (letter+9 >= len(qualityStreams)):
            qualityStreams = qualityStreams[index1:]
        else: 
            pass


    # this will print the highest itag, which is always the last
        
    # print("\n" + str(itagStore))
    actuallen = len(itagStore) - 2
    # print(itagStore[actuallen])
    return int(itagStore[actuallen])


