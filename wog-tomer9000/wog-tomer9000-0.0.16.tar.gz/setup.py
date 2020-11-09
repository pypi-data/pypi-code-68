import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wog-tomer9000",
    version="0.0.16",
    author="Tomer_Tzur",
    author_email="tomer9000@gmail.com",
    description="Package for DevOps course",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tomer9000/WOG",
    packages=setuptools.find_packages(),
    install_requires=['inputimeout', 'requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
