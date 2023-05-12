from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in testapp/__init__.py
from testapp import __version__ as version

setup(
	name="testapp",
	version=version,
	description="no",
	author="jagan",
	author_email="asp@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
