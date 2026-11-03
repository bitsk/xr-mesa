#!/usr/bin/env python3
import argparse,json,shutil,subprocess
from pathlib import Path
r=Path(__file__).resolve().parents[1];p=argparse.ArgumentParser();p.add_argument('--output',required=True,type=Path);p.add_argument('--upstream-repo',type=Path);a=p.parse_args();lock=json.loads((r/'upstream.json').read_text());out=a.output.resolve()
if out.exists():p.error('Use a new output directory')
source=str(a.upstream_repo.resolve()) if a.upstream_repo else lock['repository']
cmd=['git','clone','--no-checkout']+(['--shared'] if a.upstream_repo else ['--filter=blob:none'])+[source,str(out)]
subprocess.run(cmd,check=True);subprocess.run(['git','-C',str(out),'checkout','-B','xr/adaptation',lock['commit']],check=True)
for key in ['user.name','user.email']:
 value=subprocess.check_output(['git','-C',str(r),'config','--get',key],text=True).strip();subprocess.run(['git','-C',str(out),'config',key,value],check=True)
patches=[str(r/'patches'/name) for name in (r/lock['patch_series']).read_text().splitlines() if name.strip()]
subprocess.run(['git','-C',str(out),'am',*patches],check=True)
for directory in ['packaging','devices','debian']:
 if (r/directory).exists():shutil.copytree(r/directory,out/directory,dirs_exist_ok=True)
if (r/'include/uapi/linux').exists():
 for header in (r/'include/uapi/linux').glob('*.h'):
  if header.read_bytes()!=(out/'include/uapi/linux'/header.name).read_bytes():raise ValueError('Exported UAPI snapshot differs from patch stack')
print(json.dumps({'source':str(out),'upstream':lock['commit'],'patches':len(patches),'device_validated':False}))
