import pyautogui
import time

f = open("tmp_ls.txt", "r")
ls = f.readlines()

f.close()
#print(ls)

"""
google textbox	Point(x=711, y=168)
Type
google search	Point(x=819, y=167)
1st Image	Point(x=48, y=403)
2nd Image Point(x=41, y=751)
3d Image Point(x=90, y=982)

Big Image 	Point(x=1581, y=260)

Save Image as 	Point(x=1637, y=495)

File name textbox  Point(x=1075, y=392)

Then type cat-breed
Enter

small google textbox Point(x=754, y=162)
small search Point(x=825, y=157)

main tab Point(x=78, y=55)


Repeat
"""

for breed in ls:
    if breed == "Burmese":
        continue
    pyautogui.click(78,55)
    time.sleep(2.5)
    pyautogui.moveTo(754,162)
    pyautogui.tripleClick()
    pyautogui.typewrite("cute smol " + breed + " cat")
    pyautogui.click(825, 157)

    time.sleep(2.0)

    pyautogui.click(48, 403)
    
    time.sleep(3.0)
    
    pyautogui.rightClick(1581, 260)
    
    time.sleep(1.0)

    pyautogui.click(1637, 495)

    time.sleep(1.0)
    pyautogui.click(1075, 392)

    time.sleep(1.0)

    pyautogui.tripleClick(1075, 392)

    pyautogui.typewrite("cat-3-" + breed)
    pyautogui.hotkey("enter")

