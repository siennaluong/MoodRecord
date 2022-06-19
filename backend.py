import spotipy
import spotipy.util as util

import random



def authenticate_spotify(token):
    print('...connecting to Spotify')
    sp=spotipy.Spotify(auth=token)
    return sp


def get_known_tracks(sp):
        print('...getting your most recently played songs')
        known_tracks = []

        recently_played_total_info = sp.current_user_recently_played(limit=20)

        for recently_played_info in recently_played_total_info['items']:
            known_tracks.append(recently_played_info['track']['uri'])

        print("...getting your saved tracks")

        saved_tracks_total_info = sp.current_user_saved_tracks(limit=50)

        for saved_track in saved_tracks_total_info['items']:
            if saved_track['track']['uri'] not in known_tracks:
                known_tracks.append(saved_track['track']['uri'])
        return known_tracks


def get_related_artists(sp):
        print('...getting your top artists')
        top_artists_id = []
        top_artists_uri = []
        recommended_id = []
        recommended_uri = []

        top_artists_all_data = sp.current_user_top_artists(limit=20, time_range='medium_term')
        top_artists_data = top_artists_all_data['items']
        for artist_data in top_artists_data:
            if artist_data["id"] not in top_artists_id:
                top_artists_id.append(artist_data['id'])
                top_artists_uri.append(artist_data['uri'])

        for identifier in top_artists_id:
            recommended_artist_info = sp.artist_related_artists(identifier)
            for artist in recommended_artist_info['artists']:
                if artist['id'] not in top_artists_id:
                    recommended_id.append(artist['id'])
                    recommended_uri.append(artist['uri'])
        return recommended_uri


def get_unknown_tracks(sp, top_artists_uri):
        print("...getting top tracks")
        top_tracks_uri = []
        for artist in top_artists_uri:
            top_tracks_all_data = sp.artist_top_tracks(artist)
            top_tracks_data = top_tracks_all_data['tracks']
            for track_data in top_tracks_data:
                top_tracks_uri.append(track_data['uri'])
        return top_tracks_uri


def select_tracks(sp, tracks_uri, num, mood, energy, dance):
        
        print("...selecting tracks")
        selected_tracks_uri = []
        count = 0

        def group(seq, size):
            return (seq[pos:pos + size] for pos in range(0, len(seq), size))

        random.shuffle(tracks_uri)
        for tracks in list(group(tracks_uri, 50)):

            tracks_all_data = sp.audio_features(tracks)

            for track_data in tracks_all_data:
                try:
                    if (count < num and track_data["valence"] <= mood
                            and track_data["danceability"] <= dance
                            and track_data["energy"] <= energy):
                        selected_tracks_uri.append(track_data["uri"])
                        count += 1
                    elif (count < num and mood < track_data["valence"] <= mood + 0.2
                          and dance < track_data["danceability"] <= dance + 0.2
                          and energy < track_data["energy"] <= energy + 0.2):
                        selected_tracks_uri.append(track_data["uri"])
                        count += 1
                    elif (count < num and mood < track_data["valence"] <= mood + 0.4
                          and dance < track_data["danceability"] <= dance + 0.4
                          and energy < track_data["energy"] <= energy + 0.4):
                        selected_tracks_uri.append(track_data["uri"])
                        count += 1

                except TypeError as te:
                    continue

        return selected_tracks_uri



def create_playlist(sp, selected_tracks_uri):

        print("...creating playlist")
        user_all_data = sp.current_user()
        user_id = user_all_data["id"]

        playlist_all_data = sp.user_playlist_create(user_id, "Your record of today mood")
        playlist_id = playlist_all_data["id"]

        sp.user_playlist_add_tracks(user_id, playlist_id, selected_tracks_uri[0:30])



