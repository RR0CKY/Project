import pyautogui
import random
import time

print("Ghost Mouse Prank started! Stop karne ke liye mouse ko ekdum screen ke corner mein le jayein.")

# Computer screensize get karna
screen_width, screen_height = pyautogui.size()

# 10 baar mouse move karega (Isse control mein rahega)
for _ in range(10):
    # Screen ke andar random X aur Y coordinates chunna
    x = random.randint(100, screen_width - 100)
    y = random.randint(100, screen_height - 100)
    
    # Mouse ko Smoothly new location par le jana
    pyautogui.moveTo(x, y, duration=0.5)
    time.sleep(2)  # 2 second ka gap

print("Prank Over!")