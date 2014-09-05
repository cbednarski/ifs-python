from setuptools import setup, find_packages

setup(
    name='ifs',
    version='0.2.0',
    description='Install from source',
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
