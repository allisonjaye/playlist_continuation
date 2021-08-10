import pandas as pd
import numpy as np
import json

def jsonToCSV():
    start = 0
    end = 1000
    while end != 11000:
        songPlaylistArray = []
        path = 'spotify_data/mpd.slice.' + str(start) + "-" + str(end-1) + '.json'
        d = json.load(open(path, 'r'))
        thisSlice = pd.DataFrame.from_dict(d['playlists'], orient='columns')
        for index, row in thisSlice.iterrows():
            for track in row['tracks']:
                songPlaylistArray.append([track['track_uri'], track['artist_name'], track['track_name'], row['pid'], row['name'], track['album_name'], track['album_uri'], track['pos']])
        songPlaylist = pd.DataFrame(songPlaylistArray, columns=['trackid', 'artist_name', 'track_name', 'pid', 'playlist_name', 'album_name', 'album_id', 'position'])
        songPlaylist.to_csv('data/' + str(start) + "-" + str(end-1) + '.csv', index=False)
        start += 1000
        end += 1000


if __name__ == '__main__':
    jsonToCSV()
