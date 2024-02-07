# JSON Documents Vector Search API

This is a simple API for vector similarity search built with FastAPI. It uses a JSONVectorSearch database utility for storing and querying vector embeddings. 

## Endpoints

- `POST /create` - Creates a new empty collection by calling `db.clean()`
- `POST /add` - Adds documents to the collection. Takes a list of `ids`, `documents`, and optional `metadatas`. Calls `db.add()` to index them.  
- `POST /query` - Searches the collection. Takes a `query` string and number of `n_results` to return. Calls `db.query_str()` and returns the results.
- `DELETE /clean` - Deletes all documents in the collection by calling `db.clean()`.

## Usage 

The `documents` passed to `/add` should be dictionaries containing a `"vector"` key with the vector embedding to index.

The `query` string passed to `/query` will be converted to a vector using the same process as indexing, and a similarity search performed to find the closest matching vectors.

The API expects vectors of fixed size for a given collection.

## Requirements

- FastAPI
- Pydantic

## Database 

The `JSONVectorSearch` database utility handles storing the indexed vectors and metadata in JSON files. It provides methods for adding, cleaning, and querying the collection.

The vector search is approximate, optimized for speed over accuracy. The database is kept in-memory for low latency queries, but not persisted across restarts.

## Next Steps

- Add persistence for the database  
- Improve vector search accuracy
- Add more query options like filtering and faceting
- Containerize with Docker for easy deployment