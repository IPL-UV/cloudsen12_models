from setuptools import setup, find_packages
import codecs
import os.path

with open("README.md", "r") as fh:
    long_description = fh.read()


def parse_requirements_file(filename):
    with open(filename, encoding="utf-8") as fid:
        requires = [l.strip() for l in fid.readlines() if l]
    return requires


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(name="cloudsen12_models",
      version=get_version("cloudsen12_models/__init__.py"),
      author="Cesar Aybar, Gonzalo Mateo-Garcia",
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=find_packages(".", exclude=["tests"]),
      description="Lightweight code to run inference with CloudSEN12 models",
      install_requires=parse_requirements_file("requirements.txt"),
      url="https://github.com/IPL-UV/cloudsen12_models",
      classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering :: GIS",
        "Development Status :: 5 - Production/Stable", 
    ],
      keywords=["raster reading", "rasterio"],
)
