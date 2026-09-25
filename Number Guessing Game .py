import random

# Computer 1 se 20 tak koi bhi number chunega
secret_number = random.randint(1, 20)
attempts = 0

print("--- Number Guessing Game ---")
print("Maine 1 se 20 ke beech ek number socha hai. Guess karein!")

while True:
    guess = int(input("Aapka guess kya hai? "))
    attempts += 1  # Har baar attempt count badhega

    if guess < secret_number:
        print("Bahut chota hai! Thoda bada number try karein.")
    elif guess > secret_number:
        print("Bahut bada hai! Thoda chota number try karein.")
    else:
        print(f"Waah! Bilkul sahi jawab. Aapne {attempts} baar mein guess kiya! 🎉")
        break  # Game khatam
