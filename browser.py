import re
import sys
import os
import shutil
import requests


websites = {
    "bloomberg.com": bloomberg_com,
    "nytimes.com": nytimes_com
}


class Browser:
    def __init__(self, file=None):
        self.save_dir = self.make_dowload_dir(file)
        self.history = []
        self.current_page = None

    def make_dowload_dir(self, file):
        if file is None:
            file = "tmp"
        if not os.path.exists(file):
            os.mkdir(file)
        return file

    def load_page(self, url):
        path = re.sub(r'(http(s)?:\/\/)', '', url)
        path = self.save_dir + '/' + url + '.txt'
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
                content = r.text
            else:
                print("Error")
                return

            file_name = url[:url.rfind('.')]
            file_name = re.sub(r'(http(s)?:\/\/)', '', file_name)
            with open(self.save_dir + '/' + file_name + '.txt', 'w') as file:
                file.write(content)

            self.load_page(file_name)
        else:
            print("Error: Incorrect URL")

    def previous(self):
        if self.history:
            file_name = self.history.pop()
            with open(self.save_dir + '/' + file_name + '.txt', 'r') as file:
                print(file.read())

    def exit(self):
        if self.save_dir == "tmp":
            try:
                shutil.rmtree(self.save_dir)
            except OSError as e:
                print("Error: %s - %s." % (e.filename, e.strerror))

def check_url(url):
    return re.match(r'^(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)$', url.lower())

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
