#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import os
import sys

import yaml
from genson import SchemaBuilder
from json_schema_for_humans.generate import generate_from_filename
from json_schema_for_humans.generation_configuration import GenerationConfiguration

from annotations import DESCRIPTION, TITLE
from configuration import CONFIG_JSON, CONFIG_YML, DOCS_PATH, SCHEMA_PATH, USE_ANNOTATIONS, VERBOSE, DESCRIPTION_PLACEHOLDER


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Generate HTML documentation for YAML files.")
    if (len(sys.argv)) == 1:
        parser.print_help()

    parser.add_argument("-p", "--preview",
                        dest="preview",
                        action='store_true',
                        required=False,
                        help="Generates documentation from YAML with description placeholders.")
    parser.add_argument("-s", "--schema",
                        dest="schema",
                        action='store_true',
                        required=False,
                        help="Generates schema from YAML with description placeholders.")
    parser.add_argument("-d", "--docs",
                        dest="docs",
                        action='store_true',
                        required=False,
                        help="Generates documentation from schema.")

    args: argparse.Namespace = parser.parse_args()

    if (args.preview is True or args.schema is True):
        yml_to_json(CONFIG_YML, CONFIG_JSON, VERBOSE)

        addDescriptionPlaceholder : bool = (args.preview is True)

        generate_json_schema(CONFIG_JSON,
                             SCHEMA_PATH, addDescriptionPlaceholder, USE_ANNOTATIONS, VERBOSE)

    if (args.preview is True or args.docs is True):
        generate_docs(SCHEMA_PATH, DOCS_PATH, VERBOSE)


def generate_docs(inputPath: str, outputPath: str, verbose: bool = False) -> None:
    config: GenerationConfiguration = GenerationConfiguration(
        copy_css=False, expand_buttons=True, description_is_markdown=True)

    generate_from_filename(inputPath, outputPath, config=config)

    if (verbose):
        print("Saved docs to path: " + outputPath)


def generate_json_schema(inputPath: str, outputPath: str, addDescriptionPlaceholder : bool = False, useAnnotations: bool = False, verbose: bool = False) -> None:

    if (verbose):
        print("Loading JSON file from path: " + inputPath)

    jsonObj = json.load(open(inputPath))

    if (verbose):
        print("Generating schema")

    builder: SchemaBuilder = SchemaBuilder()
    builder.add_object(jsonObj)
    schema: dict = builder.to_schema()

    if (addDescriptionPlaceholder):
        add_description_property(schema)  # type: ignore

    if (useAnnotations):
        schema["title"] = TITLE
        schema["description"] = DESCRIPTION

    with open(outputPath, 'w') as json_file:
        json.dump(schema, json_file, indent=4)

    if (verbose):
        print("Saved schema to path: " + outputPath)


def add_description_property(d: dict) -> None:
    if ("type" in d):
        d["description"] = DESCRIPTION_PLACEHOLDER
    for key, value in d.items():
        if (type(value) == dict):
            add_description_property(value)


def yml_to_json(inputPath: str, outputPath: str, verbose: bool = False) -> None:

    if (verbose):
        print("Reading YAML file from path: " + inputPath)

    with open(inputPath, 'r') as file:
        configuration = yaml.safe_load(file)

    if (verbose):
        print("Saving JSON file to path: " + outputPath)

    with open(outputPath, 'w') as json_file:
        json.dump(configuration, json_file, indent=4)

    if (verbose):
        output: str = json.dumps(json.load(open(outputPath)), indent=4)
        print(output)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Cancelled by user.')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    except Exception as ex:
        print('ERROR: ' + str(ex))
        try:
            sys.exit(1)
        except SystemExit:
            os._exit(1)
