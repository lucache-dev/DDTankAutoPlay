import PySimpleGUI as sg
from auto_play import AutoPlay
from auto_click import AutoClick

def start(is_gvg, is_guest):
    game_mode = 'gvg' if is_gvg else 'solo'
    role = 'guest' if is_guest else 'owner'
    window.minimize()
    AutoPlay().start(game_mode, role)


def start_auto_click():
    AutoClick.start()
    window.minimize()
    return

try:
    sg.theme('DarkGrey10')

    left_column = [
        [sg.Text('Play mode: ', font=('Roboto', 16), text_color='#ffffff' )],
        [sg.Radio('Solo', "RADIO1", font=('Roboto', 12), text_color='#ddded7', default=True, key="is_solo")],
        [sg.Radio('GvG', "RADIO1", font=('Roboto', 12), text_color='#ddded7', default=False, key="is_gvg")],
        [sg.Text("", size=(1, 3))],
        [sg.Text("You're: ", font=('Roboto', 16), text_color='#ffffff' )],
        [sg.Radio("Room's owner", "RADIO2", font=('Roboto', 12), text_color='#ddded7', default=True, key="is_owner")],
        [sg.Radio("Guest", "RADIO2", font=('Roboto', 12), text_color='#ddded7', default=False, key="is_guest")],
        [sg.Text("", size=(1, 3))],
        [sg.Button('Auto Click mode', font=('Roboto', 10), size=(15,1), key='auto_click_mode', tooltip="Active auto click to upgrade your cards")]
    ]

    right_first_line = [sg.Image(filename='assets/client_img.png')]
    right_margin_line = [sg.Text("", size=(1, 3))]
    right_second_line = [sg.Button('Start', font=('Roboto', 15), size=(14, 3), key='start_button')]


    right_column = [right_first_line, right_margin_line, right_second_line]

    layout = [
        [sg.Column(left_column, size=(300, 400)),
        sg.Column(right_column, size=(300, 400), justification='center', element_justification='center')]
    ]

    window = sg.Window('DDtank Auto Play', layout, icon=('assets/icon.ico'))
    
    while True:             
        event, values = window.read()
        if event == 'start_button':
            start(values['is_gvg'], values['is_guest'])
        if event == 'auto_click_mode':
            start_auto_click()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        
    window.close()

except KeyboardInterrupt:
    window.close()
    print('<================================== !!! Interrupting exacution !!! ==================================>')