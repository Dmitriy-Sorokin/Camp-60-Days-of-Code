import PySimpleGUI as sg
from converters import convert

feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter inches: ")
inches_input = sg.Input(key="inches")

button = sg.Button("Convert")
output_label = sg.Text("", key="out")

window = sg.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button, output_label]])

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])
    meters = feet * 0.3048 + inches * 0.0254
    # result = convert(feet, inches)
    window["out"].update(value=f"{meters} m")


window.close()