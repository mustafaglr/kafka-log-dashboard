from confluent_kafka import Consumer
from pymongo import MongoClient
import threading
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
from dash.dependencies import Input, Output
from multiprocessing import Process
import time


entry = [[['2019-04-09 13:11:25'], ['INFO'], ['Istanbul'], ['Hello-From-Istanbul']], [['2019-04-09 13:11:26'], ['FATAL'], ['London'], ['Hello-From-London']], [['2019-04-09 13:11:27'], ['FATAL'], ['Istanbul'], ['Hello-From-Istanbul']], [['2019-04-09 13:11:28'], ['INFO'], ['Moskow'], ['Hello-From-Moskow']], [['2019-04-09 13:11:29'], ['INFO'], ['Moskow'], ['Hello-From-Moskow']], [['2019-04-09 13:11:30'], ['FATAL'], ['Tokyo'], ['Hello-From-Tokyo']], [['2019-04-09 13:11:31'], ['DEBUG'], ['Istanbul'], ['Hello-From-Istanbul']], [['2019-04-09 13:11:32'], ['FATAL'], ['Beijing'], ['Hello-From-Beijing']], [['2019-04-09 13:11:33'], ['INFO'], ['London'], ['Hello-From-London']], [['2019-04-09 13:11:34'], ['INFO'], ['Tokyo'], ['Hello-From-Tokyo']], [['2019-04-09 13:11:35'], ['ERROR'], ['Tokyo'], ['Hello-From-Tokyo']], [['2019-04-09 13:11:36'], ['DEBUG'], ['Tokyo'], ['Hello-From-Tokyo']], [['2019-04-09 13:11:37'], ['WARN'], ['Tokyo'], ['Hello-From-Tokyo']], [['2019-04-09 13:11:38'], ['FATAL'], ['London'], ['Hello-From-London']], [['2019-04-09 13:11:39'], ['WARN'], ['Istanbul'], ['Hello-From-Istanbul']], [['2019-04-09 13:11:40'], ['WARN'], ['London'], ['Hello-From-London']], [['2019-04-09 13:11:41'], ['INFO'], ['Moskow'], ['Hello-From-Moskow']], [['2019-04-09 13:11:42'], ['FATAL'], ['Moskow'], ['Hello-From-Moskow']], [['2019-04-09 13:11:43'], ['DEBUG'], ['Tokyo'], ['Hello-From-Tokyo']], [['2019-04-09 13:11:44'], ['ERROR'], ['Moskow'], ['Hello-From-Moskow']], [['2019-04-09 13:11:45'], ['WARN'], ['Beijing'], ['Hello-From-Beijing']], [['2019-04-09 13:11:46'], ['DEBUG'], ['Beijing'], ['Hello-From-Beijing']], [['2019-04-09 13:11:47'], ['ERROR'], ['Istanbul'], ['Hello-From-Istanbul']], [['2019-04-09 13:11:48'], ['WARN'], ['Beijing'], ['Hello-From-Beijing']], [['2019-04-09 13:11:49'], ['DEBUG'], ['Beijing'], ['Hello-From-Beijing']], [['2019-04-09 13:11:50'], ['INFO'], ['Beijing'], ['Hello-From-Beijing']], [['2019-04-09 13:11:51'], ['INFO'], ['London'], ['Hello-From-London']], [['2019-04-09 13:11:52'], ['ERROR'], ['London'], ['Hello-From-London']], [['2019-04-09 13:11:53'], ['WARN'], ['Istanbul'], ['Hello-From-Istanbul']], [['2019-04-09 13:11:54'], ['ERROR'], ['Istanbul'], ['Hello-From-Istanbul']], [['2019-04-09 13:11:55'], ['FATAL'], ['London'], ['Hello-From-London']], [['2019-04-09 13:11:56'], ['WARN'], ['Istanbul'], ['Hello-From-Istanbul']], [['2019-04-09 13:11:57'], ['DEBUG'], ['Beijing'], ['Hello-From-Beijing']], [['2019-04-09 13:11:58'], ['INFO'], ['Moskow'], ['Hello-From-Moskow']], [['2019-04-09 13:11:59'], ['ERROR'], ['Tokyo'], ['Hello-From-Tokyo']], [['2019-04-09 13:12:00'], ['INFO'], ['Moskow'], ['Hello-From-Moskow']], [['2019-04-09 13:12:01'], ['DEBUG'], ['Istanbul'], ['Hello-From-Istanbul']], [['2019-04-09 13:12:02'], ['ERROR'], ['Tokyo'], ['Hello-From-Tokyo']], [['2019-04-09 13:12:03'], ['ERROR'], ['London'], ['Hello-From-London']], [['2019-04-09 13:12:04'], ['WARN'], ['Moskow'], ['Hello-From-Moskow']], [['2019-04-09 13:12:05'], ['WARN'], ['London'], ['Hello-From-London']], [['2019-04-09 13:12:06'], ['INFO'], ['Beijing'], ['Hello-From-Beijing']], [['2019-04-09 13:12:07'], ['DEBUG'], ['Istanbul'], ['Hello-From-Istanbul']], [['2019-04-09 13:12:08'], ['WARN'], ['Tokyo'], ['Hello-From-Tokyo']], [['2019-04-09 13:12:09'], ['INFO'], ['Tokyo'], ['Hello-From-Tokyo']], [['2019-04-09 13:12:10'], ['FATAL'], ['Tokyo'], ['Hello-From-Tokyo']], [['2019-04-09 13:12:11'], ['ERROR'], ['Moskow'], ['Hello-From-Moskow']], [['2019-04-09 13:12:12'], ['DEBUG'], ['Beijing'], ['Hello-From-Beijing']], [['2019-04-09 13:12:13'], ['FATAL'], ['Tokyo'], ['Hello-From-Tokyo']], [['2019-04-09 13:12:14'], ['INFO'], ['Tokyo'], ['Hello-From-Tokyo']], [['2019-04-09 13:12:15'], ['FATAL'], ['Tokyo'], ['Hello-From-Tokyo']], [['2019-04-09 13:12:16'], ['DEBUG'], ['Istanbul'], ['Hello-From-Istanbul']], [['2019-04-09 13:12:17'], ['WARN'], ['Beijing'], ['Hello-From-Beijing']], [['2019-04-09 13:12:18'], ['ERROR'], ['Beijing'], ['Hello-From-Beijing']], [['2019-04-09 13:12:19'], ['FATAL'], ['London'], ['Hello-From-London']], [['2019-04-09 13:12:20'], ['FATAL'], ['Istanbul'], ['Hello-From-Istanbul']], [['2019-04-09 13:12:21'], ['FATAL'], ['Beijing'], ['Hello-From-Beijing']], [['2019-04-09 13:12:22'], ['INFO'], ['Tokyo'], ['Hello-From-Tokyo']], [['2019-04-09 13:12:23'], ['FATAL'], ['Moskow'], ['Hello-From-Moskow']], [['2019-04-09 13:12:24'], ['DEBUG'], ['Moskow'], ['Hello-From-Moskow']], [['2019-04-09 13:12:25'], ['FATAL'], ['Beijing'], ['Hello-From-Beijing']], [['2019-04-09 13:12:26'], ['DEBUG'], ['Beijing'], ['Hello-From-Beijing']], [['2019-04-09 13:12:27'], ['WARN'], ['Beijing'], ['Hello-From-Beijing']], [['2019-04-09 13:12:28'], ['INFO'], ['Tokyo'], ['Hello-From-Tokyo']], [['2019-04-09 13:12:29'], ['INFO'], ['London'], ['Hello-From-London']], [['2019-04-09 13:12:30'], ['FATAL'], ['Moskow'], ['Hello-From-Moskow']], [['2019-04-09 13:12:31'], ['DEBUG'], ['Istanbul'], ['Hello-From-Istanbul']], [['2019-04-09 13:12:32'], ['FATAL'], ['London'], ['Hello-From-London']], [['2019-04-09 13:12:33'], ['ERROR'], ['Moskow'], ['Hello-From-Moskow']], [['2019-04-09 13:12:34'], ['FATAL'], ['Moskow'], ['Hello-From-Moskow']], [['2019-04-09 13:12:35'], ['WARN'], ['Moskow'], ['Hello-From-Moskow']], [['2019-04-09 13:12:36'], ['FATAL'], ['Beijing'], ['Hello-From-Beijing']], [['2019-04-09 13:12:37'], ['INFO'], ['Tokyo'], ['Hello-From-Tokyo']], [['2019-04-09 13:12:38'], ['INFO'], ['London'], ['Hello-From-London']], [['2019-04-09 13:12:39'], ['ERROR'], ['London'], ['Hello-From-London']], [['2019-04-09 13:12:40'], ['DEBUG'], ['Moskow'], ['Hello-From-Moskow']], [['2019-04-09 13:12:41'], ['ERROR'], ['Moskow'], ['Hello-From-Moskow']], [['2019-04-09 13:12:42'], ['INFO'], ['Beijing'], ['Hello-From-Beijing']], [['2019-04-09 13:12:43'], ['INFO'], ['Moskow'], ['Hello-From-Moskow']], [['2019-04-09 13:12:44'], ['DEBUG'], ['Tokyo'], ['Hello-From-Tokyo']], [['2019-04-09 13:12:45'], ['ERROR'], ['Moskow'], ['Hello-From-Moskow']]]
timeseries=['13:11:25']
countofmessage=[]
splitted = []

