from setuptools import setup,find_packages

setup(
    name='cc4p38_1',
    version='0.1',
#    packages=['cc4p38_1pkg'],
    packages=find_packages(where='src'),
    package_data={  # Optional
        'sample': ['stock_data.json'],
    },
    package_dir={'': 'src'},
    url='https://github.com/itsaint/cc4p38_1/',
    license='',
    author='itsaint',
    author_email='itsaint@gmail.com',
    description='cc4 '
)
