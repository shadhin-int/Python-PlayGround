import sys
import requests
import re
from os.path import exists


def check_url_exist(url):
    with open('links.txt', 'r+') as f:
        for line in f.readlines():
            if url in line:
                return True
        return False

def add_to_txt_file(url, mode):
    with open('links.txt', mode=mode) as f:
        is_url_exist = check_url_exist(url=url)
        if is_url_exist is False:
            f.write(url)
            f.write('\n')
            print(f"New link -> {url} added...")
        else:
            print("Not found any new data ...!")



def main():
    for url in sys.argv[1:]:
        # response = requests.get('https://raw.githubusercontent.com/shadhin-int/Python-Script/main/links.txt')
        response = requests.get(url=url)

        if response.status_code in [200,201]:
            for data in response.iter_lines():
                get_url = re.search("(?P<url>https?://[^\s]+)", str(data)).group("url")
                is_file_exit = exists('links.txt')
                if is_file_exit is True:
                    add_to_txt_file(url=get_url, mode='a+')
                else:
                    print("File not found.... create file and add your data....")
                    add_to_txt_file(url=get_url, mode='w+')



if __name__ == "__main__":
    main()