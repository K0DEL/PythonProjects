from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID = "daa68e16d38c4ecc9622fa69135ecea1"
CLIENT_SECRET = "174fa19a07804b85be1bd47aa60c2cb7"

date = input(
    "Enter the date you wanna travel to in the format of YYYY-MM-DD: "
)
billboard_url = "https://www.billboard.com/charts/hot-100/"

response = requests.get(billboard_url + date)

soup = BeautifulSoup(response.text, "html.parser")

span_tags = soup.find_all(
    name="span",
    class_="chart-element__information__song text--truncate color--primary"
)

songs = [tag.getText() for tag in span_tags]

# print(songs)
scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    scope=scope,
    redirect_uri="https://example.com"
))
playlist_id = sp.user_playlist_create(
    name="Billboard 100 to Spotify" + date,
    user="g3d3b686wzwlabs23zee8quv1",
    description="This playlist is created using python",
    public=False,
    collaborative=False,
)

song_uris = []
for song in songs:
    print(song)
    items = sp.search(q=song, limit=1, type="track")['tracks']['items']
    if len(items) != 0:
        song_uris.append(items[0]['uri'])
        # print(type(items[0]['uri']))

# print(song_uris)

print(playlist_id['id'])
sp.user_playlist_add_tracks(
    user="g3d3b686wzwlabs23zee8quv1",
    playlist_id=playlist_id['id'],
    tracks=song_uris,
)

print("Plalist Created and Songs Added")
