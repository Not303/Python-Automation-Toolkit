import os
import shutil
import sys

EXTENSION_MAP = {
    ".txt": "Text_Files",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".exe": "Installers",
    ".zip": "Archives",
    ".py": "Scripts",
    ".sh": "Scripts"
}

if len(sys.argv) < 2:
    print("Error: You must provide a folder path.")
    print("Usage: python3 file_organizer.py <FOLDER_PATH>")
    sys.exit()

folder_path = sys.argv[1] #the main dir path
print(f"--- Sorting {folder_path} ---")

for filename in os.listdir(folder_path):
    source = f"{folder_path}/{filename}"
    
    if os.path.isdir(source):
        continue    #skip dirs
    _, extension = os.path.splitext(filename)   #get extension
    extension = extension.lower() # Normalize to lowercase
    if extension in EXTENSION_MAP:   #filtering
        folder_name = EXTENSION_MAP[extension]
        destination_folder = f"{folder_path}/{folder_name}"
        
        if not os.path.exists(destination_folder): #create dir if not exist
            os.mkdir(destination_folder)
            print(f"created the folder {folder_name}")
            
        destination=f"{destination_folder}/{filename}" #final path (to)
        
        shutil.move(source,destination)
        print(f"Moved: {filename}")
print("Clean up complete.")