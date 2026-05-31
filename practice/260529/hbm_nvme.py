import os
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from langchain_chroma import Chroma

load_dotenv()

DB_DIR = "./chroma_db"
COLLECTION_NAME = "coding"

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

def build_store():
    hbm_loader = TextLoader("./hbm.txt", encoding="utf-8")
    hbm_docs = hbm_loader.load()
    nvme_loader = TextLoader("./nvme.txt", encoding="utf-8")
    nvme_docs = nvme_loader.load()

    total_docs = hbm_docs + nvme_docs

    chunks = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100).split_documents(total_docs)

    store = Chroma.from_documents(
        chunks, embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=DB_DIR
    )
    return store

def load_store():
    store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=DB_DIR
    )

    print(f'디비 로드 완료 - {store._collection.count()}개 청크 로딩')
    return store

if os.path.exists(DB_DIR) and os.listdir(DB_DIR):
    store = load_store()
else:
    store = build_store()


question = "NVMe와 HBM를 비교해줘."

retriever = store.as_retriever(search_kwargs={'k': 3})
results = store.similarity_search(question, k=3)


llm = ChatOpenAI(model="gpt-4o-mini")
prompt = ChatPromptTemplate.from_messages([
    ('system', "당신은 문서 기반 Q&A 시스템입니다. 아래 문서만을 참고해서 답하세요. 문서에 적합한 내용이 없으면, '모른다'라고 답변하세요.\n\n문서:\n{context}"),
    ("user", "{question}")
])

def format_docs(docs):
    return "\n\n".join(d.page_content for d in docs)

chain = (
    RunnablePassthrough.assign(context=lambda x: format_docs(retriever.invoke(x["question"])))
    | prompt | llm | StrOutputParser()
)

print(f'질문: {question}\n')
print(f'답변: {chain.invoke({"question": question})}\n')

for doc in results:
    print(f"source: {doc.metadata}")