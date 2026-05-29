from langchain_community.document_loaders import TextLoader

loader = TextLoader('./hbm.txt', encoding="utf-8")
documents = loader.load()

print(f"불러온 문서의 개수: {len(documents)}")

doc = documents[0]
print(f"page_content (앞100자만: \n{doc}...\n")
print(f"metadata: {doc.metadata}")