#code by @rxxv
import os
from bs4 import BeautifulSoup
from requests import request
from time import sleep
from threading import active_count, Thread
import re

TOKEN_FILE = "token.txt"
EMAIL_FILE = "email.txt"

ASCII_ART = """
                              *                   
  *   )                     (  `              (   
` )  /(   (     )           )\))(      )  (   )\  
 ( )(_)) ))\   (     `  )  ((_)()\  ( /(  )\ ((_) 
(_(_()) /((_)  )\  ' /(/(  (_()((_) )(_))((_) _   
|_   _|(_))  _((_)) ((_)_\ |  \/  |((_)_  (_)| |  
  | |  / -_)| 'by@rxxv' | \| |\/| |/ _` | | || |  
  |_|  \___||_|_|_| | .__/ |_|  |_|\__,_| |_||_|  
                    |_|                           
"""

class Email:
    def __init__(self):
        self.token = self.load_token()
        self.email = self.load_email()

    def get_email(self) -> str:
        while True:
            try:
                url = "https://api.tempmail.lol/generate"
                response = request("GET", url, timeout=10)
                self.token = response.json()["token"]
                self.email = response.json()["address"]
                self.save_token(self.token)  # Save the token to a file
                self.save_email(self.email)  # Save the email address to a file
                return self.email
            except Exception as e:
                print(f"Error in get_email: {e}")
                sleep(5)

    def get_messages(self) -> list:
        while True:
            try:
                url = f"https://api.tempmail.lol/auth/{self.token}"
                response = request("GET", url, timeout=10)
                messages = response.json()["email"]
                if messages:
                    return messages
                else:
                    print("Waiting for message...")
                    sleep(5)
            except Exception as e:
                print(f"Error in get_messages: {e}")
                sleep(5)

    def save_token(self, token: str):
        with open(TOKEN_FILE, "w") as file:
            file.write(token)

    def load_token(self) -> str:
        if os.path.exists(TOKEN_FILE):
            with open(TOKEN_FILE, "r") as file:
                token = file.read().strip()
                if not token:
                    print("Token not found. Please generate a new email.")
                    return ""  # Return an empty string if the token is not found
                return token
        return ""

    def save_email(self, email: str):
        with open(EMAIL_FILE, "w") as file:
            file.write(email)

    def load_email(self) -> str:
        if os.path.exists(EMAIL_FILE):
            with open(EMAIL_FILE, "r") as file:
                return file.read().strip()
        return ""

def extract_code_from_html(html_content: str) -> str:
    soup = BeautifulSoup(html_content, 'html.parser')
    code = soup.find(text=re.compile(r'\d{6,}'))
    return code if code else "Code not found"

def choose_email() -> bool:
    choice = input("Do you want to use a new email or the current email? (new/current): ").strip().lower()
    return choice == "new"

def Generate():
    print(ASCII_ART)  # Print the ASCII art before starting
    try:
        EmailClient = Email()
        if not EmailClient.token:  # If the token is not found or is empty
            if choose_email():
                Address = EmailClient.get_email()
                print(f"Generated email address: {Address}")  # Print the generated email address
            else:
                print("Token not found please generate new email. Exiting.")
                return

        else:
            Address = EmailClient.email
            print(f"Using current email address: {Address}")

        # Wait for messages and print the verification code
        Messages = EmailClient.get_messages()
        for message in Messages:
            html_content = message.get('html', '')
            code = extract_code_from_html(html_content)
            if code != "Code not found":
                print(f"Verification code: {code}")
                break  # Exit after finding the code
            else:
                print("Code not found in the message.")

    except Exception as e:
        print(f"Error in Generate: {e}")

while True:
    if active_count() <= 1:
        Thread(target=Generate).start()
