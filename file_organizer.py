import os
import shutil
import sys

if len(sys.argv) < 2:
    print("Error: You must provide a folder path.")
    print("Usage: python3 file_organizer.py <FOLDER_PATH>")
    sys.exit()

folder_path = sys.argv[1] #the main dir path
for filename in os.listdir(folder_path):
    
    if filename.endswith(".txt"):   #filtering
        destination_folder = f"{folder_path}/tempf"
        
        if not os.path.exists(destination_folder): #create dir if not exist
            os.mkdir(destination_folder)
            print("created the folder.")
            
        source=f"{folder_path}/{filename}"  #source path (from)
        destination=f"{destination_folder}/{filename}" #final path (to)
        shutil.move(source,destination)
        print(f"Moved: {filename}")
print("Clean up complete.")