# -*- coding; utf-8 -*-
"""
OpenWeatherMap からデータを取得する
rev 0.0 クジラ飛行机,増補改訂Pythonによるスクレイピング&機械学習 開発テクニック 初版,ソシム（株）,2019
rev 0.1 入力フォーム追加 by M.Nakano
rev 0.2 apikey変更 by M.Nakano
rev 0.3 textbox追加し、これに結果表示
"""
import requests
import json

# tkinterのインポート
import tkinter as tk
import tkinter.ttk as ttk

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
    text_area.delete(1.0, tk.END)
    name = data["name"]
    weather = data["weather"][0]["description"]
    temp_min = k2c(data["main"]["temp_min"])
    temp_max = k2c(data["main"]["temp_max"])
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind_speed = data["wind"]["speed"]
    # 結果を画面に表示 --- (※8)
    # テキストエリアに入力情報を表示
    info = f"""
都市: {name}
天気: {weather}
最低気温: {temp_min}
最高気温: {temp_max}
湿度: {humidity}
気圧: {pressure}
風速度: {wind_speed}
"""
    text_area.insert(tk.END, info)



#Comboboxの選択項目用リスト
cb_city_name = ['Tokyo,JP', 'London,UK', 'New York,US']

#ウィンドウを作成
app = tk.Tk()

#ウィンドウサイズを指定
app.geometry("320x240")

#ウィンドウタイトルを指定
app.title('天気')

frame1 = ttk.Frame(app)
frame1.pack()

#都市
# Combobox
city_name = tk.StringVar()
city_name_cb = ttk.Combobox(
    frame1, 
    textvariable=city_name, 
    values=cb_city_name, 
    width=30)
city_name_cb.set(cb_city_name[0])
city_name_cb.bind(
    '<<ComboboxSelected>>')
# city_name_cb.grid(row=0, column=0)
city_name_cb.pack()

# Button
button1 = ttk.Button(frame1, text='OK', command=get_waether)
# button1.grid(row=1, column=0)
button1.pack()

# テキストエリアを作成
text_area = tk.Text(frame1, height=9, width=50)
# text_area.grid(row=2, column=0)
text_area.pack()

#ウィンドウ表示継続
app.mainloop()



