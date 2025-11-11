from pathlib import Path
import numpy as np
from PIL import Image
bg = np.array(Image.open('frames/background.png').convert('RGB'), dtype=np.uint8)
frames = sorted(Path('frames').glob('frame_*.png'))
regions = {
    'tube': (120, 60, 560, 180),
    'coil': (40, 140, 260, 460),
    'ramp': (210, 300, 350, 420),
    'funnel': (330, 140, 560, 360),
    'ring': (640, 80, 900, 360),
    'slide': (640, 320, 940, 520)
}
for f in frames:
    img = np.array(Image.open(f).convert('RGB'), dtype=np.uint8)
    diff = np.abs(img.astype(int) - bg.astype(int)).sum(axis=2)
    white = (img[...,0] > 230) & (img[...,1] > 230) & (img[...,2] > 230)
    mask = (diff > 60) & white
    counts = {}
    for name, (x1,y1,x2,y2) in regions.items():
        counts[name] = int(mask[y1:y2, x1:x2].sum())
    region = max(counts, key=counts.get)
    total = int(mask.sum())
    print(f.name, '->', region, counts[region], 'of', total, counts)
