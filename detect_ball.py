from pathlib import Path
import numpy as np
from PIL import Image
bg = np.array(Image.open('frames/background.png').convert('RGB'), dtype=np.int16)
frames = sorted(Path('frames').glob('frame_*.png'))
for f in frames:
    img = np.array(Image.open(f).convert('RGB'), dtype=np.int16)
    diff = np.abs(img - bg).sum(axis=2)
    mask = diff > 60
    ys, xs = np.where(mask)
    if len(xs) == 0:
        print(f.name, 'no diff')
        continue
    cx = float(xs.mean())
    cy = float(ys.mean())
    print(f.name, 'centroid', round(cx,1), round(cy,1), 'pixels', len(xs))
