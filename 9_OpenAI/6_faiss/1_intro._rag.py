from dotenv import load_dotenv
import os

from openai import OpenAI

import faiss
import numpy as np

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

# 우리의 문장 데이터
document =[ "한국소프트웨어저작권 협회는 spc라는 약자를 가지고 있고, 다양한 국내 기업의 SW라이센스와 저작원을 자루는 곳입니다.",
"홍길동은 2020 1월 1일 생으로, 강원도 설빙산에서 태어났고, 그곳에서 호랑이를 잡어먹으며 성쟁했습니다.",
"Python은 개발 언어 중에 가장 쉽다고 하는데, 그렇게 쉬운 언어는 아닙니다."
]

def get_embedding(text):
    response = client.embeddings.create(
        input=text,
        model="text-embedding-ada-002"
    )

    # print(response)
    return np.array(response.data[0].embedding)

# print(get_embedding(document))

index = faiss.IndexFlatL2(1536) # OpenAI로 임베딩 하면 1536차원
doc_embeddings = np.array([get_embedding(doc) for doc in document])
index.add(doc_embeddings) # 나온 숫자값을 백터DB에 넣는다.

# 사용자의 질문을 받아서 우리의 백터DB에 물어본다
def rag_query(user_query):
    query_embedding = get_embedding(user_query)
    _, indices = index.search(np.array([query_embedding]), k=1) # 백터DB에서 질문(user_query)의 숫자갑과 가장 가까운 거를 k+1개 반환하시오
    retrieved_doc = document[indices[0][0]]

    prompt = f'''
    아래 내용을 보고 답변하시오. 아래 질문과 관련 자료가 연관이 없으면 모른다고 답변할 수 없는 내용이면
    적절한 미사여구와 이모티콘으로 답변하시오. 질문에 전혀 상관 없는 대답은 하지 말고 사용자는 제공된 문서의 내용을
    못 보기 때문에 그것에 대해서도 언급하지 마시오.
    

    사용자의 질문: {user_query}

    관련 자료: {retrieved_doc}
    '''

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role': 'system', 'content': '당신은 친절한 AI도우미 입니다.'},
            {'role': 'user', 'content': prompt}
        ]
    )

    # print(indices)
    # return retrieved_doc
    return response.choices[0].message.content

query = '너는 뭐야?'
# query = '땡땡이는 spc에서 태어났음~'

print(rag_query(query))