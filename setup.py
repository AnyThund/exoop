import setuptools

from exoop import __author__, __email__, __version__, __description__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="exoop", # Replace with your own username
    version=__version__,
    author=__author__,
    author_email=__email__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/AnyThund/exoop",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'exoop = exoop.command:main',
        ]
    },
    license='MIT',
)
