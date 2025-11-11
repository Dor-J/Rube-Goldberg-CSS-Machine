from pathlib import Path
import numpy as np
from PIL import Image
bg = np.array(Image.open('frames/background.png').convert('RGB'), dtype=np.uint8)
bg_white = (bg[...,0] > 240) & (bg[...,1] > 240) & (bg[...,2] > 240)
frames = sorted(Path('frames').glob('frame_*.png'))
for f in frames:
    img = np.array(Image.open(f).convert('RGB'), dtype=np.uint8)
    white = (img[...,0] > 240) & (img[...,1] > 240) & (img[...,2] > 240)
    mask = white & (~bg_white)
    ys, xs = np.where(mask)
    if len(xs) == 0:
        print(f.name, 'no ball mask')
        continue
    cx = xs.mean(); cy = ys.mean()
    print(f.name, 'ball approx', round(cx,1), round(cy,1), 'count', len(xs))
