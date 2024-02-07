import json
import chromadb
from typing import List

class JSONVectorSearch:

    def __init__(self, name='json_db') -> None:
        self.chroma_client = chromadb.Client()
        self.collection = self.chroma_client.create_collection(name=name)

    def add(self, ids:List[str], documents:List[dict], metadatas:List[dict]=None):
        assert len(ids) == len(documents)
        if metadatas is None:
            metadatas = [{}]*len(ids)
        assert len(metadatas) == len(documents)

        jsons_str = [json.dumps(doc) for doc in documents]

        self.collection.add(
            documents=jsons_str,
            metadatas=metadatas,
            ids=ids
        )

    def query_str(self, query:str, n_results=1):
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )

        n_res = len(results['ids'])

        output = []
        for k in range(n_res):
            output.append(dict(
                id=results['ids'][k],
                distance=results['distances'][k],
                data=json.loads(results['documents'][k]),
                metadata=json.upresults['metadatas'][k],
            ))
        
        return output
    
    def query_json(self, data:dict, n_results=1):
        
        return self.query_str(
            query=json.dumps(data),
            n_results=n_results
        )

    def clean(self):
        self.collection.delete()