#!/usr/bin/env python3
import json,shutil,subprocess,sys
from pathlib import Path
root=Path(sys.argv[1]);triplet=subprocess.check_output(['dpkg-architecture','-qDEB_HOST_MULTIARCH'],text=True).strip();private=root/'usr/lib'/triplet/'xr-mesa';target=private/'icd.d';target.mkdir(parents=True,exist_ok=True)
for path in (root/'usr/share/vulkan/icd.d').glob('*.json'):
 item=json.loads(path.read_text());item['ICD']['library_path']=str(Path('/usr/lib')/triplet/'xr-mesa/libvulkan_freedreno.so');(target/path.name).write_text(json.dumps(item,indent=2)+'\n');path.unlink()
shutil.rmtree(root/'usr/share',ignore_errors=True)
