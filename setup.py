from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pyweidentity',
    version='1.0',
    description="weidentity python sdk",
    author=["huifeng", "leeduckgo"],
    author_email='1290017556@qq.com',
    url="https://github.com/SUIBE-Blockchain/Weidentity-Python-SDK",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests",
        "eth_account",
        "ecdsa"
    ]
)