import os
import shutil
from pathlib import Path

# Base directory
base_dir = r"C:\Users\m214128\Downloads\BattleSpaceGDD\files"

# Move all files from subdirectories to base_dir
for root, dirs, files in os.walk(base_dir):
    if root == base_dir:
        continue
    
    for file in files:
        src = os.path.join(root, file)
        dst = os.path.join(base_dir, file)
        
        # Handle name conflicts
        if os.path.exists(dst):
            name, ext = os.path.splitext(file)
            counter = 1
            while os.path.exists(dst):
                dst = os.path.join(base_dir, f"{name}_{counter}{ext}")
                counter += 1
        
        shutil.move(src, dst)
        print(f"Moved: {file}")

# Remove empty directories
for root, dirs, files in os.walk(base_dir, topdown=False):
    for dir in dirs:
        dir_path = os.path.join(root, dir)
        try:
            os.rmdir(dir_path)
            print(f"Removed empty dir: {dir}")
        except:
            pass

print("Done!")