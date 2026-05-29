from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("./Javascript.pdf")
pages = loader.load()

print("페이지 수: ", len(pages))

for p in pages:
    if p.page_content.strip():
        print("발견한 내용이 있는 첫 페이지: ", p.metadata)
        print("페이지 내용", p.page_content[:100])
        break