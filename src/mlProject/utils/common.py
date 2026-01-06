#Common functions for the project


import yaml
from box import ConfigBox
from src.mlProject import logger
from ensure import ensure_annotations
from box.exceptions import BoxValueError




file_path = r"E:\projects\TrainingFPDModel\End-to-End-ML-Pipeline\datasets\V1\data_fixed.yaml"
# config_data = read_yaml_file(file_path)/print(f"First User Name: {config_data['users'][0]['name']}")

@ensure_annotations #ensure that the function adheres to the specified type annotations & raises errors if not
def read_yaml_file(filepath) -> ConfigBox: #CongiBox is a dictionary like object that allows access via dot notation
    try:
        with open(filepath, 'r') as file:
            data = yaml.safe_load(file)
            logger.info(f"YAML file '{filepath}' read successfully.")
            return ConfigBox(data)
    except BoxValueError: #Raised when trying to access a non-existent key in a Box object
       raise ValueError(f"The file '{filepath}' is empty.")
    except Exception as e:
        logger.error(f"Error reading YAML file '{filepath}': {e}")
        raise e
