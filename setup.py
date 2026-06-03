from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function returns the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines();
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

#metadata about the entire project
setup(
    name='mlproject',
    version='0.0.1',
    author='Hanan',
    author_email='mdhanansjd@gmail.com',
    packages=find_packages(), #find all the packages in the project and include them in the distribution
    install_requires=get_requirements('requirements.txt'), #get the list of dependencies from the requirements.txt file

)