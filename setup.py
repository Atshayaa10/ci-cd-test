from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="calculator",
    version="1.0",
    description="A simple calculator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your@email.com",
    packages=["calculator"],
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)