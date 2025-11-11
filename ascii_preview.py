from pathlib import Path
from PIL import Image
chars = ' .:-=+*#%@'
frames = sorted(Path('frames').glob('frame_*.png'))
for frame in frames:
    img = Image.open(frame).convert('L').resize((80, 48))
    pixels = img.load()
    print('\n', frame.name)
    for y in range(img.height):
        line = ''.join(chars[pixels[x,y]*len(chars)//256] for x in range(img.width))
        print(line)
    break
