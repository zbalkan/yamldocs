from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description: str = fh.read()

setup(
    name="yamldocs",
    version="0.1.0",
    packages=find_packages(),
    description="tl;dr: JavaDoc or doxygen for YAML.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zbalkan/yaml-docs",
    author="Zafer Balkan",
    author_email="zafer@zaferbalkan.com",
    license="MIT",
    classifiers=[
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
    ],
    install_requires=[
        "autopep8 >= 1.7.0",
        "certifi >= 2022.9.24",
        "charset-normalizer >= 2.1.1",
        "click >= 8.1.3",
        "colorama >= 0.4.5",
        "dataclasses-json >= 0.5.7",
        "genson >= 1.2.2",
        "htmlmin >= 0.1.12",
        "idna >= 3.4",
        "Jinja2 >= 3.1.2",
        "json-schema-for-humans >= 0.41.8",
        "markdown2 >= 2.4.5",
        "MarkupSafe >= 2.1.1",
        "marshmallow >= 3.18.0",
        "marshmallow-enum >= 1.5.1",
        "mypy-extensions >= 0.4.3",
        "packaging >= 21.3",
        "pycodestyle >= 2.9.1",
        "Pygments >= 2.13.0",
        "pyparsing >= 3.0.9",
        "pytz >= 2021.3",
        "PyYAML >= 6.0",
        "requests >= 2.28.1",
        "toml >= 0.10.2",
        "typing-inspect >= 0.8.0",
        "typing_extensions >= 4.4.0",
        "urllib3 >= 1.26.12",

    ],
)