time_interval = 30

next = 0
oldentry = 0
plus = 0
rest = 0

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(
    html.Div([
        html.H4('Kafka Dashboard'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1 * 1000,
            n_intervals=0
        )
    ])
)

client = MongoClient("localhost", 27017)
db = client.get_database("people")
messages = db.get_collection("messages")

c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['my-topic'])


def listen():
    while True:
        msg = c.poll(1.0)
        if msg is None :
            continue
        if msg.error() :
            print("Consumer error: {}".format(msg.error()))
            continue

        splitted = msg.value().decode('utf-8').split(" ")
        entry.append([[splitted[0] + " " + splitted[1]], [splitted[2]], [splitted[3]], [splitted[4]]])
        messages.insert({"timestamp": splitted[0]+" "+splitted[1], "logdetail": splitted[2], "logservercityname": splitted[3], "loglevel": splitted[4]})

    c.close()


def getdata():
    global timeseries
    global countofmessage
    global oldentry
    global entry
    while True:
        time.sleep(0.2)
        if oldentry < len(entry):
            oldentry = len(entry)
            timeseries = []
            countofmessage = []

            for i in range(len(entry)):
                times = entry[i][0][0].split(" ")[1]
                timeseries.append(times)

            if len(entry) % time_interval == 0:
                rest = 0
                next = 0
            else:
                rest = len(entry) % time_interval
                next = 1

            last = int(len(entry) / time_interval) + next
            for i in range(last):
                countofmessage.append([0, 0, 0, 0, 0])
                a = i * time_interval
                if i == last - 1:
                    plus = rest
                else:
                    plus = time_interval

                for k in range(a, a + plus):
                    if entry[k][2][0] == "Moskow":
                        countofmessage[i][0] += 1
                    if entry[k][2][0] == "Istanbul":
                        countofmessage[i][1] += 1
                    if entry[k][2][0] == "Tokyo":
                        countofmessage[i][2] += 1
                    if entry[k][2][0] == "Beijing":
                        countofmessage[i][3] += 1
                    if entry[k][2][0] == "London":
                        countofmessage[i][4] += 1


