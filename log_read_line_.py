import os
import re
def check_word_in_last_line(file_path, word):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        last_line = lines[-1].strip()  # Remove leading/trailing whitespace
        
        if word in last_line:
            # return True
            match = re.search(r'perc:(\d+:.*$)', last_line)
        
            if match:
                desired_string = match.group(1)
                print(desired_string)
                
            else:
                print("Substring not found.")
        else:
            return False

folder_path = "C:/Users/ppravallika/Downloads/autoxlogs/logs"
extension = ".log"  # Replace with your desired file extension
word_to_check = "perc:"

for file_name in os.listdir(folder_path):
    if file_name.endswith(extension):
        file_path = os.path.join(folder_path, file_name)
        if check_word_in_last_line(file_path, word_to_check):
            # print(f"The word '{word_to_check}' was found in the last line of file: {file_path}")
            pass
        else:
            # print(f"The word '{word_to_check}' was not found in the last line of file: {file_path}")
            pass
