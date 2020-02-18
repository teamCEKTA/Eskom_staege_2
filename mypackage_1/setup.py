from setuptools import setup, find_packages

setup(
    name='Team_2 Predict',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA Stage2 Predict',
    long_description=open('README.md').read(),
    install_requires=['numpy','pandas'],
    url='https://github.com/<username>/<package-name>',
    author='<Team_2>',
    author_email='keithtakarinda@gmail.com'
)