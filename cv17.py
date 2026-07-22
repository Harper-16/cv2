#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 17:11:42 2026

@author: dhruv
"""

import requests

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Full json response: {response.json()}")
        
        joke_data = response.json()
        return f"{joke_data['setup']} - joke{joke_data['punchline']}"
    else:
        return "Failed to get a hilarious joke for my master :("

def main():
    print("welcome to the joke - mania ")
    while True:
        user_input = input("Press enter to get a new joke or type 'q' or 'exit' to exit: HAVE FUN").strip().lower()
        if user_input in ("q","exit"):
            print("Goodbye")
            break
        joke = get_random_joke()
        print(joke)

if __name__ == "__main__":
    main()
            
        
    