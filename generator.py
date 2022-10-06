import os
import sys

from json_schema_for_humans.generate import generate_from_filename
from json_schema_for_humans.generation_configuration import \
    GenerationConfiguration

SOURCE_PATH: str = "./schema"
DOCS_PATH: str = "./docs/defaults.html"


def main() -> None:
    config: GenerationConfiguration = GenerationConfiguration(
        copy_css=False, expand_buttons=True, description_is_markdown=False)
    generate_from_filename(SOURCE_PATH, DOCS_PATH, config=config)


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
