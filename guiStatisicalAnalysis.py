import PySimpleGUI as sg
import matplotlib.pyplot as plt
import datetime
import connectWorldBank, createGraph, createMenu, menu, createCountryList, check

# 登録されているmenuオブジェクトを生成。fieldとしてindicator,title,xlabel,ylabelを保持
# listbox(=titile)、dataframe取得時に利用する
menu_list = createMenu.create()
title_list = []
for menu in menu_list:
    title_list.append(menu.title)

# 入力値チェック、ポップアップ画面で使用
country_list = createCountryList.create()

# define layout
layout = [
    [
        sg.Listbox(title_list, size=(50, len(menu_list)), key="list_box",
         default_values=[title_list[0]], select_mode=sg.LISTBOX_SELECT_MODE_SINGLE)
  ],[
    sg.Text("[Countries]")
  ],[
    sg.Text("please input country code. you can input max 5 countries.")
  ],[
    sg.InputText(default_text = "JP", key = "country1", size = (15,1))
  ],[
    sg.InputText(default_text = "US", key = "country2", size = (15,1))
  ],[
    sg.InputText(default_text = "CN", key = "country3", size = (15,1))
  ],[
    sg.InputText(default_text = "IN", key = "country4", size = (15,1))
  ],[
    sg.InputText(default_text = "", key = "country5", size = (15,1))
  ],[
    sg.Button(
      "search",
      key = "bt_search")
  ],[
    sg.Text("", key = "error", size = (50,1), text_color='pink')
  ],[
    sg.Text("if you don't know country code, please check it.\nhttps://en.wikipedia.org/wiki/ISO_3166-1", size = (100,2))
  ],[
    sg.Button("country code", key = "bt_country")
  ]
]

# define window
window = sg.Window("Statistical Analysis", layout, size = (400,500))

# define action
while True:
  event, values = window.read()
  if event == None:
    break
  elif event == "bt_search":
    window["error"].update("")
    countries = []
    # 入力値があればlistに登録。入力値チェック処理、dataframe取得時に利用
    for num in range(1,6):
      if values["country" + str(num)] != "":
        countries.append(values["country" + str(num)])
    if check.isExist(countries) == False:
      window["error"].update("input data error. country code is not exist.")
    elif check.isUnique(countries) == False:
      window["error"].update("input data error. country code is not unique.")
    else:
      # pandasでWorldBankに接続、選択したメニューのdataframeを取得
      for menu in menu_list:
        if menu.title == values["list_box"][0]:
          select_indicator = menu.indicator
          select_title     = menu.title 
          select_xlabel    = menu.xlabel
          select_ylabel    = menu.ylabel
      dfs = connectWorldBank.worldBank(countries, select_indicator)
      createGraph.Graph(dfs, select_title, select_xlabel, select_ylabel)
  elif event == "bt_country":
    sg.popup_scrolled("[country code]\n", country_list)

window.close()
