#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import sys

from annotations import Annotations
from configuration import Configuration
from generator import DocumentGenerator


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

    an: Annotations = Annotations()
    config: Configuration = Configuration()

    generator: DocumentGenerator = DocumentGenerator(
        title=an.TITLE, description=an.DESCRIPTION, descriptionPlaceholder=an.DESCRIPTION_PLACEHOLDER)

    if (args.preview is True or args.schema is True):
        generator.yml_to_json(
            config.CONFIG_YML, config.CONFIG_JSON, config.VERBOSE)

        addDescriptionPlaceholder: bool = (args.preview is True)

        generator.generate_json_schema(inputPath=config.CONFIG_JSON,
                                       outputPath=config.SCHEMA_PATH, addDescriptionPlaceholder=addDescriptionPlaceholder, verbose=config.VERBOSE)

    if (args.preview is True or args.docs is True):
        generator.generate_docs(inputPath=config.SCHEMA_PATH,
                                outputPath=config.DOCS_PATH, verbose=config.VERBOSE)


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
