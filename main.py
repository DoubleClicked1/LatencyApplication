import PySimpleGUI as sg
from pythonping import ping

pingDestination = '8.8.8.8' #change Address of server here!
response_list = ping(pingDestination, size=40, count=10)
averagePing = str(response_list.rtt_avg_ms)
sg.theme("SystemDefault1") #You can also change the theme of the application. For a list of them search up 'PySimpleGUI themes'

layout = [[sg.Text("Your ping is: " + averagePing + "ms", key='-TEXT-')],
          [sg.Button("Refresh"), sg.Button("Exit")]]

window = sg.Window("Ping Displayer", layout, margins=(50, 25))

while True:
    event, values = window.read()
    if event == "Refresh":
        response_list = ping(pingDestination, size=40, count=10)
        averagePing = str(response_list.rtt_avg_ms)
        window['-TEXT-'].update("Your ping is: " + averagePing + "ms")
    if event == sg.WIN_CLOSED or event == "Exit":
        break

window.close()
