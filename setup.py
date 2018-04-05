from setuptools import setup

setup(
    name='python-mojang-api-cli',
    version='1.0.0',
    py_modules=['cli'],
    install_requires=[
        'Click',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        mclookup=cli:main
    ''',
    url='https://github.com/Pixelhash/python-mojang-api-cli',
    license='MIT',
    author='CodeHat',
    author_email='dev@codehat.de',
    description='A simple Python Cli to communicate with the Mojang API.'
)
