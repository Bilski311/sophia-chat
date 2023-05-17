from flask import Flask, request
from qdrant_client import QdrantClient
from llama_index.vector_stores import QdrantVectorStore
from llama_index import GPTVectorStoreIndex, StorageContext, Document

app = Flask(__name__)
client = QdrantClient("http://localhost:6333")

@app.route('/file', methods=['POST'])
def upload_file():
    file = request.files['file']
    vector_store = QdrantVectorStore(
        client=client,
        collection_name=file.name,
    )
    storage_context = StorageContext.from_defaults(
        vector_store = vector_store
    )
    text = file.read().decode()
    index = GPTVectorStoreIndex.from_documents([Document(text)], storage_context=storage_context)

    return 'File uploaded successfully'

@app.route('/index', methods=['GET'])
def get_index():
    vector_store = QdrantVectorStore(
        client=client,
        collection_name="file",
    )
    storage_context = StorageContext.from_defaults(
        vector_store = vector_store
    )
    index = GPTVectorStoreIndex.from_documents([], storage_context=storage_context)
    query_engine = index.as_query_engine()
    response = query_engine.query("Who is Dominik Bilski?")
    print(response)

    return 'Success'

if __name__ == '__main__':
    app.run()