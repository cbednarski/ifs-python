from setuptools import setup, find_packages

setup(
    name='ifs',
    version='0.7.1',
    author='Chris Bednarski',
    author_email='banzaimonkey@gmail.com',
    url='https://github.com/cbednarski/ifs',
    description='Install from source',
    license='ISC',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'colorama'
    ],
    entry_points='''
        [console_scripts]
        ifs=ifs.cli:cli
    '''
)
