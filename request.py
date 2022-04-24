import json
from models import Music


def get_music(type):
    with open ('itunes.json') as f:
        collection = json.load(f)

        music_list = []
        for song in collection['results']:
            if song['wrapperType'] == type:
                artistId=song.get('artistId')
                artistName=song.get('artistName')
                trackName=song.get('trackName')
                artistViewUrl=song.get('artistViewUrl')
                trackPrice=song.get('trackPrice')
                artworkUrl100=song.get('artworkUrl100')
                collectionViewUrl =song.get('collectionViewUrl')
                collectionName=song.get('collectionName')
                primaryGenreName=song.get('primaryGenreName')

                song_object =Music(artistId,artistName,trackName,trackPrice,artistViewUrl,artworkUrl100,collectionViewUrl,collectionName,primaryGenreName)
                music_list.append(song_object)
    
    return music_list
    
                