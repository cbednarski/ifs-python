from setuptools import setup

setup(
    name='ifs',
    version='0.11.0',
    author='Chris Bednarski',
    author_email='banzaimonkey@gmail.com',
    url='https://github.com/cbednarski/ifs',
    description='Install from source',
    license='ISC',
    packages=['ifs', 'ifs.source'],
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
