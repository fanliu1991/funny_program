#! python3
'''
PyAutoGUI can simulate moving the mouse, clicking the mouse, dragging with the mouse, pressing keys, pressing and holding keys, and pressing keyboard hotkey combinations.
'''
# import sys, optparse, os
import pyautogui
import time

TOTAL_PAGES = 10

# sleep 5 seconds to allow user open desired pages
time.sleep(5)

try:
    # Given read-only pages, automatically screen shot current page, and then jump to next page to take screen shot
    '''
    for i in range(TOTAL_PAGES):
        pyautogui.screenshot("page_%d.pdf" %i)
        pyautogui.press("right")
        # sleep 1 second to turn to next page
        time.sleep(1)
    '''

    # Keep tracking mouse position
    mouse_pos = pyautogui.position()
    print("at begining:", mouse_pos)
    while True:
        new_mouse_pos = pyautogui.position()
        if (new_mouse_pos != mouse_pos):
            print(new_mouse_pos)
            mouse_pos = new_mouse_pos
            time.sleep(1)
except KeyboardInterrupt:
    print("Quit by user!")
else:
    print("No error deducted.")
finally:
    print("Done.")

