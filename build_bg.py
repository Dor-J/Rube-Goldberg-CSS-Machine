from pathlib import Path
import numpy as np
from PIL import Image
frames = sorted(Path('frames').glob('frame_*.png'))
stack = []
for f in frames:
    stack.append(np.array(Image.open(f).convert('RGB'), dtype=np.uint8))
arr = np.stack(stack, axis=0)
median = np.median(arr, axis=0).astype(np.uint8)
Image.fromarray(median).save('frames/background.png')
print('saved background.png')
