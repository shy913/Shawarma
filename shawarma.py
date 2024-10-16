import time

import cv2
import numpy as np
import pyautogui



while True:


    # 截屏并转换为灰度图像
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)


    # --开始一天
    # 加载目标图像
    template = cv2.imread('kaishiyitian.png')
    w, h = template.shape[1], template.shape[0]
    # 使用模板匹配
    result = cv2.matchTemplate(gray_screenshot, cv2.cvtColor(template, cv2.COLOR_BGR2GRAY), cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= 0.95)  # 设定阈值
    for pt in zip(*loc[::-1]):
        # 点击目标位置
        pyautogui.mouseDown(pt[0] + w // 2, pt[1] + h // 2)
        pyautogui.sleep(0.1)  # 持续按下.1s
        pyautogui.mouseUp()
        break  # 点击一次后退出




    # check_empty
    flag = 0
    # 截屏并转换为灰度图像
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # potato mach
    template = cv2.imread('empty_potato_mach.png')
    # 使用模板匹配
    result = cv2.matchTemplate(gray_screenshot, cv2.cvtColor(template, cv2.COLOR_BGR2GRAY), cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= 0.9)  # 设定阈值
    if len(loc[0]) > 0:
        flag = 1
        print('empty potato mach!')
        pyautogui.moveTo(2292,966)
        pyautogui.mouseDown()
        time.sleep(5)
        pyautogui.mouseUp()

    # potato
    template = cv2.imread('empty_potato.png')
    # 使用模板匹配
    result = cv2.matchTemplate(gray_screenshot, cv2.cvtColor(template, cv2.COLOR_BGR2GRAY), cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= 0.9)  # 设定阈值
    if len(loc[0]) > 0:
        flag = 1
        print('empty potato!')
        pyautogui.moveTo(2060,906)
        pyautogui.mouseDown()
        pyautogui.mouseUp()

    # meat
    template = cv2.imread('empty_meat.png')
    # 使用模板匹配
    result = cv2.matchTemplate(gray_screenshot, cv2.cvtColor(template, cv2.COLOR_BGR2GRAY), cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= 0.9)  # 设定阈值
    if len(loc[0]) > 0:
        flag = 1
        print('empty meat!')
        pyautogui.mouseDown(513,1062)

        for _ in range(5):
            pyautogui.moveTo(633,900,duration=0.3)
            pyautogui.moveTo(633, 500)
        pyautogui.mouseUp()

    # cucumber
    template = cv2.imread('empty_cucumber.png')
    # 使用模板匹配
    result = cv2.matchTemplate(gray_screenshot, cv2.cvtColor(template, cv2.COLOR_BGR2GRAY), cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= 0.9)  # 设定阈值
    if len(loc[0]) > 0:
        flag = 1
        time.sleep(0.3)
        print('empty cucumber!')
        pyautogui.moveTo(362, 800)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        time.sleep(0.3)
        for _ in range(10):
            pyautogui.mouseDown(585,753)
            pyautogui.mouseUp()
        pyautogui.moveTo(362, 800)
        pyautogui.mouseDown()
        pyautogui.mouseUp()

        # yogurt
        template = cv2.imread('empty_yogurt.png')
        # 使用模板匹配
        result = cv2.matchTemplate(gray_screenshot, cv2.cvtColor(template, cv2.COLOR_BGR2GRAY), cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= 0.9)  # 设定阈值
        if len(loc[0]) > 0:
            flag = 1
            print('empty yogurt!')
            time.sleep(0.3)
            pyautogui.moveTo(362, 800)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            time.sleep(0.3)
            for _ in range(10):
                pyautogui.mouseDown(575, 872)
                pyautogui.mouseUp()
            pyautogui.moveTo(362, 800)
            pyautogui.mouseDown()
            pyautogui.mouseUp()

    if flag == 0:
        # shawarma start !!
        # 截屏并转换为灰度图像
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

        # 点击卷饼
        template = cv2.imread('empty_table.png')
        w, h = template.shape[1], template.shape[0]
        # 使用模板匹配
        result = cv2.matchTemplate(gray_screenshot, cv2.cvtColor(template, cv2.COLOR_BGR2GRAY), cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= 0.9)  # 设定阈值
        for pt in zip(*loc[::-1]):
            # 点击目标位置
            pyautogui.mouseDown(pt[0] + w // 6, pt[1] + h // 2)
            pyautogui.mouseUp()
            time.sleep(0.5)
            pyautogui.moveTo(684,1007)
            for _ in range(3):
                pyautogui.mouseDown()
                pyautogui.mouseUp()
            pyautogui.moveTo(900, 1014)
            for _ in range(3):
                pyautogui.mouseDown()
                pyautogui.mouseUp()
            pyautogui.moveTo(1100, 1000)
            for _ in range(3):
                pyautogui.mouseDown()
                pyautogui.mouseUp()
            pyautogui.moveTo(1298, 1000)
            for _ in range(3):
                pyautogui.mouseDown()
                pyautogui.mouseUp()

            # check
            screenshot = pyautogui.screenshot()
            screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
            template = cv2.imread('full_shawarma.png')
            # 使用模板匹配
            result = cv2.matchTemplate(gray_screenshot, cv2.cvtColor(template, cv2.COLOR_BGR2GRAY),
                                       cv2.TM_CCOEFF_NORMED)
            loc = np.where(result >= 0.9)  # 设定阈值
            if len(loc[0]) == 0:
                break


            # juan
            pyautogui.moveTo(1271,1251)
            pyautogui.mouseDown()
            pyautogui.moveTo(1281, 1095,duration=0.5)
            pyautogui.mouseUp()
            # baozhuang
            time.sleep(0.3)
            pyautogui.moveTo(1058,1178)
            pyautogui.mouseDown()
            pyautogui.moveTo(1500, 1182,duration=0.5)
            pyautogui.mouseUp()
            break  # 点击一次后退出