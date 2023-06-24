# Helper functions
import sys
import os
import re

def codedir(filename):
    return os.path.join("code", filename)

def yesno(prompt, answers = ["y", "n"]):
    answer = ""
    while answer not in answers:
        slash_list = '/'.join(answers)
        answer = input(f"{prompt} ({slash_list}): ")
        if answer not in answers:
            or_list = "' or '".join(answers)
            print(f"ERROR:    Please type '{or_list}'")
    return answer

def safepath(path):
    if path == ".":
        path = ""

    base = os.path.abspath("code")
    file = os.path.abspath(os.path.join(base, path))

    if os.path.commonpath([base, file]) != base:
        print(f"ERROR:    Tried to access file '{file}' outside of code folder!")
        sys.exit(1)

    return path

def extract_number(filename):
    match = re.search(r'\d+', filename)
    if match:
        return int(match.group())
    else:
        return 0

def numberfile(parent_folder, folder=False):
    # Get a list of all files/folders in the parent folder
    items = [item for item in os.listdir(parent_folder)]

    # Find the highest numbered file/folder
    highest_number = 0
    for item in items:
        if folder and os.path.isdir(os.path.join(parent_folder, item)):
            item_number = extract_number(item)
            if item_number > highest_number:
                highest_number = item_number
        elif not folder and os.path.isfile(os.path.join(parent_folder, item)):
            item_number = extract_number(item)
            if item_number > highest_number:
                highest_number = item_number

    # Increment the highest number
    new_item_number = highest_number + 1
    new_item_name = str(new_item_number).zfill(4)

    return new_item_name
