from pathlib import Path
from PIL import Image
import json
root=Path(__file__).resolve().parent
items=json.loads((root/'manifest.json').read_text())
assert len(items)==136, 'Expected 136 module sprites'
assert len({a['file'] for a in items})==136
for a in items:
 im=Image.open(root/a['path'])
 assert im.mode=='RGBA' and im.size==(a['width'],a['height']),a['file']
 alpha=im.getchannel('A')
 for y,row in enumerate(a['footprint']):
  for x,v in enumerate(row):
   box=alpha.crop((x*64,y*64,(x+1)*64,(y+1)*64)).getbbox()
   assert bool(box)==(v=='■'),(a['file'],x,y)
print('PASS: 136 unique RGBA sprites, exact dimensions, transparent negative cells, nonempty occupied cells.')
