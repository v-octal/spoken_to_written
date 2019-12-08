from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='spoken_to_written',
    version='0.1',
    description='A module to convert text from a speech recognition system to written format.',
    license="MIT",
    long_description=long_description,
    author='Vikas Rajput',
    author_email='vikasrajput.official@gmail.com',
    packages=['spoken_to_written'],
    install_requires=['word2number'],
    include_package_data=True,
    package_dir={'spoken_to_written': 'spoken_to_written'},
    package_data={'spoken_to_written': ['conversion_rules.json']}
)
