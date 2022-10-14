import json
from pathlib import Path

class json_dict(dict.__dict__.__class__):
    """
    json_dict(json_file_path) -> dictionary dict(mapping) -> new dictionary
    initialized by mapping JSON file content
      (key, value) pairs
    Extract dictionary object from the given JSON file.
    If it is not, then an UnexpectedException is thrown.
    :Args:
        - json_file_path - path to the JSON file -> str
    Example:
        from extract_dict import json_dict
        dictionary = json_dict('./file.json')
    """
    def __init__(self, json_file_path: str) -> dict.__dict__.__class__:  # type: ignore
        """
        Constructor. An extract dictionary object from the given JSON file.
        If it is not, then an UnexpectedException is thrown.
        :Args:
         - json_file_path - path to the JSON file -> str
        Example:
            from extract_dict import json_dict
            dictionary = json_dict('./file.json')
        """
        with open(Path(json_file_path)) as reader:
            json_content = json.load(reader)
            return json_content