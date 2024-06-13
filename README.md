IPFS Huggingface Bridge:

for huggingface transformers python library visit:
https://github.com/endomorphosis/ipfs_transformers/

for huggingface datasets python library visit:
https://github.com/endomorphosis/ipfs_datasets/

for transformers.js visit:                          
https://github.com/endomorphosis/ipfs_transformers_js

for orbitdb_kit nodejs library visit:
https://github.com/endomorphosis/orbitdb_kit/

for python model manager library visit: 
https://github.com/endomorphosis/ipfs_model_manager/

for nodejs model manager library visit: 
https://github.com/endomorphosis/ipfs_model_manager_js/

for nodejs ipfs huggingface scraper with pinning services visit:
https://github.com/endomorphosis/ipfs_huggingface_scraper/

for ipfs agents visit:
https://github.com/endomorphosis/ipfs_huggingface_scraper/

for ipfs accelerate visit:
https://github.com/endomorphosis/ipfs_accelerate/

Author - Benjamin Barber
QA - Kevin De Haan

# About

This is a model manager and wrapper for huggingface, looks up a index of models from an collection of models, and will download a model from either https/s3/ipfs, depending on which source is the fastest.

# How to use
~~~shell
pip install .
~~~

look run ``python3 example.py`` for examples of usage.

this is designed to be a drop in replacement, which requires only 2 lines to be changed

In your python script
~~~shell
from ipfs_kit import ipfs_kit
from orbitdb_kit import orbitdb_kit 
from ipfs_model_manager import ipfs_model_manager as model_manager
from ipfs_model_manager import load_config()
from ipfs_model_manager import load_collection()
config = load_config()
collection = load_collection()
models = ModelManager()
ready = models.ready()
models.import_config(config)
models.import_collection(collection)
models.state()
~~~

or 

~~~shell
from ipfs_kit import ipfs_kit
from orbitdb_kit import orbitdb_kit 
from ipfs_model_manager import ipfs_model_manager as model_manager
from ipfs_model_manager import load_config()
from ipfs_model_manager import load_collection()
config = load_config()
config.s3cfg = {
        "bucket": "cloud",
        "endpoint": "https://storage.googleapis.com",
        "secret_key": "",
        "access_key": ""
    }
collection = load_collection()
models = ModelManager()
ready = models.ready()
models.import_config(config)
models.import_collection(collection)
models.state()
~~~

~~~
