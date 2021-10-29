import winsound
from time import sleep
from PlaySound import AudioFile
from Parser import Parser

game_found_keywords = ['preparing the game', 'loading loot', 'creating loot pools', 'synchronizing', 'waiting for players']
matching_started = False
# dual_screen_region = (880, 1145, 774, 38)
dual_screen_region = (880, 1130, 774, 75)

print("Starting script...", flush=True)
sleep(1)

# Loop 
while True:
    sleep(0.5)
    if(not matching_started):
        if(Parser(region=dual_screen_region, keywords=['matching'])):
            winsound.Beep(988, 120) ; winsound.Beep(784, 120) ; winsound.Beep(988, 120) ; winsound.Beep(784, 120)
            print('Matching detected, searching for game_found_keywords...', flush=True)
            matching_started = True
    # look for game found keywords instead of matching
    elif(Parser(region=dual_screen_region, keywords=game_found_keywords)):
        winsound.Beep(988, 120) ; winsound.Beep(988, 120) ; winsound.Beep(988, 120) ; winsound.Beep(988, 120)
        print('Match has been found!', flush=True)
        break

# play wav alert sound
a = AudioFile('super_silso_whoaa.wav')
a.play()
a.close()

print("\nScript ended.")

#  # Extra references
# pyautogui.press('space')
# pyautogui.write('hello world!', 0.25)
# screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
# currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
