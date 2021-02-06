import pathlib
import setuptools, os
 
# The directory containing this file
HERE = pathlib.Path(__file__).parent
 
# The text of the README file
README = (HERE / "README.md").read_text()
 
# Pull requirements from the text file
requirement_path = (HERE / 'requirements.txt')
install_requires = []
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()
 
# This call to setup() does all the work
setuptools.setup(
    name="osc_client",
    version="0.0.1",
    description="A Python client for OpenStreetCam.org (OSC) API utilization.",
    long_description=README,
    long_description_content_type="text/markdown",
    author="d33bs",
    author_email="d33bs@users.noreply.github.com",
    license="Apache 2.0",
    keywords="osc openstreetcam streetview roadview api requests",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(where='src'),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=install_requires,
)