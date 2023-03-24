import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 流行りのアーティストの多変量分析
# 音楽の特徴量（例えば、曲の長さ、テンポ、キー、歌詞の難易度、アーティストの人気度など）と、それらの特徴量から導き出される目的変数である「流行度」を用いて、線形回帰モデルを構築
# spotipy_intro.pyで作成したデータセットmusic_data.csvを読み込み、Popularity列を目的変数として使用

# データセットの読み込み
music_data = pd.read_csv('music_data.csv')

print(music_data)

music_data = pd.get_dummies(music_data, columns=['Name'])

# ジャンルの分割
genres = music_data['Genres'].str.get_dummies(', ')
music_data = pd.concat([music_data, genres], axis=1)
music_data = music_data.drop(['Genres'], axis=1)

# 特徴量と目的変数の分離
X = music_data.drop(['Popularity'], axis=1)
y = music_data['Popularity']

# 訓練データとテストデータに分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

# 線形回帰モデルの学習
model = LinearRegression()
model.fit(X_train, y_train)

# テストデータでの予測
y_pred = model.predict(X_test)

# モデルの評価
# テストデータでモデルの予測を行い、scoreメソッドを使用して、モデルの評価指標であるR^2スコアを計算。
# このスコアは、0から1までの範囲であり、1に近いほどモデルの予測精度が高い
score = model.score(X_test, y_test)
print('R^2 score:', score)

# => R^2 score: 0.7273191931299534
