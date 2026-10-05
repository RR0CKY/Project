import time
import rotatescreen

# Screen ko access karne ke liye display initialize karna
screen = rotatescreen.get_primary_display()

# Screen ko alag-alag angle par rotate karne ka loop
# 0 = Normal, 90 = Right, 180 = Inverted, 270 = Left
angles = [90, 180, 270, 0]

print("Prank start ho raha hai... (Stop karne ke liye Terminal ko Ctrl+C karein)")

for _ in range(2):  # Screen ko 2 baar poora ghumayega
    for angle in angles:
        screen.rotate_to(angle)
        time.sleep(1)  # Har rotation ke beech 1 second ka gap

# Prank khatam hone par screen ko wapas normal (0 degree) par set karna
screen.rotate_to(0)
print("Screen wapas normal ho gayi!")