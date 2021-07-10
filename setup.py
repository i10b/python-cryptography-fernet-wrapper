import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-cryptography-fernet-wrapper",
    version="1.0.4",
    author="krazykirby99999",
    description="A wrapper for cryptography.fernet",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KrazyKirby99999/python-cryptography-fernet-wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "cryptography"
    ]
)