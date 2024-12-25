import json
while True:
    command=input("command: ")
    if command=="q":
        break
    elif command=="+":
        with open("bank.json", "r") as file:
            name_lastname=input("name, lastname: ")
            t=json.load(file)
            sum_=int(input("sum: "))
            if t.get(name_lastname)==None:
                t[name_lastname] = sum_
            else:
                t[name_lastname] += sum_

            with open("bank.json","w")as file2:
                json.dump(t,file2)

    elif command=="-":
        with open("bank.json", "r") as file:
            name_lastname=input("name, lastname: ")
            t=json.load(file)
            sum_=int(input("sum: "))
            if t.get(name_lastname)==None:
                t[name_lastname] = -sum_
            else:
                t[name_lastname] -= sum_

            with open("bank.json","w")as file2:
                json.dump(t,file2)
    elif command == "r":
        with open("bank.json", "r") as file:
            name_lastname = input("name, lastname: ")
            t = json.load(file)
            print(t.get(name_lastname))