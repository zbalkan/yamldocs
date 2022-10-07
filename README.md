# YAML Configuration Documentation

A naive approach to generate documentation from YAML files which can be integrated into CI-CD pipeline. In short, JavaDoc or doxygen for YAMl.

The `defaults.yml` file used as an example is extracted from OpenSearch configuration.

## Usage

* `git clone` the repository.
* Copy the YAML file under `docs/` directory.
* Update `configuration.py` based on your requirements.
* Run `pip install -r requirements.txt`
* Run `python3 doc_generator.py`
* PROFIT

## Generated docs

The documentation is under `./docs` directory. Under screenshots, ou can get both partial and full views.

![Sample screenshot](./screenshots/partial.png)

## Reference

The POC is based on the ideas in the issue [214](https://github.com/opensearch-project/documentation-website/issues/214)
