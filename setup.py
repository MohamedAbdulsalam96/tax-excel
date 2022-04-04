from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tax_excel/__init__.py
from tax_excel import __version__ as version

setup(
	name="tax_excel",
	version=version,
	description="Custom integration to enhenance multi location multi manager reporfor different categories",
	author="Jide Olayinka",
	author_email="spryng.managed@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
