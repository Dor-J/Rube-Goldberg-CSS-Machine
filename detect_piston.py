from pathlib import Path
import numpy as np
from PIL import Image
bg = np.array(Image.open('frames/background.png').convert('RGB'), dtype=np.int16)
frames = sorted(Path('frames').glob('frame_*.png'))
region = (650, 150, 950, 350)
for f in frames:
    img = np.array(Image.open(f).convert('RGB'), dtype=np.int16)
    diff = np.abs(img - bg).sum(axis=2)
    x1,y1,x2,y2 = region
    sub = diff[y1:y2, x1:x2]
    moved = int((sub > 60).sum())
    print(f.name, moved)
