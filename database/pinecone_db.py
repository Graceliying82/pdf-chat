import logging
from typing import List

import pinecone
from icecream import ic

from constants import PINECONE_API_KEY, PINECONE_API_ENV


# from functools import cache


# @cache
def index_list() -> List[str]:
    return pinecone.list_indexes()


def _setup() -> None:
    print('Init pinecone database')
    pinecone.init(
        api_key=PINECONE_API_KEY,
        environment=PINECONE_API_ENV,
    )

    ic(f"pinecone-setup:{index_list()}")


def create_index(index_name: str, dimension: int = 1536, metric: str = "euclidean"):
    # check before creating
    if index_name not in index_list():
        # index not existed. Create a new index
        pinecone.create_index(name=index_name, dimension=dimension, metric=metric)
        ic(f"create a new index {index_name}")
    else:
        logging.warning(f"{index_name} index existed. skip creating.")


_setup()

# class PineconeDB:
#     __slots__ = []  # Perf: debug
#
#     def __init__(self):
#         pinecone.init(
#             api_key=PINECONE_API_KEY,
#             environment=PINECONE_API_ENV,
#         )
#
#     @property
#     @cache
#     def index_list(self,cached:int=0): #use any other number to get the latest
#         return pinecone.list_indexes()