@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n) :
    data = {
        'moskow_x': [],
        'moskow_y': [],

        'istanbul_x': [],
        'istanbul_y': [],

        'tokyo_x': [],
        'tokyo_y': [],

        'beijing_x': [],
        'beijing_y': [],

        'london_x': [],
        'london_y': [],

    }

    end = int(len(entry) / time_interval) + next + 2
    mod = len(entry) % time_interval
    for i in range(0, end):
        if i == 0:
            time_interval_i = 0
        elif i == end - 1:
            time_interval_i = (i * time_interval) - (time_interval - mod) - 1
        else:
            time_interval_i = (i * time_interval)

        data['moskow_x'].append(timeseries[time_interval_i])
        data['istanbul_x'].append(timeseries[time_interval_i])
        data['tokyo_x'].append(timeseries[time_interval_i])
        data['beijing_x'].append(timeseries[time_interval_i])
        data['london_x'].append(timeseries[time_interval_i])

    for i in range(len(countofmessage)):
        data['moskow_y'].append(countofmessage[i][0])
        data['istanbul_y'].append(countofmessage[i][1])
        data['tokyo_y'].append(countofmessage[i][2])
        data['beijing_y'].append(countofmessage[i][3])
        data['london_y'].append(countofmessage[i][4])

    fig = plotly.tools.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
    fig['layout']['margin'] = {
        'l': 30, 'r': 10, 'b': 30, 't': 10
    }
    fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

    fig.append_trace({
        'x': data['moskow_x'],
        'y': data['moskow_y'],
        'name': 'Moskow',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 1, 1)
    fig.append_trace({
        'x': data['istanbul_x'],
        'y': data['istanbul_y'],
        'name': 'Istanbul',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 1, 1)
    fig.append_trace({
        'x': data['tokyo_x'],
        'y': data['tokyo_y'],
        'name': 'Tokyo',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 1, 1)
    fig.append_trace({
        'x': data['beijing_x'],
        'y': data['beijing_y'],
        'name': 'Beijing',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 1, 1)
    fig.append_trace({
        'x': data['london_x'],
        'y': data['london_y'],
        'name': 'London',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 1, 1)

    return fig


def startserver():
    app.run_server(host='0.0.0.0')


if __name__ == "__main__":
    sv = threading.Thread(name='startserver', target=startserver)
    tb = threading.Thread(name='getdata', target=getdata)
    ta = threading.Thread(name='listen', target=listen)
    sv.start()
    tb.start()
    ta.start()













