#!/usr/bin/python

import requests
import json
import sys

if (len(sys.argv)==3):

        print ("username = "+sys.argv[1]+", password = "+sys.argv[2])
        username = sys.argv[1]
        password = sys.argv[2]

        print ("Connecting...")
        try:
            response = requests.post(
                "https://my.vanmoof.com/api/v8/authenticate",
                headers = {
                    'Api-Key': 'fcb38d47-f14b-30cf-843b-26283f6a5819',
                },
                auth=(username,password)
            )
            print("Login successful!")
            #print(response.json())
            print(json.dumps(response.json(), indent=4))
            access_token = response.json()['token']
        except requests.exceptions.RequestException as error:
            print("Login failed:")
            print(error)


        try:
            vanmoof = requests.get(
                "https://my.vanmoof.com/api/v8/getCustomerData/?includeBikeDetails",
                headers= {
                    'Api-Key': 'fcb38d47-f14b-30cf-843b-26283f6a5819',
                    'Authorization': 'Bearer '+access_token
                }
            )
            print("\nResult:")
            print(vanmoof)
            vanmoofjson = json.dumps(vanmoof.json(), indent=4)
            print("\nResult JSON:")
            print(vanmoofjson)

        except requests.exceptions.RequestException as error:
            print("Get vanmoof details faild failed:")
            print(error)
else:
        print ("Usage: "+sys.argv[0]+" <username> <password>")

