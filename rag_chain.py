from llama_index import VectorStoreIndex, SimpleDirectoryReader
from langchain.chat_models import ChatOpenAI
from llama_index.storage.storage_context import StorageContext

llm = ChatOpenAI(temperature=0.3)

def suggest_infrastructure_projects():
    docs = SimpleDirectoryReader("data/documents").load_data()
    storage_context = StorageContext.from_defaults(persist_dir="vectorstore/chroma")
    index = VectorStoreIndex.from_documents(docs, storage_context=storage_context)

    query_engine = index.as_query_engine(llm=llm)
    result = query_engine.query("Which infrastructure projects are needed given the uploaded plans and maps?")
    return {"recommendations": result.response}