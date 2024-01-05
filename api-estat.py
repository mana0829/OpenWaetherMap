# -*- coding; utf-8 -*-
"""
OpenWeatherMap からデータを取得する
rev 0.0 クジラ飛行机,増補改訂Pythonによるスクレイピング＆機械学習 開発テクニック 初版,ソシム（株）,2019
rev 0.1 入力フォーム追加 by M.Nakano
rev 0.2 apikey変更 by M.Nakano
"""
import requests
import json, pprint
from tkinter import *
from tkinter import ttk

# APIキーの指定 - 以下を書き換えてください★ --- (※1)
apikey = "556c2dd7923f2653ad118d89d374bf5b"
          
# 天気を調べたい都市の一覧 --- (※2)
cities = ["Tokyo,JP", "London,UK", "New York,US"]
# APIのひな型 --- (※3)
api = "https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

# 温度変換(ケルビン→摂氏) --- (※4)
k2c = lambda k: k - 273.15

# 各都市の温度を取得する --- (※5)
def get_waether():
    name = city_name.get()
    # APIのURLを得る --- (※6)
    url = api.format(city=name, key=apikey)
    # 実際にAPIにリクエストを送信して結果を取得する
    r = requests.get(url)
    # 結果はJSON形式なのでデコードする --- (※7)
    data = json.loads(r.text)
    # print(data) 
    # 結果を画面に表示 --- (※8)
    print("+ 都市=", data["name"])
    print("| 天気=", data["weather"][0]["description"])
    print("| 最低気温=", k2c(data["main"]["temp_min"]))
    print("| 最高気温=", k2c(data["main"]["temp_max"]))
    print("| 湿度=", data["main"]["humidity"])
    print("| 気圧=", data["main"]["pressure"])
    print("| 風速度=", data["wind"]["speed"])
    print("")


#Comboboxの選択項目用リスト
cb_city_name = ['Tokyo,JP', 'London,UK', 'New York,US']

#ウィンドウを作成
app = Tk()

#ウィンドウサイズを指定
app.geometry("320x240")

#ウィンドウタイトルを指定
app.title('天気')

frame1 = ttk.Frame(app, padding=(32))
frame1.grid()

#都市
# Combobox
city_name = StringVar()
city_name_cb = ttk.Combobox(
    frame1, 
    textvariable=city_name, 
    values=cb_city_name, 
    width=20)
city_name_cb.set(cb_city_name[0])
city_name_cb.bind(
    '<<ComboboxSelected>>')
city_name_cb.grid(row=0, column=1)

# Button
button1 = ttk.Button(frame1, text='OK', command=get_waether)
button1.grid(row=1, column=1)

#ウィンドウ表示継続
app.mainloop()



