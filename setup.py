from setuptools import setup, find_packages
from typing import List

hyphen_dot_e = '-e .'

def get_requirements(file: str) -> List[str]:
    requirements = []
    with open(file) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if hyphen_dot_e in requirements:
            requirements.remove(hyphen_dot_e)
    return requirements

setup(
    name='ML-Model-Deployment',
    version='0.1',
    author='AJ Parker',
    author_email='trueajparker@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)