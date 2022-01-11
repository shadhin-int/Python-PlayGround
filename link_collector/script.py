import sys
import requests
import re
from os.path import exists


def is_url_exist(url):
    with open('link_data.txt', 'r+') as f:
        for line in f.readlines():
            if url in line:
                print("Not found any new data for add!")
                return True
        return False

def add_to_txt_file(data, mode):
    with open('link_data.txt', mode=mode) as f:
        aa = is_url_exist(url=data)
        if aa is not True:
            f.write(data)
            f.write('\n')
            print(f"New link -> {data} added...")


def main():
    for url in sys.argv[1:]:
        # response = requests.get('https://raw.githubusercontent.com/shadhin-int/Python-Script/main/links.txt')
        response = requests.get(url=url)

        if response.status_code in [200,201]:
            for data in response.iter_lines():
                ress = re.search("(?P<url>https?://[^\s]+)", str(data)).group("url")
                is_file_exit = exists('link_data.txt')
                if is_file_exit is True:
                    add_to_txt_file(data=ress, mode='a+')
                else:
                    print("File not found.... create file and add your data....")
                    add_to_txt_file(data=ress, mode='w+')



if __name__ == "__main__":
    main()