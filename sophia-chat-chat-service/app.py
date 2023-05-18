from flask import Flask, request, jsonify
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

@app.route('/index/<collection_name>', methods=['POST'])
def get_answer(collection_name):
    data = request.get_json()

    query = data.get("query")
    if query is None:
        return jsonify({"error": "Please provide 'query'"}), 400

    vector_store = QdrantVectorStore(
        client=client,
        collection_name=collection_name,
    )
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    index = GPTVectorStoreIndex.from_documents([], storage_context=storage_context)
    query_engine = index.as_query_engine()
    response = query_engine.query(query)

    return jsonify({"response": response}), 200

if __name__ == '__main__':
    app.run()