from os import system
import click
def json_reader(file: str) -> dict:
    import json

    with open(file) as f:
        dictionary = json.load(f)
    return dictionary

def changer():
    text = str()
    char = str()
    dictionary = json_reader("dictionary.json")
    while(char != '-'):
        system('cls')
        print(text)
        char = click.getchar()
        char = char.upper()
        text += dictionary[char] + ' '


def main():
    changer()

if __name__ == "__main__":
    main()
        
