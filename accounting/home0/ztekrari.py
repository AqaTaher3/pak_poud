import os
import shutil
import random
import string
import sys

main_directory = 11
destination_directory = 11

def generate_random_letters(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def move_duplicate_files(directory):
    files = [f for f in os.listdir(directory) if f.endswith('.jpg')]
    duplicate_files = {}
    
    for file in files:
        random_letters = generate_random_letters(2)
        new_filename = random_letters + file
        
        if new_filename in duplicate_files:
            destination_path = os.path.join(destination_directory, new_filename)
            shutil.move(os.path.join(directory, file), destination_path)
            duplicate_files[new_filename].append(destination_path)
        else:
            duplicate_files[new_filename] = [os.path.join(directory, file)]
    
    for filename, paths in duplicate_files.items():
        if len(paths) > 1:
            print(f'فایل‌های همنام "{filename}":', file=sys.stdout)
            for path in paths:
                print(path, file=sys.stdout)

for root, dirs, files in os.walk(main_directory):
    move_duplicate_files(root)