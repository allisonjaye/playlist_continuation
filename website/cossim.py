import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import load_npz
from collections import Counter
import pickle

data = pd.read_pickle('data.pkl')

st.title("Please Don't Stop The Music:")
st.header("A Playist Continuation Program")
with st.form('my form'):
    random_playlists = ['Throwbacks', 'Country jams', 'Classic Rock', 'Christmas', 'Disney']
    p_name = st.selectbox('Choose a Playlist', (random_playlists))
    playlist_index = data[data.playlist_name == p_name]["pid"].values[0]
    col1, col2 = st.columns(2)
    submitted1 = col1.form_submit_button("Check it Out")
    col1.header("Original Playlist")
    submitted2 = col2.form_submit_button("Recommend Songs")
    col2.header("Recommendations")

    if submitted1:
        with col1:
            play_tracks = data[data.pid == playlist_index]['trackid'].sample(5, random_state=1).tolist()
            track1, track2, track3, track4, track5 = play_tracks
            print(components.iframe(f"https://open.spotify.com/embed/track/{track1}", height=80, width=300))
            print(components.iframe(f"https://open.spotify.com/embed/track/{track2}", height=80, width=300))
            print(components.iframe(f"https://open.spotify.com/embed/track/{track3}", height=80, width=300))
            print(components.iframe(f"https://open.spotify.com/embed/track/{track4}", height=80, width=300))
            print(components.iframe(f"https://open.spotify.com/embed/track/{track5}", height=80, width=300))


    if submitted2:
        with col1:
            play_tracks = data[data.pid == playlist_index]['trackid'].sample(5, random_state=1).tolist()
            track1, track2, track3, track4, track5 = play_tracks
            print(components.iframe(f"https://open.spotify.com/embed/track/{track1}", height=80, width=300))
            print(components.iframe(f"https://open.spotify.com/embed/track/{track2}", height=80, width=300))
            print(components.iframe(f"https://open.spotify.com/embed/track/{track3}", height=80, width=300))
            print(components.iframe(f"https://open.spotify.com/embed/track/{track4}", height=80, width=300))
            print(components.iframe(f"https://open.spotify.com/embed/track/{track5}", height=80, width=300))
        with col2:
            with open("pivot_columns.txt", "rb") as fp:
                pivot = pickle.load(fp)
            sparse = load_npz('sparse.npz')

            cos_sim = cosine_similarity(sparse)
            sim_playlists = list(enumerate(cos_sim[playlist_index]))
            sorted_similar_playlists = sorted(sim_playlists,key=lambda x:x[1],reverse=True)[1:]
            dif_songs = []
            for row in sorted_similar_playlists[:500]:
                dif = sparse[row[0]] - sparse[playlist_index]
                dif[dif==-1] = 0
                dif_indicies = dif.nonzero()
                dif_songs.append(dif_indicies[1])
            total = np.hstack(dif_songs)
            common = Counter(total).most_common(5)
            song_indicies_list = []
            for row in common:
                song_indicies_list.append(row[0])
                track_uri = []
                for index in song_indicies_list:
                    track_uri.append(data[data['track_name'] == pivot[index]]['trackid'].iloc[0])
            song1, song2, song3, song4, song5 = track_uri
            
            print(components.iframe(f"https://open.spotify.com/embed/track/{song1}", height=80, width=300))
            print(components.iframe(f"https://open.spotify.com/embed/track/{song2}", height=80, width=300))
            print(components.iframe(f"https://open.spotify.com/embed/track/{song3}", height=80, width=300))
            print(components.iframe(f"https://open.spotify.com/embed/track/{song4}", height=80, width=300))
            print(components.iframe(f"https://open.spotify.com/embed/track/{song5}", height=80, width=300))
            
    
