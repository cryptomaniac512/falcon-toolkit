from setuptools import setup

setup(
    author='Nikita Sivakov',
    author_email='cryptomaniac.512@gmail.com',
    classifiers=[
        "Framework :: Pytest",
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Testing',
    ],
    description='Collection of utils for the Falcon Framework',
    entry_points={
        'pytest11': [
            'falcon-toolkit = falcon_toolkit.pytest.fixtures',
        ],
    },
    install_requires=['pytest>=3.4.0', 'falcon>=1.4.0'],
    keywords=['pytest', 'fixtures', 'falcon', 'client', 'api'],
    license='MIT',
    long_description_markdown_filename='README.md',
    name='falcon-toolkit',
    packages=['falcon_toolkit'],
    python_requires='>=3.4',
    setup_requires=['setuptools-markdown', 'pytest-runner'],
    tests_require=['pytest'],
    url='https://github.com/cryptomaniac512/falcon-toolkit',
    version='0.0.1',
)
