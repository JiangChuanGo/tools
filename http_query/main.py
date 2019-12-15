# encoding = utf-8

import PySimpleGUI as sg
import requests
import json

# sg.change_look_and_feel("Light Gray")
sg.change_look_and_feel('DefaultNoMoreNagging') 

METHODS = ("GET", "POST")

layout = [
    [
        sg.Combo(METHODS, default_value="POST", size= (5, 1), key="-METHOD-", readonly=True, change_submits=True), 
        sg.Combo(("http://", "https://"), default_value="http://", size= (8, 1), key="-SCHEME-", readonly=True), 
        sg.Input("localhost:80/", tooltip="host:port/url", justification="left", key= "-URL-", size = (40, 1))
    ],
    [sg.Frame("Headers", layout = [[sg.Multiline( size=(55, 1), tooltip="heads with json-style",key= "-HEADERS-")]])],
    [sg.Frame("Body", layout = [[sg.Multiline( size=(55, 1), tooltip="body string", key= "-BODY-")]])],
    [sg.Frame("Return Text (read Only!)", layout = [[sg.Multiline( size=(55, 10), tooltip="return text", key= "-TEXT-", disabled=True)]])],
    [sg.Button("Submit", key = "-SUBMIT-"), sg.Button("Clear", key = "-CLEAR-")]
]

def clear_all(window):
    window["-HEADERS-"].update("")
    window["-BODY-"].update("")
    window["-TEXT-"].update("")

def do_query(method, url, headers = None, body = None):
    if method not in METHODS:
        raise Exception("unsupported Method " + method)

    headers = headers.strip()
    body = body.strip()

    try:
        headers_dict = {} if headers == "" else json.loads(headers)
    except Exception as e:
        raise Exception("parse Headers Error:" + str(e))

    if not isinstance(headers_dict, dict):
        raise Exception("headers should be json data")

    if method == "POST":
        ret = requests.post(url, headers = headers_dict, data = body.encode("utf-8"))
    elif method == "GET":
        ret = requests.get(url, headers = headers_dict)

    if ret.status_code != requests.codes.ok:
        raise Exception("server status code:" +  str(ret.status_code))

    return ret.text



window = sg.Window("APP", layout = layout)

while True:
    event, values = window.read()

    if event is None:
        break

    if event == "-METHOD-":
        method = values["-METHOD-"]

        if method == "POST":
            window["-BODY-"].update("", background_color = "white", disabled = False)
        else:
            window["-BODY-"].update("Only work in POST method", background_color = "gray", disabled = True)

        continue

    if event == "-CLEAR-":
        clear_all(window)
        continue

    if event == "-SUBMIT-":
        method = values["-METHOD-"]
        url = values["-SCHEME-"] + values["-URL-"]
        headers = values["-HEADERS-"]
        body = values["-BODY-"]

        try:
            ret = do_query(method, url, headers, body)
            window['-TEXT-'].update(ret)
        except Exception as e:
            sg.Popup(str(e))

        continue

window.close()
