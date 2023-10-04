from setuptools import setup

setup(
    name='ffconverter',
    version='0.1',
    description='File Format Converter',
    url='https://github.com/RajaniDharmaram/File-Format-Converter',
    author='Rajani Dharmaram',
    author_email='rajanidharmaram03@gmail.com',
    license='MIT',
    packages=['ffconverter'],
    install_requires=[
          'pandas<=2.1.1',
      ],
    entry_points = {
        'console_scripts': ['ffconverter=ffconverter:main'],
    },  
    zip_safe=False
)
