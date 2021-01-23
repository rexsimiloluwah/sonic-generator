import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="sonic-generator",
    version="1.1.5",
    description="Automatically generate starter template for your FastPI projects in a jiffy.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/rexsimiloluwah/sonic-generator",
    author="Similoluwa Okunowo",
    author_email="rexsimiloluwa@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["sonic"],
    include_package_data=True,
    install_requires=["fastapi", "aiofiles", "pydantic", "uvicorn", "PyYAML", "jinja2", "colorama"],
    entry_points={
        "console_scripts": [
            "sonicgenerator=sonic.__main__:main",
        ]
    },
)