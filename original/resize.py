from PIL import Image
import os
from pathlib import Path

def resize_image(input_path, output_name, target_height=1000):
    try:
        img = Image.open(input_path)
        # Convert to PNG if it isn't
        if img.format != 'PNG':
            img = img.convert('RGBA')

        # Get the aspect ratio
        width, height = img.size
        aspect_ratio = width / height

        # Check if the aspect ratio is roughly 3:2 with 15% range allowance
        if 0.85 * (3/2) <= aspect_ratio <= 1.15 * (3/2):
            # Resize image maintaining aspect ratio
            new_width = int(target_height * aspect_ratio)
            new_img = img.resize((new_width, target_height))

            # Save image in the script's directory
            new_img.save(f"{output_name}.png", 'PNG')
        else:
            print("Please crop the image to a 3:2 ratio")
            exit()

    except Exception as e:
        print(f"Failed to process image. Error: {e}")
        exit()

if __name__ == "__main__":
    first_image_path = input("Entrez le chemin vers le recto. Enter the path of the onward side (the one with the portrait): ").strip().replace('\\', '')
    second_image_path = input("Entrez le chemin vers le verso. Enter the path of the forward side (the one with the address): ").strip().replace('\\', '')

    # Convert input paths to absolute paths
    first_image_path = Path(first_image_path).resolve()
    second_image_path = Path(second_image_path).resolve()

    resize_image(first_image_path, "CNI-recto-original")
    resize_image(second_image_path, "CNI-verso-original")
