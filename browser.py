import re
import sys
import os
import shutil
import requests
from bs4 import BeautifulSoup
from collections import deque
from colorama import init, Fore

class Browser:
    def __init__(self, file=None):
        self.save_dir = self.make_download_dir(file)
        self.history = deque()
        self.current_page = None

    def make_download_dir(self, file):
        if file is None:
            file = "tmp"
        if not os.path.exists(file):
            os.mkdir(file)
        return file

    def load_page(self, url):
        path = re.sub(r'(http(s)?://)', '', url)
        path = self.save_dir + '/' + path + '.txt'
        if os.path.exists(path):
            if self.current_page:
                self.history.append(self.current_page)
            with open(path, 'r') as f:
                print(f.read())
                self.current_page = url
        else:
            self.download_page(url)

    def download_page(self, url):
        if check_url(url):
            if not url.startswith('http'):
                url = "https://" + url
            r = requests.get(url)
            if r:
                content = parse_page(r.content)
            else:
                print("Error")
                return

            file_name = url[:url.rfind('.')]
            file_name = re.sub(r'(http(s)?://)', '', file_name)
            with open(self.save_dir + '/' + file_name + '.txt', 'w') as file:
                file.write(content)

            self.load_page(file_name)
        else:
            print("Error: Incorrect URL")

    def previous(self):
        if self.history:
            file_name = self.history.pop()
            self.current_page = None
            self.load_page(file_name)

    def exit(self):
        if self.save_dir == "tmp":
            try:
                shutil.rmtree(self.save_dir)
            except OSError as e:
                print("Error: %s - %s." % (e.filename, e.strerror))


def parse_page(content):
    include_tags = ['title', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']
    def text_tag(e):
        return e.parent.name in include_tags
    soup = BeautifulSoup(content, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts=[]
    for i in texts:
        if i.parent.name in include_tags:
            if i.parent.name == 'a':
                i = Fore.BLUE + i
            else:
                i = Fore.WHITE + i
            visible_texts.append(i)
    #visible_texts = filter(text_tag, texts)
    return "\n".join(t.strip() for t in visible_texts)

def check_url(url):
    return re.match(r'^(http(s)?://.)?(www\.)?[-a-zA-Z0-9@:%._+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_+.~#?&/=]*)$', url.lower())


def main():
    browser = Browser() if len(sys.argv) == 1 else Browser(sys.argv[1])

    while True:
        command = input('> ').strip()
        if command == 'exit':
            browser.exit()
            break
        elif command == 'back':
            browser.previous()
        else:
            browser.load_page(command)


if __name__ == '__main__':
    main()
