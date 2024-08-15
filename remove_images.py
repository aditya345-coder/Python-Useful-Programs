import os
import random

def remove_random_images(folder, num_images=4):
    """Recursively removes a specified number of random images from a folder and its subdirectories.

    Args:
        folder (str): The path to the root folder.
        num_images (int, optional): The number of images to delete. Defaults to 4.
    """

    for root, dirs, files in os.walk(folder):
        image_files = [f for f in files if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]  # Adjust image extensions as needed
        if len(image_files) > 0:
            random.shuffle(image_files)
            for _ in range(min(num_images, len(image_files))):
                image_path = os.path.join(root, image_files.pop())
                try:
                    os.remove(image_path)
                    print(f"Removed image: {image_path}")
                except FileNotFoundError:
                    print(f"Error removing image: {image_path}")

# Example usage
folder = "folder name"
remove_random_images(folder, num_images=2)  # Delete 2 random images
