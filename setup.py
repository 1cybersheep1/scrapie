# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('scrapie/scrapie.py').read(),
    re.M
    ).group(1)


#with open("README.rst", "rb") as f:
#    long_descr = f.read().decode("utf-8")


setup(
    name = "scrapie",
    packages = ["scrapie"],
    entry_points = {
        "console_scripts": ['scrapie = scrapie.scrapie:main']
        },
    version = version,
    description = "",
    #long_description = long_descr,
    author = "Andre Alves",
    author_email = "andre.marques.alves@gmail.com",
    url = "https://pypi.org/project/scrapie/",
    )
