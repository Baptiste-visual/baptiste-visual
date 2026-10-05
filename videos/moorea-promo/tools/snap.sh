#!/usr/bin/env bash
# Dev-only: screenshot a frame composition at given local times and build a contact sheet.
# usage: tools/snap.sh <frame_id> <t1> [t2 ...]   -> .hyperframes/snaps/<frame_id>-sheet.jpg
set -e
cd "$(dirname "$0")/.."
F="$1"; shift
CH=$(ls -d /root/.cache/hyperframes/chrome/chrome-headless-shell/*/chrome-headless-shell-linux64/chrome-headless-shell | head -1)
mkdir -p .hyperframes/snaps
OUTS=()
for T in "$@"; do
  O=".hyperframes/snaps/$F-$T.png"
  timeout 60 "$CH" --no-sandbox --allow-file-access-from-files --use-angle=swiftshader --enable-unsafe-swiftshader \
    --hide-scrollbars --screenshot="$O" --window-size=1920,1080 --virtual-time-budget=6000 \
    "file://$PWD/tools/frame-harness.html?f=$F&t=$T" >/dev/null 2>&1 || true
  OUTS+=("$O")
done
python3 - "$F" "${OUTS[@]}" <<'PY'
import sys
from PIL import Image
f=sys.argv[1]; files=sys.argv[2:]
ims=[Image.open(x).convert('RGB').resize((640,360)) for x in files]
cols=3; rows=(len(ims)+cols-1)//cols
sheet=Image.new('RGB',(640*cols,360*rows),(0,0,0))
for i,im in enumerate(ims): sheet.paste(im,((i%cols)*640,(i//cols)*360))
out=f'.hyperframes/snaps/{f}-sheet.jpg'; sheet.save(out,quality=85); print(out)
PY
