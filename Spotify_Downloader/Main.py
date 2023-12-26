import spot
import functions
import youtube_api
import os




tracks = spot.getsongs()
print("now in main")
print(tracks[2])
nameAndArtistList = []
nameAndArtistdict = {'name': "", 'artist': ""}

#ima create a folder to download the songs into 
print(os.getcwd())
os.mkdir(tracks[2] + " downloaded")
print(os.getcwd + "\\" + tracks[2] + " downloaded")
print(os.getcwd())

# now i need to figure out how to go one by one, return only names and artists then shove into youtube downloader

if tracks[0] == 1:
    tracks = tracks[1]
    # print(tracks)
    for stuff in tracks:
            x = ""
            nameAndArtistdict = {'name': "", 'artist': ""}

            print("name of track: " + str(stuff['name'])) 
            print("Artists: ", end="")
            for arts in stuff['artists']:
                x += str(arts) + ", "
            # try:
            
            x = x[:len(x)-2]
            print(x)


            
            nameAndArtistdict['name'] = str(stuff['name'])
            nameAndArtistdict['artist'] = x
            nameAndArtistList.append(nameAndArtistdict)
            print("Track num: " + str(stuff['tracknum'] -1)) 
            print("-------------------------\n\n")


elif tracks[0] == 2: 
    print(tracks)

    tracks = tracks[1]
    for stuff in tracks:
                x = ""
                nameAndArtistdict = {'name': "", 'artist': ""}


                print("name of track: " + str(stuff['name'])) 
                print("Artists: ", end="")
                for arts in stuff['artists']:
                    x += str(arts) + ", "
                
                
                x = x[:len(x)-2]
                print(x)


                nameAndArtistdict['name'] = str(stuff['name'])
                nameAndArtistdict['artist'] = x
                nameAndArtistList.append(nameAndArtistdict)
                
                print("Track num: " + str(stuff['tracknum'])) 
                print("-------------------------\n\n")



print("Da list")
print(nameAndArtistList)

#now we download from youtube???

#im gonna limit the amount of stuff you can download cause i dont want to download 500 songs

# print(nameAndArtistList[0]['name'] + " by " + nameAndArtistList[0]['artist'])

# if len(nameAndArtistList) > 15:
#       print("Download in progress.......")
#       for num in range(0,15):
#        print(str(num + 1))
#        youtube_api.downloadfromyoutube(nameAndArtistList[num]['name'] + " by " + nameAndArtistList[num]['artist'])
#        print("\n")
# else: 
#      print("Download in progress.......")
#      for num in range(0,len(nameAndArtistList)):
#        print(str(num + 1))
#        youtube_api.downloadfromyoutube(nameAndArtistList[num]['name'] + " by " + nameAndArtistList[num]['artist'])
#        print("\n")
   
print("Download finished")


#now change each song into mp3

#now put into new folder

#now give each song metadata that contains their artists

#u done
                



