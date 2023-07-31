import PySimpleGUI

label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter todo", key="todo")
add_button = PySimpleGUI.Button("Add")

window = PySimpleGUI.Window("My To-do", layout=[[label], [input_box, add_button]], font=('Helvetica', 20))
event = window.read()
print(event)
window.close()
