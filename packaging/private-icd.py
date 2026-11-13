#!/usr/bin/env python3
import json,shutil,subprocess,sys
from pathlib import Path
root=Path(sys.argv[1]);triplet=subprocess.check_output(['dpkg-architecture','-qDEB_HOST_MULTIARCH'],text=True).strip();private=root/'usr/lib'/triplet/'xr-mesa';target=private/'icd.d';target.mkdir(parents=True,exist_ok=True)
for path in (root/'usr/share/vulkan/icd.d').glob('*.json'):
 # Meson's cross-file CPU spelling can be armv8-a rather than aarch64.
 # The ARM64 package owns one stable path consumed by the session profile.
 if not path.name.startswith('freedreno_icd.') or triplet!='aarch64-linux-gnu':
  raise ValueError('Unexpected private ICD target: '+path.name+' / '+triplet)
 item=json.loads(path.read_text());item['ICD']['library_path']=str(Path('/usr/lib')/triplet/'xr-mesa/libvulkan_freedreno.so');(target/'freedreno_icd.aarch64.json').write_text(json.dumps(item,indent=2)+'\n');path.unlink()
shutil.rmtree(root/'usr/share',ignore_errors=True)
