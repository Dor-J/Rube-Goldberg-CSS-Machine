from pathlib import Path
from PIL import Image, ImageChops
import numpy as np
frames_dir = Path('frames')
frames = sorted(frames_dir.glob('frame_*.png'))
report = []
prev = None
for idx, frame_path in enumerate(frames):
    img = Image.open(frame_path).convert('RGB')
    arr = np.array(img)
    white_mask = (arr[...,0] > 235) & (arr[...,1] > 235) & (arr[...,2] > 235)
    ys, xs = np.where(white_mask)
    if len(xs):
        cx = float(xs.mean())
        cy = float(ys.mean())
    else:
        cx = cy = float('nan')
    bbox = None
    if prev is not None:
        diff = ImageChops.difference(img, prev)
        diff_gray = diff.convert('L')
        diff_arr = np.array(diff_gray)
        y, x = np.where(diff_arr > 30)
        if len(x):
            bbox = (int(x.min()), int(y.min()), int(x.max()), int(y.max()))
    report.append((frame_path.name, cx, cy, bbox))
    prev = img
for name, cx, cy, bbox in report:
    print(name, 'center', round(cx,1), round(cy,1), 'bbox', bbox)
