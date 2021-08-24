# Please Don't Stop the Music: A Playlist Continuation Program
<div align="center"><img src="https://github.com/allisonjaye/playlist_continuation/blob/main/images/397-3976701_spotify-logo-green-png.jpeg" width="275" height="100">
    
<div align="left">

## Table of contents
- [Introduction](#introduction)
    - [Overview](#overview)
    - [Motivation](#motivation)
- [Exploratory Data Analysis](#exploratory-data-analysis)
    - [Data Descriptions](#data-descriptions)
    - [Visualizations](#visualizations)
- [Models](#models)
    - [Baseline Model](#baseline-model)
    - [Collaborative Filtering](#collaborative-filtering)
- [Results](#results)
    - [Recommendation Web App](#recommendation-web-app)
- [Next Steps](#next-steps)
## Introduction
### Overview
This program is designed to automatically continue a user's playlist on any music platform - here, Spotify. When used, it will help users find new music they enjoy as well as keep them using the platform longer. My steps for completing this program start with exploring and learning about the data. Then I created a simple baseline model as a reference point for improvement. Using multiple different models, I predicted if a user would enjoy the songs enough to add them to their playlist. Finally, I implemented the best model into a web app to recommend songs from a random playlist.

### Motivation
Over the past decade, music streaming services have become increasingly popular, changing the way consumers interact with their audio content. Listeners are no longer bound to predetermined track listings on an album or record; rather, they are free to construct their own playlists as they see fit. As a result, the task of automatic playlist generation has become increasingly relevant to the streaming community. These services rely on intelligent systems in order enhance the playlist creation experience, analyzing user preferences and tastes to recommend new songs. This project seeks to test the power of these recommendation models – observing which techniques perform best in the playlist continuation task.

## Exploratory Data Analysis
### Data Descriptions
The data used in this program is from Spotify's Million Playlist Dataset. It is publically accessable [here](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge/dataset_files). The file structure consists of 10,000 .json subfiles, with each subfile containing 1,000 playlists. Each playlist object contains the following attributes:

- **'collaborative'**: boolean (describes whether or not it is a collaborative playlist)
- **'duration_ms'**: int (the duration of the entire playlist in milliseconds)
- **'modified_at'**: int (the Unix Epoch Time value of when the playlist was last modified)
- **'name'**: str (name of the playlist)
- **'num_albums'**: int (number of unique albums in the playlist)
- **'num_artists'**: int (number of unique artists in the playlist)
- **'num_edits'**: int (number of times the playlist has been edited)
- **'num_followers'**: int (number of users that follow the playlist)
- **'num_tracks'**: int (number of tracks on the playlist)
- **'pid'**: int (the playlist ID number, ranging from 0 - 999,999,999)
- **'tracks'**: list of track objects (contains a list of tracks, where each track is an object containing the following attributes:
    - {**'album_name'**: str (the name of the track’s album)
    - **'album_uri'**: str (the unique album ID -- uniform resource identifier)
    - **'artist_name'**: str (the name of the artist)
    - **'artist_uri'**: str (the unique artist ID -- uniform resource identifier)
    - **'duration_ms'**: int (the duration of the track in milliseconds)
    - **'pos'**: int (the track’s position in the playlist)
    - **'track_name'**: str (the name of the track)})

### Visualizations
Taking a look into the data, the songs that appeared most frequently in all of the playlists were mostly rap/hip-hop.
    
<img src="https://github.com/allisonjaye/playlist_continuation/blob/main/images/pop_songs.jpg" width="720" height="432">
    
The most popular song *titles* were very similar but not exactly the same due to some songs having the same title.
    
<img src="https://github.com/allisonjaye/playlist_continuation/blob/main/images/pop_song_titles.jpg" width="720" height="432">
    
I found that the most popular playlist title was 'Country'.
    
<img src="https://github.com/allisonjaye/playlist_continuation/blob/main/images/pop_playlist_titles.jpg" width="720" height="432">
    
The most popular artists throughly the playlist corresponded highly with the most popular songs.
    
<img src="https://github.com/allisonjaye/playlist_continuation/blob/main/images/pop_artists.jpg" width="720" height="432">
    
The same with the most popular albumns.
    
<img src="https://github.com/allisonjaye/playlist_continuation/blob/main/images/pop_albums.jpg" width="720" height="432">
    
Most popular album *titles* throughout the playlists also include 'Greatest Hits' because so many different artists have an album with this title.
    
<img src="https://github.com/allisonjaye/playlist_continuation/blob/main/images/pop_album_titles.jpg" width="720" height="432">

## Models
    
### Baseline Model
To start, I created a baseline model as a reference point for growth. This model recommended most popular songs as a continuation for any playlist. From exploring the data, it seemed that this would work well for playlists that were mostly rap/hip-hop based but not so well with any other genre. With most playlists being titled 'Country', this model would not work well very often.
    
### Collaborative Filtering
To combat this, I added a collaborative filtering algorithm. I shifted the data into a sparse matrix with each playlist on one side and all of the songs on the other. If a song was on a playlist, it received a one and otherwise, it received a zero. I then used K-Nearest Neighbors to find similarities between each playlist based on values of song. From the top 500 most similar playlists, the algorithm compiles the most common songs not including the songs already on given playlist. These songs are then recommended to the user. 
    
## Results
    
### Recommendation Web App
Using Streamlit, I was able to produce a functioning web application that allows the user a choice of sample playlists to get recommendations from. Try it for yourself [here](https://share.streamlit.io/allisonjaye/playlist_continuation/main/website/knn.py). This is a screenshot example from the 'Classic Rock' playlist.
<img src="https://github.com/allisonjaye/playlist_continuation/blob/main/images/Screen%20Shot%202021-08-10%20at%2010.49.16%20PM.png" width="905" height="432">

## Next Steps
I plan continue improving my program by tuning hyperparameters, testing more models, and including a matrix factorization technique like SVD or NMF. I will also develop the website's capabilities to allow users to imput their own playlists or even just songs that they enjoy. Using another dataset with meta data about each song, I will implement a hybrid recommender that not only finds similarities in the playlists, but in the songs themselves. Instead of using human opinion as a measurement of accuracy, I will create a testing method to be able to see how well each model is doing numerically.
