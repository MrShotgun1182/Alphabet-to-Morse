from os import system
import click
def json_reader(file: str) -> dict:
    import json

    with open(file) as f:
        dictionary = json.load(f)
    return dictionary

        
