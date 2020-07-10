import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="KMeansImage", # Replace with your own username
    version="0.69",
    author="Sahil",
    author_email="sahils.1997.s@gmail.com",
    description="A K-Means based image compressor. Consists interactive widgets for Jupyter Notebook",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
