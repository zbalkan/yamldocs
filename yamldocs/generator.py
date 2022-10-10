import json
import os

import yaml
from genson import SchemaBuilder
from json_schema_for_humans.generate import generate_from_filename
from json_schema_for_humans.generation_configuration import GenerationConfiguration


class DocumentGenerator():

    __title: str
    __description: str
    __descriptionPlaceholder: str

    def __init__(self, title: str, description: str, descriptionPlaceholder: str) -> None:
        self.__title = title
        self.__description = description
        self.__descriptionPlaceholder = descriptionPlaceholder

    def generate_docs(self, inputPath: str, outputPath: str, verbose: bool = False) -> None:

        __inputPath: str = os.path.abspath(inputPath)
        __outputPath: str = os.path.abspath(outputPath)

        if (verbose):
            print("Loading JSON schema from path: " + __inputPath)

        config: GenerationConfiguration = GenerationConfiguration(
            copy_css=False, expand_buttons=True, description_is_markdown=True)

        generate_from_filename(__inputPath, __outputPath, config=config)

        if (verbose):
            print("Saved docs to path: " + __outputPath)

    def generate_json_schema(self, inputPath: str, outputPath: str, addDescriptionPlaceholder: bool = False, verbose: bool = False) -> None:

        __inputPath: str = os.path.abspath(inputPath)
        __outputPath: str = os.path.abspath(outputPath)

        if (verbose):
            print("Loading JSON file from path: " + __inputPath)

        jsonObj = json.load(open(__inputPath))

        if (verbose):
            print("Generating schema")

        builder: SchemaBuilder = SchemaBuilder()
        builder.add_object(jsonObj)
        schema: dict = builder.to_schema()

        if (addDescriptionPlaceholder):
            self.add_description_property(schema)  # type: ignore

        schema["title"] = self.__title
        schema["description"] = self.__description

        with open(__outputPath, 'w') as json_file:
            json.dump(schema, json_file, indent=4)

        if (verbose):
            print("Saved schema to path: " + __outputPath)

    def add_description_property(self, d: dict) -> None:
        if ("type" in d):
            d["description"] = self.__descriptionPlaceholder
        for key, value in d.items():
            if (type(value) == dict):
                self.add_description_property(value)

    def yml_to_json(self, inputPath: str, outputPath: str, verbose: bool = False) -> None:
        __inputPath: str = os.path.abspath(inputPath)
        __outputPath: str = os.path.abspath(outputPath)

        if (verbose):
            print("Reading YAML file from path: " + __inputPath)

        with open(__inputPath, 'r') as file:
            configuration = yaml.safe_load(file)

        if (verbose):
            print("Saving JSON file to path: " + __outputPath)

        with open(__outputPath, 'w') as json_file:
            json.dump(configuration, json_file, indent=4)

        if (verbose):
            print("Saved JSON file to path: " + __outputPath)
