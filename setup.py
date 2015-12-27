from setuptools import setup, find_packages

setup(
    name='yarh',
    version='0.2', #phase2
    description='Yet Another Rough HTML',
    #long_description=long_description,
    url='https://github.com/minacle/yarh',
    author='Mayu Laierlence',
    author_email='minacle@live.com',
    license='BSD',
    classifiers=[ # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='yarh html',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'yarh=yarh.__main__',
        ],
    },
)
