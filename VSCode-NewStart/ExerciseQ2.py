import os

def get_file_list(directory):
    file_list = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_list.append(file_path)
    return file_list

# Specify the directory path
directory_path = "C:/Users/Tom/Desktop"

# Get the list of files in the directory
files = get_file_list(directory_path)

# Print the file names
for file in files:
   print(file)