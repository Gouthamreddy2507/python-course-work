photos = [
    "beach.png",
    "mountain.jpg",
    "party1.jpg",
    "selfie.png",
    "birthday.png",
    "concert.jpg",
    "sunset.png",
    "trip1.jpg"
]
print("photo Gallery:")
for i in range(len(photos)):
    print(f"{i+1}. {photos[i]}")
selection = int(input("enter photos id:"))
for selection in photos:
    print(photos[selection])
