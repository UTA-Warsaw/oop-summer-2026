my_data = {
    "name":"Yevhen",
    "suename":"Protasov",
    "age": 18,
    "names": ["Solomia"]
}

def greeting(name):
    print(f"Hello my name is {name}")
greeting("Yevhen")

def isadult(user):
    if user["age"] >= 18:
        return True

print(isadult(my_data))
