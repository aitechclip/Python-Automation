import os
import shutil
import datetime

def create_backup(source_dir, backup_dir):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_dir_with_time = os.path.join(backup_dir, timestamp)

    try:
        shutil.copytree(source_dir, backup_dir_with_time)
        print(f"Backup created from '{source_dir}' to '{backup_dir_with_time}'")
    except Exception as e:
        print(f"Error creating backup: {e}")

if __name__ == "__main__":
    source_directory = "/path/to/source/directory"  # Customize source directory
    backup_directory = "/path/to/backup/directory"  # Customize backup directory

    create_backup(source_directory, backup_directory)
