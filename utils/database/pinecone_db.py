import pinecone

from constants import PINECONE_API_KEY, PINECONE_API_ENV

from functools import cache


def setup_pinecone():
    pinecone.init(
        api_key=PINECONE_API_KEY,
        environment=PINECONE_API_ENV,
    )


class PineconeDB:

    def __init__(self):
        pinecone.init(
            api_key=PINECONE_API_KEY,
            environment=PINECONE_API_ENV,
        )

    @property
    @cache  # FIX: can cause problems
    def index_list(self):
        return pinecone.list_indexes()

    # Function to creat a new Index, default dimension is 1536 and default metric is "euclidean"
    def create_index(self, index_name, dimension=1536, metric="euclidean"):
        # get the latest indexes list from server

        # check before creating
        if index_name not in self.index_list:
            # index not existed. Create a new index
            pinecone.create_index(name=index_name, dimension=dimension, metric=metric)
            print(f"create a new index {index_name}")
        else:
            print(f"{index_name} index existed. skip creating.")
