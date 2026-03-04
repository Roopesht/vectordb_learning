import chromadb
client = chromadb.PersistentClient('./data')
collection = client.get_collection("mydocs")
print(collection.get())