import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import csv

# Document: https://spotipy.readthedocs.io/en/2.18.0/

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="MYID",
                                                           client_secret="MYSECRET"))

# アーティストページ3点メニュー > シェア > アーティストのリンクをコピーより取得
artist_url = "https://open.spotify.com/artist/3YQKmKGau1PzlVlkL1iodx?si=mKSuQzQTS3yVat7ZmAnXGg"
output_file = "music_data.csv"

results = sp.artist_top_tracks(artist_url)


# トップ 10 トラックの 30 秒サンプルとカバー アートを取得する方法を示す
for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()

# 関連アーティストの出力
results = sp.artist_related_artists(artist_url)
result = results['artists']
related_df = pd.DataFrame(
    # columns=['Name', 'Genres', 'Images_url', 'Popularity', 'URL', 'URI'])
    columns=['Name', 'Genres', 'Popularity'])

for i in range(len(result)):
    append_df = {
        'Name': result[i]['name'],
        'Genres': ", ".join(result[i]['genres']),
        # 'Images_url': result[i]['images'][0]['url'],
        'Popularity': result[i]['popularity'],
        # 'URL': result[i]['external_urls']['spotify'],
        # 'URI': result[i]['uri']
    }

    related_df = pd.concat([related_df, pd.DataFrame(
        append_df, index=[0])], ignore_index=True)
print(related_df)

# CSV出力
related_df.to_csv(output_file, encoding='utf-8')
with open(output_file, 'a', newline='') as f:
    writer = csv.writer(f)
