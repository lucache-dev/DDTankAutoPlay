import pyautogui, time

class AutoPlay:
    def __init__(self):
        return

    def match_started(self):
        timer = time.time()
        is_your_turn = False
        while not is_your_turn and time.time() - timer < 180:
            your_turn_img = pyautogui.locateOnScreen('assets/images/your_turn.png', confidence=0.5)
            pass_img = pyautogui.locateOnScreen('assets/images/pass.png', confidence=0.5)
            is_your_turn = your_turn_img != None or pass_img != None
            if is_your_turn:
                print('NOW IS YOUR TURN')
                time.sleep(1)
                pyautogui.write('124', interval=0.20)
                pyautogui.keyDown('up')
                time.sleep(1.0)
                pyautogui.keyUp('up')
                pyautogui.keyDown('space')
                pyautogui.keyUp('space')
                is_your_turn = False

            elif self.check_if_match_is_finish():
                break

        return

    def check_if_match_is_finish(self):
        end_game_img = pyautogui.locateOnScreen('assets\images\end_game.png', confidence=0.5)
        lobby_img = pyautogui.locateOnScreen('assets/images/start_queue.png', confidence=0.5)

        return end_game_img != None or lobby_img != None

    def start_queue(self):
        while True:
            ready_button = pyautogui.locateOnScreen('assets/images/start_queue.png', confidence=0.5)
            if ready_button != None:
                pyautogui.leftClick(ready_button)
                searching_game = pyautogui.locateOnScreen('assets\images\searching_solo_game.png', confidence=0.5)
                searching_gvg = pyautogui.locateOnScreen('assets\images\searching_gvg.png', confidence=0.5)
                if searching_game or searching_gvg != None:
                    time.sleep(2)
                    searching_game = pyautogui.locateOnScreen('assets\images\searching_solo_game.png', confidence=0.5)
                    searching_gvg = pyautogui.locateOnScreen('assets\images\searching_gvg.png', confidence=0.5)
                    if searching_game or searching_gvg != None:
                        print('Queue Started')
                        break
        return

    def set_ready(self):
        while True:
            ready_button = pyautogui.locateOnScreen('assets/images/ready_queue.png', confidence=0.7)
            if ready_button != None:
                pyautogui.leftClick(ready_button)
                time.sleep(2)
                searching_gvg = pyautogui.locateOnScreen('assets\images\searching_gvg.png', confidence=0.5)
                if searching_gvg != None:
                    print('Queue Started')
                    break
        return

    def wait_load(self):
        match_is_started = False
        while not match_is_started: 
            image_coordinates = pyautogui.locateOnScreen('assets\images\loading_screen.png', confidence=0.5)
            match_is_started = image_coordinates != None
            if match_is_started:
                print('Match Starting')
        return

    def start(self, gama_mode, role):
        is_queue = True
        is_loading = False
        is_on_match = False
        while True:
            if is_queue:
                if gama_mode== 'gvg' and role == 'guest':
                    self.set_ready()
                else:
                    self.start_queue()
                is_queue = False
                is_loading = True
                is_on_match = False
            elif is_loading:
                self.wait_load()
                is_queue = False
                is_loading = False
                is_on_match = True
            elif is_on_match:
                self.match_started()
                is_queue = True
                is_loading = False
                is_on_match = False