from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    requirement_list:List[str] = []

    return requirement_list

setup(
    name = "flipkart",
    version = "0.0.1",
    author = "abhi142s",
    author_email = "abhinandan96is@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)
