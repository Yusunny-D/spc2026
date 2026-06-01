import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template, send_from_directory

# 랭체인 기본 불러오기
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

# 문서 파서 기본 불러오기 (PyPDFLoader)
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

load_dotenv()

# 1. 백터스토어 셋업
DB_DIR = "./chroma.db"
DATA_DIR = "./DATA"
COLLECTION_NAME = "my_rag_db"

os.makedirs(DATA_DIR, exist_ok=True)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
store = Chroma(collection_name=COLLECTION_NAME, embedding_function=embeddings, persist_directory=DB_DIR)
retriever = store.as_retriever(search_kwargs={'k': 3})
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

# 2. 랭체인 셋업한다 (LCEL)
llm = ChatOpenAI(model="gpt-4o-mini")
prompt = ChatPromptTemplate.from_messages([
    ('system', "당신은 문서 기반 QA시스템입니다. 아래 문서만 참고해서 답변하시오.\n\n"
                "문서에 적합나 내용이 없으면, '모른다'라고 답변하시오.\n"
                "문서\n{context}\n"),
    ("user", "{question}")
])

######################
# Flask
######################
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.post('/upload')
def upload():
    file = request.file.get('files')
    
    # 파일이 정상적으로 받아졌으면? 우리 DATA 폴더에 저장한다.
    

    part = splitter.split_documents(PyPDFLoader(data['pdf']).load())

    print (part)

    return jsonify({"message": "업로드"})

@app.post('/ask')
def ask():
    return jsonify({"message": "답변 완료"})

if __name__ == "__main__":
    app.run(debug=True)