from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Team2_Functions',
    long_description=open('README.md').read(),
    install_requires=['numpy','pandas'],
    url='https://github.com/teamCEKTA/Eskom_staege_2',
    author='Team_2',
    author_email='eltonmaepa7@gmail.com'
)