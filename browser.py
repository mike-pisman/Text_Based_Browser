# Mikhail Pisman
# https://github.com/mike-pisman/Text_Based_Browser
# Text-Based Browser
# browser.py
# Main file with class and main function

import re
import sys
import os
import shutil
import requests
from bs4 import BeautifulSoup
from collections import deque
from colorama import init, Fore


# Browser class
class Browser:
    # Init
    def __init__(self, file=None):
        self.save_dir = self.make_download_dir(file)  # Create directory for downloaded files
        self.history = deque()  # Create stack for history of visited sites
        self.current_page = None

    # Function takes, name of folder as a parameter and creates folder in root directory for downloaded files
    def make_download_dir(self, file):
        if file is None:  # If no folder was passed in CLI arguments
            file = "tmp"  # Create folder named "tmp"(default folder)
        if not os.path.exists(file):  # Check that folder doesn't exist
            os.mkdir(file)  # If there is no such folder, create new one
        return file  # Return name of the folder

    # Function takes url-string as parameter and prints out the page if it was downloaded, otherwise downloads the page
    def load_page(self, url):
        path = re.sub(r'(http(s)?://)', '', url)  # Remove http:// or https:// from url string
        path = self.save_dir + '/' + path + '.txt'  # add .txt and folder name
        if os.path.exists(path):  # Check if such page was downloaded
            if self.current_page:  # If the browser already displaying a page
                self.history.append(self.current_page)  # add that page to the browser history
            with open(path, 'r') as f:  # open the page file
                print(f.read())  # print the content
                self.current_page = url  # Set the current page for history purpose
        else:
            self.download_page(url)  # If such page doesn't exist, download it

    # Function takes url string as a parameter, and downloads the page with that url
    def download_page(self, url):
        if check_url(url):  # Check that url is in correct form
            if not url.startswith('http'):  # if url doesn't have http:// in the beginning
                url = "https://" + url  # add https://
            r = requests.get(url)  # Create GET request with url
            if r:  # If the request was successful
                content = parse_page(r.content)  # Parse HTML page, to extract all text
            else:
                print("Error")  # In case of unsuccessful request
                return

            file_name = url[:url.rfind('.')]  # Strip the top-level domain (.com, .net, etc.)
            file_name = re.sub(r'(http(s)?://)', '', file_name)  # remove http:// or https://
            with open(self.save_dir + '/' + file_name + '.txt', 'w') as file:  # Create or rewrite file
                file.write(content)  # Add parsed text

            self.load_page(file_name)  # Load downloaded page
        else:
            print("Error: Incorrect URL")  # If the url was in incorrect form

    # Function loads previous page
    def previous(self):
        if self.history:  # If any pages were visited already
            file_name = self.history.pop()  # Remove last visited page
            self.current_page = None  # Set current page to none to avoid recursion in history
            self.load_page(file_name)  # Load previous page

    # Function stops execution of the program
    def exit(self):
        if self.save_dir == "tmp":  # If the browser used default directory
            try:
                shutil.rmtree(self.save_dir)  # Delete it
            except OSError as e:  # In case of any error
                print("Error: %s - %s." % (e.filename, e.strerror))  # Print out the error

# Function takes string with HTML downloaded page and parses it, returning string with colored text
def parse_page(content):
    # Only include text in between tags:
    include_tags = ['title', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']

    soup = BeautifulSoup(content, 'html.parser')  # Parse HTML using beautiful soup
    texts = soup.findAll(text=True)  # Find all tags with text
    visible_texts = []  # List for resulted parsed text
    for i in texts:  # For each tag
        if i.parent.name in include_tags:  # If it's in included tags
            if i.parent.name == 'a':  # If it's a link add colormap blue color
                i = Fore.BLUE + i  # To print links in blue
            else:
                i = Fore.WHITE + i  # To print other text in white
            visible_texts.append(i)  # Add string to the result list
    return "\n".join(t.strip() for t in visible_texts)  # Join list into one string, separated by new line


# Function check url string in parameter for correctness
def check_url(url):
    # If the string matches the pattern return True, otherwise False
    return re.match(r'^(http(s)?://.)?(www\.)?[-a-zA-Z0-9@:%._+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_+.~#?&/=]*)$', url.lower())


# Main function the takes input from user and interprets commands
def main():
    # Create an instance of browser with CLI argument or without
    browser = Browser() if len(sys.argv) == 1 else Browser(sys.argv[1])

    # Get commands
    while True:
        print(Fore.RED + 'Text-Based Browser by Mikhail Pisman')
        print(Fore.GREEN + "\t- Please, enter: url of the page you would like to visit")
        print('\t- "back" to print previously visited page')
        print('\t- "exit" to exit the program')
        command = input(Fore.WHITE + '> ').strip()
        # Stop applications
        if command == 'exit':
            browser.exit()
            break
        # Show previous page
        elif command == 'back':
            browser.previous()
        # Load page from the CLI
        else:
            browser.load_page(command)


if __name__ == '__main__':
    main()
