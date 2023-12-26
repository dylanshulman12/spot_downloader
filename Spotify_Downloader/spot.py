import spotipy
from spotipy.oauth2 import SpotifyOAuth
import functions

def getsongs():



    

    SPOTIPY_CLIENT_ID='2b6b3df4e4fd4aa3acccce716b7e7149'
    SPOTIPY_CLIENT_SECRET='af9defde96024172819c3e1c0322e8f3'
    SPOTIPY_REDIRECT_URI='http://localhost:1234/'



    profileCall = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                                client_secret=SPOTIPY_CLIENT_SECRET,
                                                redirect_uri=SPOTIPY_REDIRECT_URI,
                                                scope="user-read-private"))

    #getting user name:
    call = profileCall.current_user()
    # print(call)
    print("\n\n\n -------------------------------")
    dispName = call['display_name']

    # get albums first
    alb = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                                client_secret=SPOTIPY_CLIENT_SECRET,
                                                redirect_uri=SPOTIPY_REDIRECT_URI,
                                                scope="user-library-read"))

    alb1 = alb.current_user_saved_albums(limit=50, offset=0)


    playlists = []

    for item in alb1['items']:
        n = item['album']['name']
        im = item['album']['images'][0]['url']

        d = item['album']['id']
        o = 'album/compilation'
        v = 'public'
        r = item['album']['tracks']['total']
        playlists.append(functions.playlistDict(n,im,d,o,v,r))

    albumlistnum = len(playlists)
    print(str(albumlistnum) + "\n\n\nplaylists: ")
    #getting user playlists
    playCall = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                                client_secret=SPOTIPY_CLIENT_SECRET,
                                                redirect_uri=SPOTIPY_REDIRECT_URI,
                                                scope="playlist-read-private"))

    call2 = playCall.current_user_playlists(limit=50, offset=0)
    #gathering data
    # print(call2)


    for item in call2['items']:
        n = item['name']
        im = item['images'][0]['url']

        d = item['id']
        o = item['owner']['display_name']
        v = item['public']
        r = item['tracks']['total']
        playlists.append(functions.playlistDict(n,im,d,o,v,r))

    numberPlay = 0;
    #Now that we have all of that data saved I shall attempt to print it all out!!!!
        
    # print(playlists)
    print("\n\n ---------------------------- \n All DATA IN A READABLE FORMAT \n\n")

    print("Display name " + dispName)
    for l in playlists:
        print(numberPlay)
        print("name: " + l['name'])
        print("Playlist owner " + l['owner'])
        print("id: " + l['id'])
        print("imageURL: " + str(l['imageUrl']))
        print("viewability: " +  str(l['viewability']))
        print("track number: " +  str(l['tracknum']))
        print("-------------------- \n")
        numberPlay+=1
        


    #user select a playlist...
    userInput = input("------------------- \n What playlist would you like to download \n ----------------------")
    playlistPick = playlists[int(userInput)]['name']
    Mode = 0
    if (int(userInput) <= albumlistnum): #getting tracks for albums

        Mode = 1
        userInput = playlists[int(userInput)]['id']
        ListSongs = playCall.album_tracks(userInput, limit=50, offset=0)
        tracks = functions.getEverythinginDictalbums(ListSongs)
        print("mode: " + str(Mode))

        return [Mode, tracks, playlistPick]
    


        #aight now lets print out the items of a selected playlist. 

        #we can reuse playCall because it has ther same scope
            
        # for stuff in tracks:
        #     print(stuff)
        #     print("\n")

        

    else: #this is getting tracks for playlists
        Mode = 2



        #set user input variable to the id of the playlist, so we can reuse the variable here, too lazy to make another one

        userInput = playlists[int(userInput)]['id']


        #aight now lets print out the items of a selected playlist. 

        #we can reuse playCall because it has ther same scope
            
        ListSongs = playCall.playlist_items(userInput, fields='total,items', limit=100, offset=0, additional_types=['track'])



        # print(ListSongs['items'][1])

        # with open("sus.json", "w") as paper:
        #     x = ""
        #     for i in ListSongs['items']:
        #         x+= str(i) + "\n"
        #     paper.write(x)


        tracks = functions.getEverythinginDict(ListSongs)





        # for stuff in tracks:
        #     print(stuff)
        #     print("\n")

        #End prgrm
    
    print("mode: " + str(Mode))
    return [Mode, tracks, playlistPick];