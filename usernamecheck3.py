import time
from random import randint
import requests
from bs4 import BeautifulSoup

# Takes one argument (a list) and returns a random entry from the list
def get_word(theList):
    word = theList[randint(0, len(words))]
    return word

library_url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
r = requests.get(library_url)
text = r.text
words = text.split()




x = 0
while x < 100:       # set number of usernames to pull here
    user = get_word(words)
    url = 'https://www.instagram.com/api/v1/users/web_profile_info'
    
    querystring = {"username": user}

    payload = ""
    headers = {
        "cookie": "csrftoken=LtAI7nLEUmwQBVHm8RgdCRMQ16intjoW",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "X-CSRFToken": "LtAI7nLEUmwQBVHm8RgdCRMQ16intjoW",
        "X-IG-App-ID": "936619743392459",
        "X-ASBD-ID": "198387",
        "X-IG-WWW-Claim": "hmac.AR33CwCq2HQ_1WEcNOsHCP82MAfJ7jz-X4ZkQjmNfLdqbUzl",
        "X-Requested-With": "XMLHttpRequest",
        "Connection": "keep-alive",
        "Referer": "https://www.instagram.com/" + user + "/",
        "Cookie": "ig_did=E2C6F01C-8175-4845-9611-9574639967CD; datr=zWjIY8mPJR69mBaMTfC6F76S; mid=Y8hozgALAAEyUIhNqdosLFkRLTFx; ig_nrcb=1; sessionid=6376909533^%^3AIWhRZ5RduYODIO^%^3A17^%^3AAYet3kgHa2BvYzxaA4fcAd9tKqSZboHbypHoCmtsGQ; fbm_124024574287414=base_domain=.instagram.com; ds_user_id=6376909533; csrftoken=LtAI7nLEUmwQBVHm8RgdCRMQ16intjoW; shbid=17686\0546376909533\0541710534230:01f7037d9071f48e142111baad19e05a3ca054a556af4c5e0efde499d34e11ead8cfb6b2; shbts=1678998230\0546376909533\0541710534230:01f7fc81e993932a2ac0a4d6a4e677c9068aedd91aa3b88254d9eca8b84002ad7811ed7f; dpr=1.5; rur=EAG\0546376909533\0541710536554:01f7fd79b5b4ade965d6e703e258bd68be7feffa2a6d8f1cf5afae407c8af58218f19913; fbsr_124024574287414=aNHwq4XR6GFzI_1H2yt9uR9jXh4tPCED_i5jfH58DnE.eyJ1c2VyX2lkIjoiMTAwMDEyODE4MDgwODUwIiwiY29kZSI6IkFRRHFpX19JTUtabW1QR1Q1WHZ2VDVkcXZGVkM3WFpCaFdramxjUkpjbmNHSnk3Nk4zM0tEbVhES0ZFLXEtRGRCXzk1SkhHeXB4RnY2YU12dU5QM3JFdndxOEpvdUtaWlY5VzYxNjNxaGYyZVJKTFYteEVtc0JnOXdIcENVc24wakdVQW95Y0RoWjdvSVZaUWVQN1pBc2cyUEJkeGNsN2VVNDZOejZKWnFnV0N4MklTUnNkdVdNb2E0cEc5UWlZSWpjV1Rna1NZNTV3Y2RCMXpTdlVKVWNZb1FQVUg0elp1TjE2dDJkb2dzR1RyWlo2djRwSUVPaXNhS1lHcndRcWpOM2ZaMFZoUzVhbWFOUTdOaUVpQ0paa3RfcGhiX19oLUV3M25pRUVGNjdjQmpDVlB5QUdRTHMtcWNsWEUtdWNxTm9YX3FSeFBVanN3dVBSRmVURlRDc2wzIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU4zTDlQbDUyemxubXVINHBlWkFjV1E5TTgwZkhKakhaQ0lCQ1BJSFpBQUNMMU93SFpBZlZSTHNvbU9QV1B6NkZuVkhaQUp1WkFRcVEyUWNFSFlEcThGOUI3S2RCemFya2dFdzJJQzFHa3g0TlpCUU52anVoeGFGcUdEZnpzbmtqdHZma2RXczBvWFZleFpCSHE5T0hoQmhMRmcyQ1VHQ3Vyc1pDWkE0ZEx1VmJDTmI0S2hGaU81RXpNQWtjUURTMHI5Z1pEWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY3OTAwMDUyM30; fbsr_124024574287414=kpmzGJ-Q-v_gq-uEbKBQPnet57oErQMu7GWNPC7TQoM.eyJ1c2VyX2lkIjoiMTAwMDEyODE4MDgwODUwIiwiY29kZSI6IkFRQk02YmxlczlNU1JPMVU0UG5wQl83RlJqSlVKTllXUTJfRkhHWlkza2ZiMnBvbWpMRGY4czZxMjgzUE5WRlFDY0JuRUdfZUZRbU5zRUdGUGVrNHQwUmpSWWg1TkdlejA2ZVRUZ3h0RHRpdW5yY3Y1QUNmdnJuN0pfS0FuSDZONFNwRWJ4RnZqT3NTTDdzN3dacm1BQndSdy1HdWhUQXFLZjFrVnBHcXBoeFNZYnFnd1FIeUFQeHA4Sm5GMVVQNER4ZF84VWhBZFpOcThsamhYVTBFaVFyYXVWZ0U2MXhZLUt4Y2wzNDVvOTJvNHlzdjlyNlpKdFo4aW4ybVUxZzE3QXFkaVNKaXY0ME9DNk41LVVBZTJMWmoyX2dsTm9RZjZZVnpvNHpGU09kYW9KaGoxRFZrck0zSHNUOE1NSWxZSkFHdVdPYXR0b2tPellyTzhYay0zdkE1Iiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU5TVG1yZDhSWkJ1RHJ0eUNoa0UwOGJsbmdmN1JZM25RU2FjaXl1c2hiZTFYMHdkQ1Bwc1Y0ZEdsNVQxWUV4VjJuUFRSZWRxUGNxblFaQ1Z3bUFXc0l6WE1lVEVUazU4WkFORGU2SUY2ZUVmc1NtZGRwaFpBTlFzZlpDQ2JGZTBDTXllQ05oQzNxWkNqYkNUZUpaQVA2dHI3RU9vS2hzQTFCUmduakV0aDdZVEJLS1A4d1NiYTVSYTVNUTVMOG8yZ1pEWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY3OTAwMDQ0OH0",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    
    # doc = BeautifulSoup(response.text, 'html.parser')  this isn't needed anymore since this server responds with a 404 not found
    if response.status_code == 404:
        print("User available: " + user)
    else:
        print("User taken: " + user)
    time.sleep(2.5)
    x += 1
