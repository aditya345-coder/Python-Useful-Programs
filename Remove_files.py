import os
import re
import traceback

def remove_files(path, extension):
    """Removes file on the basis of extension from both single and nested folders.

    Args:
        path (str): Path to the root folder.
    """

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):  # Check for MP4 files
                try:
                    os.remove(os.path.join(root, file))
                    print(f"Removed video: {os.path.join(root, file)}")
                except Exception as e:
                    print(f"Error removing video: {e}")

# Example usage
path = "Folder 1"
remove_files(path, '.mp4')