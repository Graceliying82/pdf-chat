import os
from dotenv import load_dotenv
from dotenv import find_dotenv

def get_key(key_name):
    # Load the environment variables from the .env file
    load_dotenv()

    # Print out your .env file path. Please keep your .env file at the same level with your app.py 
    print(find_dotenv())

    # Get API keys by name
    key = os.getenv(key_name)
    if key:
        print(f"key {key_name} found!")
    else:
        raise ValueError(f"Required API KEY {key_name} NOT FOUND!")
    return key
    