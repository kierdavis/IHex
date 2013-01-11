from setuptools import setup

setup(
  name = "IHex",
  version = "0.1.4",
  py_modules = ["ihex"],

  author = "Kier Davis",
  author_email = "kierdavis@gmail.com",
  description = "A Python library for reading and writing Intel Hex files",
  url = "https://github.com/kierdavis/IHex",
  keywords = "intel hex binary files",
  test_suite = 'test_ihex',
  classifiers = ["Programming Language :: Python",
      "License :: Public Domain",
      "Operating System :: OS Independent",
      "Topic :: Software Development :: Libraries :: Python Modules"],
)
