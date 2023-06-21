import pinecone
from ..load_env import get_key

class PineconeDB:
    # Index list get from database
    index_list = []

    def __init__(self):
        # get required API keys to init database
        pinecone.init(
            api_key=get_key("PINECONE_API_KEY"),
            environment=get_key("PINECONE_API_ENV")
        )
        print('inside class PineconeDB. initializing...')
        #self.get_indexes()

    # Function to get existed API keys.
    def get_indexes(self):
        self.index_list = pinecone.list_indexes()
        return self.index_list

    # Function to creat a new Index, default dimension is 1536 and default metric is "euclidean"
    def create_index(self, index_name, dimension=1536, metric="euclidean"):
        # get the latest indexes list from server
        self.get_indexes()
       
       # check before creating
        if index_name not in self.index_list:
            # index not existed. Create a new index
            pinecone.create_index(name=index_name, dimension=dimension, metric=metric)
            print(f"create a new index {index_name}")
        else:
            print(f"{index_name} index existed. skip creating.")
