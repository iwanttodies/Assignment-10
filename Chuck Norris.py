import requests

while True:
    respond=requests.get("https://api.chucknorris.io/jokes/random")
    joke=respond.json()
    print(joke["value"])
    a=input("Do you want another one?(y/n)")
    if a==("y"):
        continue
    if a==("n"):
        print("alright")
        break
    else:
        print("ok i assume that a yes")
        continue
    
