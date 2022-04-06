from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in custom/__init__.py
from custom import __version__ as version

setup(
	name="custom",
	version=version,
	description="it is for custom system ",
	author="Rida`a",
	author_email="info@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
