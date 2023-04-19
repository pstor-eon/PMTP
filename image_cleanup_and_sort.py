import os
import shutil
from datetime import datetime

target_directory = "/path/to/your/folder"

def is_image(file):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp']
    return any(file.lower().endswith(ext) for ext in image_extensions)

today_date = datetime.now().strftime('%Y-%m-%d')
today_folder = os.path.join(target_directory, today_date)

if not os.path.exists(today_folder):
    os.makedirs(today_folder)

# Move images not in any folder to the folder created today
for item in os.listdir(target_directory):
    item_path = os.path.join(target_directory, item)

    if os.path.isfile(item_path) and is_image(item):
        new_path = os.path.join(today_folder, item)
        shutil.move(item_path, new_path)
        print(f"Moved {item_path} to {new_path}")
