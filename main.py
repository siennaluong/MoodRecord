from flask import Flask, render_template, url_for, request, redirect

from datetime import datetime
from backend import authenticate_spotify, get_known_tracks, get_related_artists, get_unknown_tracks, select_tracks, create_playlist
import spotipy.util as util

app = Flask(__name__)


client_id = "CLIENT_ID"
client_secret = "CLIENT_SECRET"
redirect_uri = "REDIRECT_URI"
scope = 'user-library-read user-top-read playlist-modify-public user-follow-read user-read-recently-played'




@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        userName = request.form['username']
        return redirect(url_for("user", usr=userName))
    else:
        return render_template('welcome.html')
    

@app.route('/<usr>', methods=['POST','GET'])
def user(usr):

    if request.method == 'POST':
        mood = float(request.form['mood'])/100
        energy = float(request.form['energy'])/100
        dance = float(request.form['dance'])/100
        unknown_num = float(request.form['num'])/100
        known_num = 10- int(unknown_num)/10
        
        token = util.prompt_for_user_token(usr, scope, client_id, client_secret, redirect_uri)
        spotify_auth = authenticate_spotify(token)
        related_artists = get_related_artists(spotify_auth)
        known_tracks = get_known_tracks(spotify_auth)
        unknown_tracks = get_unknown_tracks(spotify_auth, top_artists)
        selected_unknown_tracks = select_tracks(spotify_auth, unknown_tracks, unknown_num, mood, energy, dance)
        selected_known_tracks = select_tracks(spotify_auth, known_tracks, known_num, mood, energy, dance)
        selected_tracks = []

        for track in selected_known_tracks:
            selected_tracks.append(track)
        for track in selected_unknown_tracks:
            selected_tracks.append(track)

        playlist = create_playlist(spotify_auth, selected_tracks)
        
        return redirect(url_for("get_email"))
    else:
        return render_template('playlist.html')
    
@app.route('/emailpage', methods=['POST','GET'])
def get_email():
    if request.method == 'POST':
        email = request.form['email']
        emailMail="mailto:" + str(email)
        print(emailMail)
        return render_template("result.html", email=emailMail)

    else:
        return render_template('email.html')


if (__name__=='__main__'):
    app.run(debug=True)

