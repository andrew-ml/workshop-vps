import os
import re
import cv2
from time import sleep
from datetime import datetime
from pathlib import Path

INPUT_PATH = '/home/ftpuser/input'
OUTPUT_PATH = '/home/ftpuser/output'

def main():
    print('.')
    Path(INPUT_PATH).mkdir(parents=True, exist_ok=True)
    Path(OUTPUT_PATH).mkdir(parents=True, exist_ok=True)

    dir_list = os.listdir(INPUT_PATH)

    for filename in dir_list:
        full_input_path = os.path.join(INPUT_PATH, filename)

        if re.match(r'.*(jpg|jpeg|png)', filename):
            img = cv2.imread(full_input_path)
            img_inv = cv2.bitwise_not(img)

            timestamp = datetime.now().strftime("%Y-%d-%m_%H-%M-%S")

            filename_edited = re.sub('(.[^.]*)$', rf'_{timestamp}\1', filename)
            cv2.imwrite(os.path.join(OUTPUT_PATH, filename_edited), img_inv)

            
            print(f'Saved {filename_edited} file to output folder')
        else:
            print(f'Error, file {filename} is not an image')
        
        os.remove(full_input_path)


if __name__ == '__main__':
    while True:
        main()
        sleep(1)