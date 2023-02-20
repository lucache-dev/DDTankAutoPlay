import pyautogui, time, keyboard

class AutoClick:
    def __init__(self):
       return

    def start():
        time.sleep(2)
        while True:
            pyautogui.click(clicks=1, interval=0.05)
            if keyboard.is_pressed('s'):
                break
        print('break')
        return
        