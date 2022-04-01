from setuptools import setup

# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='LedFxAPI',
    packages=['LedFxAPI'],
    version='0.0.1',
    license='MIT',
    description='API wrapper for LedFx API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Sebastian Wallat',
    author_email='wallatsebastian@gmail.com',
    url='https://github.com/',
    download_url='https://github.com/SebastianWallat/SolarWattEnergyManagerAPI/archive/v_053.tar.gz',
    keywords=['IOT', 'Solar', 'Local'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)