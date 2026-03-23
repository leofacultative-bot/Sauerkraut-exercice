from PIL import Image, ImageDraw, ImageFont
import os

sizes = [72, 96, 128, 144, 152, 192, 384, 512]

for size in sizes:
    img = Image.new('RGB', (size, size), color='#080b10')
    draw = ImageDraw.Draw(img)
    
    # Draw a colored circle accent
    margin = size * 0.12
    draw.ellipse([margin, margin, size-margin, size-margin], outline='#ff6b35', width=max(2, size//40))
    
    # Draw "St" text
    font_size = int(size * 0.38)
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', font_size)
    except:
        font = ImageFont.load_default()
    
    text = "St"
    bbox = draw.textbbox((0,0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (size - tw) / 2 - bbox[0]
    y = (size - th) / 2 - bbox[1]
    draw.text((x, y), text, fill='#e2e8f5', font=font)
    
    img.save(f'/home/claude/study-timer-pwa/icons/icon-{size}.png')
    print(f'Generated icon-{size}.png')

print('Done!')
