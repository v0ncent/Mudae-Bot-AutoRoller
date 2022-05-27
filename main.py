import time
import keyboard
import pyautogui


def roll(number_of_rolls):
    roll_counter = 0
    while roll_counter < number_of_rolls:
        roll_counter += 1
        time.sleep(1)
        keyboard.write("$mb")
        keyboard.press("enter")
        time.sleep(.5)
        pyautogui.click()
    else:
        print('process complete')


if __name__ == '__main__':
    print('how many times would you like to roll?')
    rolls = int(input())
    if rolls is not None:
        print('press f4 to roll')
        keyboard.wait("f4")
        roll(rolls)
