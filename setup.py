from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return all the requirements 
    """

    requirements_lst: List[str] = []

    try:
        with open("requirements.txt", 'r') as file:
            # Reading all lines
            lines = file.readlines()
            # processing each line
            for line in lines:
                requirement = line.strip()

                if requirement and requirement != '-e .':
                    requirements_lst.append(requirement)

    except FileNotFoundError:
        print("Require a 'requirements.txt' file!!!")
    
    return requirements_lst

setup(
    name="RaceIntel",
    version="0.0.1",
    author="Venkatesh Munaga",
    author_email="munagavenkatesh02@gmail.com",
    packages=find_packages(),
    install_require=get_requirements()
)