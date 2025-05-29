# import requests
# from bs4 import BeautifulSoup
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
#
# date = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: ")
# response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}").text
# soup = BeautifulSoup(response, "html.parser")
# song_titles = soup.select("li ul li h3")
# tracks_list = [song.get_text(strip=True) for song in song_titles]
# artist_list = [song.find_next_sibling("span").get_text(strip=True) for song in song_titles]
# data = [{"track": tracks_list[i], "artist": artist_list[i]} for i in range(100)]
# print(data)
#
# # Spotify authentication
# client_id = "1b60f12f3706402e85adbd700a70d3da"
# client_secret = "cd0c64cee0d84afe9e9e821729f8ee5c"
# redirect_url = "https://open.spotify.com"
#
# # Creating connections
# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope="playlist-modify-private",
#         redirect_uri=redirect_url,
#         client_id=client_id,
#         client_secret=client_secret,
#         cache_path="token.txt"
#     )
# )
#
# # create playlist
# playlist_name = f"Billboard Hot 100 - {date}"
# sp.user_playlist_create(user=client_id,
#                         name=playlist_name,
#                         public=True,
#                         description="Automatically generated with Python 🫶")
#
# # get song uris
# uris = []
# for song in data:
#     track = song["track"]
#     artist = song["artist"]
#     try:
#         result = sp.search(q=f"track: {track} artist: {artist}")
#         uris.append(result["tracks"]["items"][0]["uri"])
#     except IndexError:
#         print("Song not found.")
#
# # find correct playlist id
# playlists = sp.user_playlists(user=client_id)["items"]
# playlist_id = [playlist["id"] for playlist in playlists if playlist["name"] == playlist_name][0]
#
# # add songs
# sp.user_playlist_add_tracks(user=client_id,
#                             playlist_id=playlist_id,
#                             tracks=uris)


import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint
from bs4 import BeautifulSoup

SPOTIFY_CLIENT_ID = "1b60f12f3706402e85adbd700a70d3da"
SPOTIFY_SECRET = "cd0c64cee0d84afe9e9e821729f8ee5c"
REDIRECT_URL = "https://open.spotify.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URL,
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_SECRET,
        cache_path="token.txt"
    )
)

SONG_YEAR = input("What year would you like to travel back to? Enter YYYY-MM-DD format: ")
BILL_BOARD_URL = f"https://www.billboard.com/charts/hot-100/{SONG_YEAR}/"
SONG_YEAR_YEAR = SONG_YEAR.split("-")[0]
print(SONG_YEAR_YEAR)

response = requests.get(BILL_BOARD_URL)
song_scrape = response.text

soup = BeautifulSoup(song_scrape, "html.parser")

song_tags_list = soup.findAll(name="h3", class_="a-no-trucate")
artists_tags_list = soup.findAll(name="span", class_="a-no-trucate")


song_list_1 = [tag.getText().replace("\n", "") for tag in song_tags_list]
song_list_2 = [song.replace("\t", "") for song in song_list_1]

artist_list_1 = [tag.getText().replace("\n", "") for tag in artists_tags_list]
artist_list_2 = [artist.replace("\t", "") for artist in artist_list_1]

song_artist_list = dict(zip(artist_list_2, song_list_2))
# pprint(song_artist_list)


results = sp.current_user()
# pprint(results)
user_id = results['id']

# print(results)
# print(user_id)

spotify_song_uris = []
# TAKEN OUT OF BELOW FOR LOOP ['artists'][0] -> remember to add back in
for key, value in song_artist_list.items():
    spotify_result = sp.search(q=f"artist:{key} track:{value} year:{SONG_YEAR_YEAR}", type="track")
    try:
        song_uri = spotify_result['tracks']['items'][0]['uri']
        spotify_song_uris.append(song_uri)
    except IndexError:
        print(f"{value} doesn't exist in Spotify. Skipped.")

print(len(spotify_song_uris))

my_playlist = sp.user_playlist_create(user=f"{user_id}", name=f"{SONG_YEAR} Billboard Top Tracks", public=False,
                                      description="Top Tracks from back in the Dayz of Brunel")
