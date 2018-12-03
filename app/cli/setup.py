from setuptools import setup

setup(
    name='cli',
    version='1.0',
    py_modules=['app'],
    install_requires=[
	'Click',
	'Flask',
	'requests',
	'slackclient',
    'redis',
    ],
    entry_points='''
        [console_scripts]
        cli=app:hello
    ''',
)
