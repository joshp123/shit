from setuptools import setup

setup(
    name='shit',
    version='0.1',
    description='shouty git',
    url='https://github.com/joshp123/shit/',
    author='Josh Palmer',
    license='MIT',
    entry_points = {
        'console_scripts': [
            'SHIT = shit:main'
        ]
    }
)
