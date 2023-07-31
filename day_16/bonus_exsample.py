import PySimpleGUI

label = PySimpleGUI.Text("Select files to compress: ")
label1 = PySimpleGUI.Text("Select destination folder: ")
input_box = PySimpleGUI.InputText(tooltip="Enter todo")
input_box1 = PySimpleGUI.InputText(tooltip="Enter todo")
add_button = PySimpleGUI.FilesBrowse("Choose")
add_button1 = PySimpleGUI.FilesBrowse("Choose")

add_button2 = PySimpleGUI.Button("Compress")


window = PySimpleGUI.Window("My To-do", layout=[[label, input_box, add_button], [label1, input_box1, add_button1],
                                                [add_button2]])

window.read()
window.close()
