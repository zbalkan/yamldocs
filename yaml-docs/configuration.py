#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

ROOT: str = os.path.dirname(os.path.realpath(__file__))


class Configuration:

    CONFIG_YML: str = f"{ROOT}/input/defaults.yml"
    CONFIG_JSON: str = f"{ROOT}/input/defaults.json"
    SCHEMA_PATH: str = f"{ROOT}/schema/defaults.schema.json"
    DOCS_PATH: str = f"{ROOT}/output/defaults.html"
    VERBOSE: bool = True
    USE_ANNOTATIONS: bool = True
