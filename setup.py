import os

from setuptools import setup


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as _f:
        return _f.read()


setup(
    author="Nikita Sivakov",
    author_email="sivakov512@gmail.com",
    classifiers=[
        "Framework :: Pytest",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Testing",
    ],
    description="Pytest `client` fixture for the Falcon Framework",
    entry_points={"pytest11": ["pytest-falcon-client = pytest_falcon_client"]},
    keywords=["pytest", "fixture", "falcon", "client", "api"],
    license="MIT",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    name="pytest-falcon-client",
    modules=["pytest_falcon_client"],
    python_requires=">=3.6",
    install_requires=["pytest>=4.3", "falcon>=1.4"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    url="https://github.com/sivakov512/pytest-falcon-client",
    version="2.0.0",
)
