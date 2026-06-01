from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

# 랭체인 기본 불러오기
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

# 문서 파서 기본 불러오기 (PyPDFLoader)
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()

# 1. 백터스토어 셋업
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

DB_DIR = "./chroma.db"


# 2. 랭체인 셋업한다 (LCEL)

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
    # store = Chroma(collection_name="DB", embedding_function=embeddings, persist_directory=DB_DIR)
    
    # 파일이 정상적으로 받아졌으면? 우리 DATA 폴더에 저장한다.
    

    part = splitter.split_documents(PyPDFLoader(data['pdf']).load())

    print (part)

    return jsonify({"message": "업로드"})

@app.post('/ask')
def ask():
    return jsonify({"message": "답변 완료"})

if __name__ == "__main__":
    app.run(debug=True)