# Cross Platform GUI development with PySimpleGUI
# cerner_2tothe5th_2021
# Simple example of using PySimpleGUI to create cross platform GUIs. 
# Install PySimpleGUI using "pip3 install pysimplegui"

import PySimpleGUI as sg

def main():
    layout = [
        [
            [sg.Text("Hello, it's day 4. Let's build a cross platform GUI .", font='20')],
            [sg.Button('Click Me', key='CLICKME', font=20), sg.Button('Exit', font=20)],
            [sg.Output(font=20)]
        ]
    ]
    window = sg.Window("Window", layout)

    while True:
        event, values = window.read()
        if event is None or event == 'Exit':
            return
        if event == 'CLICKME':
            print("Yay, you clicked the button. Think of the possibilities. ")
main()