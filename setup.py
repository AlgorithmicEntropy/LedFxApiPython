from setuptools import setup

# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='LedFxAPI',
    packages=['LedFxAPI'],
    version='0.0.2',
    license='MIT',
    description='Python API for LedFx',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Sebastian Wallat',
    author_email='wallatsebastian@gmail.com',
    url='https://github.com/AlgorithmicEntropy/LedFxApiPython',
    download_url='https://github.com/AlgorithmicEntropy/LedFxApiPython/releases/tag/v0.0.2.tar.gz',
    keywords=['FX', 'LedFx', 'Local', 'API'],
    install_requires=[
        'requests', 'urllib3'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
)
