import chromadb
client = chromadb.PersistentClient(path="./data")
collection = client.create_collection(name="mydocs")

documents = [
    "aaa", 
    "bbb"]
collection.add(documents=documents, ids=["1", "2"])

collection = client.get_collection("mydocs")
print(collection.get(include=["embeddings"]))
