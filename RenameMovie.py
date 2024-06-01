import os
import re

def process_filename(filename):
    # Separate the file name and the extension
    name, ext = os.path.splitext(filename)
    
    # Replace the point '.' by a space ' ', except for the file extension point
    name = name.replace('.', ' ')
    name = name.replace('(', '')
    name = name.replace(')', '')
    
    # Remove the digit '1080' or 2160 if it exists
    name = name.replace('1080', '')
    name = name.replace('2160', '')
    

    # Identify any 4 consecutive numbers that represent a year
    match = re.search(r'(\d{4})', name)
    if match:
        year = match.group(1)
        name = name.replace(year,f'({year})')

    # Remove all characters after the year in parenthesis except the extension
    # remove the double parenthesis because the code above is dumb and creates a double parenthesis 
    name = re.sub(r'\(\d{4}\).*', r'(\g<0>)', name)
    name = re.sub(r'\((\d{4})\).*', r'(\1)', name)
    name = name.replace('((','(')
    return name + ext

def rename_files_in_directory():
    for filename in os.listdir('.'):
        if os.path.isfile(filename):
            new_name = process_filename(filename)
            os.rename(filename, new_name)
            print(f'Renamed: {filename} -> {new_name}')

if __name__ == "__main__":
    rename_files_in_directory()
