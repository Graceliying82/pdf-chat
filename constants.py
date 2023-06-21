from typing import Final

from os import environ

from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY: Final[str] = environ["PINECONE_API_KEY"]
PINECONE_API_ENV: Final[str] = environ["PINECONE_API_ENV"]
OPENAI_API_KEY: Final[str] = environ["OPENAI_API_KEY"]
INDEX_NAME: Final[str] = 'chatgpt'
