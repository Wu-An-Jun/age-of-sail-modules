AGE OF SAIL — COMPLETE FOOTPRINT MODULE SPRITES

136 PNG sprites cover the 229 modules described in the supplied art request.
P1: 76 sprites. P2: 51 sprites. P3: 9 sprites. No pending entries.

INSTALL
Copy assets/Nautical/Modules/ into the corresponding game folder.
Preserve exact case-sensitive filenames, including legacy spellings.
From the game repository, run: python porting/make_module_art.py
That repository was not supplied, so this import command has not been run here.
Keep existing square list icons. These sprites replace hull-grid module pictures.
Delivered gun sprites replace assembled barrels; no extra gun pieces are needed.

FORMAT
RGBA PNG, 64 pixels per hull cell. Canvas is exactly width*64 by height*64.
Bow and firing direction are up. Negative footprint cells are fully transparent.
No extra margins or numbered grid cells. Interpret the entire sprite as one object.
Warm painted nautical equipment: oak, brass, iron and canvas.
No boarding combat assets or new boarding mechanics are included.

CONTENTS
assets/: 136 runtime PNGs with original requested filenames.
source/: individual full-resolution generation images, before sizing and mask export.
manifest.json / ASSET_INDEX.csv: authoritative mappings and footprint geometry.
generation_prompts.json: English image generation prompts.
AI_INTEGRATION_PROMPT.txt: English instructions for an AI coding assistant.
preview.html / previews/: offline review gallery and contact sheets.
validation_report.json / validate_modules.py: geometry and format checks.
SHA256SUMS.txt: file checksums.

VALIDATION LIMITS
All filenames, dimensions, alpha modes and negative cells were checked.
Every occupied cell contains artwork. Visual style includes painted shading.
Gameplay readability, pivots and rotation should be reviewed in the actual engine.
Generation used the built-in image generation tool, one call per distinct asset.
