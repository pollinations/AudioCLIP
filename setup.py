import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AudioCLIP",
    version="0.0.1",
    author="AndreyGuzhov",
    author_email="",
    description="AudioCLIP pip installable",
    long_description=long_description,
    url="https://github.com/pollinations/AudioCLIP",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
