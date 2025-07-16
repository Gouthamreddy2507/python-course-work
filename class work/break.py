bullets=10
while bullets>0:
    if bullets==5:
        print("Dead")
        break
    print(f"{bullets} are left-You can shoot()")
    bullets-=1
else:
    print("Game over")