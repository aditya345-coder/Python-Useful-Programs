import os

def rename_files(folder, prefix="SFW Image"):
    """Renames files in a folder with a sequential numbering scheme, preserving their original extensions.

    Args:
        folder (str): The path to the folder containing the files.
        prefix (str, optional): The prefix for the new filenames. Defaults to "Hostel".
    """

    for count, filename in enumerate(os.listdir(folder)):
        filename_parts = os.path.splitext(filename)
        new_filename = f"{prefix} {str(count + 1)}{filename_parts[1]}"
        src = os.path.join(folder, filename)
        dst = os.path.join(folder, new_filename)

        try:
            os.rename(src, dst)
            print(f"Renamed {src} to {dst}")
        except OSError as e:
            print(f"Error renaming {src}: {e}")

# Example usage
folder_path = "SFW Images"
rename_files(folder_path)