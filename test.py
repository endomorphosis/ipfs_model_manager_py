import asyncio
from ipfs_model_manager import ipfs_model_manager
model_manager = ipfs_model_manager()
asyncio.run(model_manager.run_once())
print('done running test.py')
