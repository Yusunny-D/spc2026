from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter

loader = TextLoader('./hbm.txt', encoding="utf-8")
documents = loader.load()

contents = documents[0].page_content
print('원본 글자수', len(contents))

char_splitter = CharacterTextSplitter(
    separator='\n\n',   # 이것을 목표로 하는데, 안되면
    chunk_size=500,     # 최대 500개 되면 겹치게?
    chunk_overlap=100,  # 문장이 중간에 짤리면 의미가 사라지니 겹치게 자름
)

chunks_char = char_splitter.split_documents(documents)
print(f'[CharSplitter] {len(chunks_char)}')
print(f'첫 청크 글자 수 {len(chunks_char[0].page_content)}')


############################

recur_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks_recur = recur_splitter.split_documents(documents)
print(f'[RecurSplitter] {len(chunks_recur)}')
print(f'첫 청크 글자 수 {len(chunks_recur[0].page_content)}')