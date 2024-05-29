import pyautogui
import webbrowser
import time

webbrowser.open("https://hrms.accessassist.in/")
time.sleep(2)

image_path = "Screenshot 2024-05-29 225016.png"

while True:
    try:
        location = pyautogui.locateOnScreen(image_path)
        if location:
            center = pyautogui.center(location)
            pyautogui.click(center)
            print("Image found and clicked!")
            pyautogui.press('ctrl', 'w')
            break
        else:
            print("Image not found, retrying...")
            time.sleep(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        break
