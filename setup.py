from setuptools import setup

setup(
	name='ipfs_model_manager',
	version='0.0.2',
	packages=[
		'ipfs_model_manager',
	],
	install_requires=[
        'ipfs_kit@git+https://github.com/endomorphosis/ipfs_kit.git',
        'orbitdb_kit@git+https://github.com/endomorphosis/orbitdb_kit.git',
		'datasets',
		'urllib3',
		'requests',
		'boto3',
        'toml',
	]
)