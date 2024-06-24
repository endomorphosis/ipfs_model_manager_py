import os
import asyncio
import subprocess
from ipfs_model_manager import ipfs_model_manager
model_manager = ipfs_model_manager()
asyncio.run(model_manager.run_once())
print('done running test.py')
kill_cmd = 'kill -9 $(lsof -t -i:50001)'
os.system(kill_cmd)
ps_orbitdb = "ps aux | grep orbitdb | grep -v grep | awk \'{print $2}\' "
ps_orbitdb_results = subprocess.check_output(ps_orbitdb, shell=True).decode()
if ps_orbitdb_results != "":
    kill_orbitdb = 'kill -9 ' + ps_orbitdb_results
    kill_orbitdb_results = subprocess.check_output(kill_orbitdb, shell=True).decode()
os.system(kill_orbitdb)
