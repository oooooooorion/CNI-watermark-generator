from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import pandas as pd

arial_font_path = '/System/Library/Fonts/Supplemental/Arial.ttf'

def watermark_text(input_image_path, output_image_path, text, pos):
    # Load image
    base_image = Image.open(input_image_path).convert("RGBA")

    # Make image editable
    txt = Image.new('RGBA', base_image.size, (255,255,255,0))

    # Load font (change the path if needed)
    font = ImageFont.truetype(arial_font_path, 15)
    
    # Prepare draw and text
    d = ImageDraw.Draw(txt)
    d.text(pos, text, font=font, fill=(0,0,0,76)) # 30% opacity (0,0,0,76)

    watermarked = Image.alpha_composite(base_image, txt)
    watermarked.save(output_image_path, 'PNG')

def append_to_csv(text, csv_path):
    df = pd.DataFrame([[text, datetime.now()]], columns=["Watermark", "Timestamp"])
    df.to_csv(csv_path, mode='a', header=False, index=False)

if __name__ == '__main__':
    # Input parameters
    input_image_path1 = 'original/CNI-recto-original.png'
    output_image_path1 = 'CNI-recto.png'

    input_image_path2 = 'original/CNI-verso-original.png'
    output_image_path2 = 'CNI-verso.png'

    csv_path = 'watermark_log.csv'
    pos = (1113, 71)

    text = input("Enter watermark text: ")
    
    watermark_text(input_image_path1, output_image_path1, text, pos)
    append_to_csv(text, csv_path)

    watermark_text(input_image_path2, output_image_path2, text, pos)
    append_to_csv(text, csv_path)

    print(f"Watermark '{text}' added to images and logged in CSV.")
