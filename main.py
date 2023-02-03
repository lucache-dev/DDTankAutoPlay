import pyautogui, time


def match_started():
    is_your_turn = False
    print('is not your turn')
    while not is_your_turn:
        your_turn_img = pyautogui.locateOnScreen('your_turn.png', confidence=0.5)
        is_your_turn = your_turn_img != None
        if is_your_turn:
            print('NOW IS YOUR TURN')
            time.sleep(1)
            pyautogui.write('124', interval=0.50)
            keyDown('space')
            time.sleep(0.5)
            keyUp('space')
            return

# image_coordinates = pyautogui.locateOnScreen('image.png', confidence=0.5)
# if image_coordinates:
#     pyautogui.leftClick(image_coordinates)

try:
    match_is_started = False
    while not match_is_started: 
        image_coordinates = pyautogui.locateOnScreen('image.png', confidence=0.5)
        match_is_started = image_coordinates != None
        if match_is_started:
            print('match started')
            match_started()
except KeyboardInterrupt:
    print('interrupted')