import os
import shutil

# Path to your Downloads folder
DOWNLOADS_FOLDER = os.path.join(os.path.expanduser("~"), "Downloads")

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
}

# Create category folders if not present
def create_category_folders(base_path):
    for category in FILE_TYPES:
        category_path = os.path.join(base_path, category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
    # Create 'Others' folder for unmatched types
    others_path = os.path.join(base_path, "Others")
    if not os.path.exists(others_path):
        os.mkdir(others_path)

# Get category based on file extension
def get_category(file_name):
    ext = os.path.splitext(file_name)[1].lower()
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
    return "Others"

# Move files into categorized folders
def organize_files():
    create_category_folders(DOWNLOADS_FOLDER)
    files = os.listdir(DOWNLOADS_FOLDER)

    for file in files:
        file_path = os.path.join(DOWNLOADS_FOLDER, file)
        if os.path.isfile(file_path):
            category = get_category(file)
            destination = os.path.join(DOWNLOADS_FOLDER, category, file)
            try:
                shutil.move(file_path, destination)
                print(f"Moved: {file} ➜ {category}")
            except Exception as e:
                print(f"Failed to move {file}: {e}")

# Run the organizer
if __name__ == "__main__":
    organize_files()
