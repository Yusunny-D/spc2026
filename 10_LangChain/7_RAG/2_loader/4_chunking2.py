from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


loader = PyPDFLoader("./Javascript.pdf")
pages = loader.load()

print(f"PDF 페이지 수: {len(pages)}\n" )

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(pages)
print(f'청킹 후 문서 갯수: {len(chunks)}\n')

first = chunks[0]
print(first.metadata)
print(first.page_content)
print('-'*80)

first = chunks[101]
print(first.metadata)
print(first.page_content)
print('-'*80)

