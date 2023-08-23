import os
import sys
import shutil

def organize_files(target_dir):
    if not os.path.exists(target_dir):
        print(f"Directory '{target_dir}' does not exist.")
        return

    for filename in os.listdir(target_dir):
        if filename == "file_organizer.py":
            continue

        filepath = os.path.join(target_dir, filename)
        if os.path.isfile(filepath):
            file_extension = filename.split(".")[-1]
            if file_extension:
                destination_dir = os.path.join(target_dir, file_extension)
                os.makedirs(destination_dir, exist_ok=True)
                destination_path = os.path.join(destination_dir, filename)
                shutil.move(filepath, destination_path)
                print(f"Moved '{filename}' to '{destination_dir}'")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python file_organizer.py <target_directory>")
    else:
        target_directory = sys.argv[1]
        organize_files(target_directory)
