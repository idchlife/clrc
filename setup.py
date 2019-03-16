import setuptools


with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="clrc",
  version="0.0.3",
  author="Igor Andreev",
  author_email="idchlife@gmail.com",
  description="Easy to use console prints with colors. clrc.info(), clrc.success() etc",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/idchlife/clrc",
  packages=setuptools.find_packages(),
  install_requires=[
    "colorama==0.4.1"
  ],
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
  ]
)