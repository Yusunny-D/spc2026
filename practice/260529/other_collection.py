import os
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import StrOutputParser

from langchain_chroma import Chroma

load_dotenv()

DB_DIR = "./other_db"
COLLECTION_HBM = "hbm"
COLLECTION_NVME = "nvme"

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

def build_store():
    hbm_loader = TextLoader("./hbm.txt", encoding="utf-8")
    hbm_docs = hbm_loader.load()

    chunks_hbm = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100).split_documents(hbm_docs)

    store_hbm = Chroma.from_documents(
        chunks_hbm, embeddings,
        collection_name=COLLECTION_HBM,
        persist_directory=DB_DIR
    )

    nvme_loader = TextLoader("./nvme.txt", encoding="utf-8")
    nvme_docs = nvme_loader.load()

    chunks_nvme = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100).split_documents(nvme_docs)

    store_nvme = Chroma.from_documents(
        chunks_nvme, embeddings,
        collection_name=COLLECTION_NVME,
        persist_directory=DB_DIR
    )
    return store_hbm, store_nvme

def load_store():
    store_hbm = Chroma(
        collection_name=COLLECTION_HBM,
        embedding_function=embeddings,
        persist_directory=DB_DIR
    )

    store_nvme = Chroma(
        collection_name=COLLECTION_NVME,
        embedding_function=embeddings,
        persist_directory=DB_DIR
    )

    print(f'디비 로드 완료 - {store_hbm._collection.count()+store_nvme._collection.count()}개 청크 로딩')
    return store_hbm, store_nvme

if os.path.exists(DB_DIR) and os.listdir(DB_DIR):
    store_hbm, store_nvme = load_store()
else:
    store_hbm, store_nvme = build_store()

question = "NVMe와 HBM를 비교해줘."

retriever_hbm = store_hbm.as_retriever(search_kwargs={'k': 3})
retriever_nvme = store_nvme.as_retriever(search_kwargs={'k': 3})

results1 = store_hbm.similarity_search(question, k=3)
results2 = store_nvme.similarity_search(question, k=3)
total_results = results1+results2


llm = ChatOpenAI(model="gpt-4o-mini")
prompt = ChatPromptTemplate.from_messages([
    ('system', "당신은 문서 기반 Q&A 시스템입니다. 아래 문서만을 참고해서 답하세요. 문서에 적합한 내용이 없으면, '모른다'라고 답변하세요.\n\n문서:\n{context}"),
    ("user", "{question}")
])

# 리스트에 담긴 Document 객체(Object)를 하나의 문자열로 바꿔주는 함수
def format_docs(docs):
    return "\n\n".join(d.page_content for d in docs)

chain = (
    RunnablePassthrough.assign(
        context=lambda x: (
        format_docs(retriever_hbm.invoke(x["question"]) + retriever_nvme.invoke(x["question"]))
            )
        )
    | prompt | llm | StrOutputParser()
)

print(f'질문: {question}\n')
print(f'답변: {chain.invoke({"question": question})}\n')

for doc in total_results:
    print(f"source: {doc.metadata}")