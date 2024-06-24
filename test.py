import os
import asyncio
import subprocess
from ipfs_model_manager import ipfs_model_manager

async def run():
    model_manager = ipfs_model_manager()
    await model_manager.run_once()
    model_manager.download_model('bge-small-en-v1.5')
    kill_cmd = 'kill -9 $(lsof -t -i:50001)'
    os.system(kill_cmd)
    ps_orbitdb = "ps aux | grep orbitdb | grep -v grep | awk \'{print $2}\' "
    ps_orbitdb_results = subprocess.check_output(ps_orbitdb, shell=True).decode()
    if ps_orbitdb_results != "":
        kill_orbitdb = 'kill -9 ' + ps_orbitdb_results
        kill_orbitdb_results = subprocess.check_output(kill_orbitdb, shell=True).decode()

    ps_ipfs = "ps aux | grep ipfs | grep -v grep | awk \'{print $2}\' "
    ps_ipfs_results = subprocess.check_output(ps_ipfs, shell=True).decode()
    if ps_ipfs_results != "":
        kill_ipfs = 'kill -9 ' + ps_ipfs_results
        kill_ipfs_results = subprocess.check_output(kill_ipfs, shell=True).decode()
        

if __name__ == "__main__":
    asyncio.run(run())