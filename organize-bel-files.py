import os
import shutil

# Set your source directory here
SOURCE_DIR = "hemeKG-bel-files"  # Change if needed
DEST_ORIGINAL = "data/original-hemeKG"
DEST_CLEANED = "data/cleaned-original-hemeKGbel"

# Create destination folders if they don't exist
os.makedirs(DEST_ORIGINAL, exist_ok=True)
os.makedirs(DEST_CLEANED, exist_ok=True)

# Process files in the source directory
for filename in os.listdir(SOURCE_DIR):
    if filename.endswith(".bel") and not filename.endswith("_cleaned.bel"):
        src_path = os.path.join(SOURCE_DIR, filename)
        dst_path = os.path.join(DEST_ORIGINAL, filename)
        shutil.move(src_path, dst_path)
        print(f"Moved {filename} to {DEST_ORIGINAL}")
    elif filename.endswith("_cleaned.bel"):
        src_path = os.path.join(SOURCE_DIR, filename)
        dst_path = os.path.join(DEST_CLEANED, filename)
        shutil.move(src_path, dst_path)
        print(f"Moved {filename} to {DEST_CLEANED}")
