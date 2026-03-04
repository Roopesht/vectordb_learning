import chromadb

# Step 1: Store your knowledge base
collection = client.get_collection("company_docs")

# Step 2: User asks a question
user_question = "What is our refund policy?"

# Step 3: Retrieve relevant docs
results = collection.query(
    query_texts=[user_question],
    n_results=3
)
context = "\n".join(results['documents'][0])

# Step 4: Send to LLM with context
prompt = f"Answer using this context:\n{context}\n\nQuestion: {user_question}"
# response = llm.generate(prompt)
