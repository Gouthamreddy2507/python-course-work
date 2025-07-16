data = {
    1:{"name":"Goutham","exam_status":True, "python":100,"sql":95,"html":95},
    2:{"name":"Ruthik","exam_status":True, "python":75,"sql":79,"html":80},
    3:{"name":"Shiva","exam_status":True, "python":35,"sql":50,"html":60},
    4:{"name": "Sai","exam_status":True, "python":85,"sql":90,"html":90},
}
for i in data.keys():
    print(f'{i}.{data[i]["name"]}')
stuid = int(input("enter the student id: "))

if stuid in data:
    if data[stuid]["exam_status"]:
        total=(data[stuid]["python"]+data[stuid]["sql"]+data[stuid]["html"])/3
        if total>90:
            print(f'Congrats!!!\n{data[stuid]["name"]} got "A" grade')
        elif total>75:
            print(f'Good!!!\n{data[stuid]["name"]} got "B" grade')
        elif total>50:
            print(f'Need improvement!!!\n{data[stuid]["name"]} got "C" grade')
        elif total>35:
            print(f'Just passed!!!\n{data[stuid]["name"]} got "D" grade')
        else:
            print(f'{data[stuid]["name"]}-Fail, Better luck next time!!!')
    else:
        print(f'{data[stuid]['name']} is not attempted the exam ')
else:
    print(f"The id is not present. Try Again")

