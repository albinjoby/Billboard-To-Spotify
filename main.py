from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

date = input("enter the data in this format YYYY-MM-DD: ")
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url=url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_span = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_span]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri = "https://albinjoby.vercel.app/",
        client_id = os.getenv("CLIENT_ID"),
        client_secret = os.getenv("CLIENT_SECRET"),
        show_dialog = True,
        cache_path = "token.txt"
    )
)

user_id = sp.current_user()["id"]
print(user_id)

songs = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}",type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        track = result["tracks"]["items"][0]["name"]
        artist = result["tracks"]["items"][0]["artists"][0]["name"]
        songs.append(uri)
        print(track,"found")
    except IndexError:
        print(song,"not found")

playlist = sp.user_playlist_create(user=user_id, name=f"BillBoard 100 {date}", public=False)
print(f"Created playlist: {playlist['name']}")

if songs:
    sp.playlist_add_items(playlist_id=playlist["id"],items=songs)
    print("songs were sucessfully added")
else:
    print("no songs were added")