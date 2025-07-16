grocery = {
    1:{"product": "Rice", "Price": 60},
    2:{"product": "Wheat Flour", "Price": 45},
    3:{"product": "Sugar", "Price": 40},
    4:{"product": "Milk", "Price": 25},
    5:{"product": "Eggs (12 pcs)", "Price": 70},
    6:{"product": "Cooking oil", "Price": 130},
    7:{"product": "Tea Powder", "Price": 90},
    8:{"product": "Salt", "Price": 20},
    9:{"product": "Bread", "Price": 30},
    10:{"product": "Soap", "Price": 25},
}

for i in grocery.keys():
    print(f"{i}. {grocery[i]["product"]} {grocery[i]["Price"]}")
items=list(map(int,input("Enter the item indexes: ").split()))

total = 0
ids=set()
for i in items:
    if i not in ids:
        co=items.count(i)
        total+=(grocery[i]["Price"]*co)
        print(f"{grocery[i]["product"]}-{co}*{grocery[i]["Price"]} = {grocery[i]["Price"]}*{co}")
       

print("total bill: ", total)


