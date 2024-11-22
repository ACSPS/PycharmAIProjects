from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# List of songs
songs = [
    {"title": "Singapore", "file": "/static/Ken Carson - Singapore (Official Instrumental).mp3"},
    {"title": "Freestyle 2", "file": "/static/Ken Carson - Freestyle 2 (Instrumental).mp3"},
    {"title": "Astrothunder", "file": "/static/Travis Scott - ASTROTHUNDER (Instrumental).mp3"},
    {"title": "SDP Interlude", "file": "/static/Travis Scott - sdp interlude (Extended) (Instrumental).mp3"},
    {"title": "Cadillac", "file": "/static/Destroy Lonely - CADILLAC  (INSTRUMENTAL).mp3"},
    {"title": "New N3on", "file": "/static/Playboi Carti - New N3on (Official Instrumental).mp3"},
    {"title": "Shoota", "file": "/static/Playboi Carti - Shoota (feat. Lil Uzi Vert) [Instrumental].mp3"},
    {"title": "Solo", "file": "/static/Future - Solo (Official Instrumental).mp3"},
    {"title": "Beibs in the trap", "file": "/static/Beibs In The Trap - Travis Scottft.Nav (instrumental) FLP.mp3"},
    {"title": "Stay Schemin", "file": "/static/Rick Ross - Stay Schemin Instrumental  DOWNLOAD.mp3"},
    {"title": "No Role Modelz", "file": "/static/No Role Modelz- J. Cole (Instrumental).mp3"},
    {"title": "Timeless", "file": "/static/The Weeknd, Playboi Carti - Timeless (INSTRUMENTAL) BEST ON YOUTUBE.mp3"},
    {"title": "Pain 1993", "file": "/static/Drake - Pain 1993 feat. Playboi Carti [Official Instrumental].mp3"},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_song')
def get_song():
    song = random.choice(songs)
    return jsonify(song=song)

if __name__ == '__main__':
    app.run(debug=True)

