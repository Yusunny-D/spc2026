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
    distance, indices = index.search(np.array([query_embedding]), k=1) # 백터DB에서 질문(user_query)의 숫자갑과 가장 가까운 거를 k+1개 반환하시오
    retrieved_doc = document[indices[0][0]]

    # 거리 측정된 걸 유사도 점수로 변환
    true_distance = np.sqrt(distance[0][0])
    similarity_score = 1/ (1+true_distance) # 거리값을 정규화하여 유사도 점수로 변환

    print("\n===\n유사도점수")
    print(f'검색된 문서: {retrieved_doc}')
    print(f'유사도 점수: {true_distance:.3f}')

    if similarity_score < 0.65:
        return '해당 내용의 적합한 답변을 찾을 수 없습니다.'

    prompt = f"""
    당신은 제공된 참고 자료를 기반으로만 답변하는 AI입니다.

    규칙:
    1. 반드시 관련 자료를 근거로 답변하시오.
    2. 관련 자료에 없는 내용은 추측하지 마시오.
    3. 질문과 관련된 자료가 없으면 "제공된 자료에서는 해당 내용을 확인할 수 없습니다." 라고 답변하시오.
    4. 사용자는 원문 자료를 볼 수 없으므로 "자료에 따르면", "문서에 따르면" 같은 표현은 사용하지 마시오.
    5. 질문과 관계없는 답변은 하지 마시오.
    6. 답변은 자연스럽고 친절한 말투로 작성하시오.
    7. 적절히 이모티콘을 사용하시오.

    사용자의 질문:
    {user_query}

    관련 자료:
    {retrieved_doc}
    """

    print('>>>>>>>')
    print(f'질문과 가까운 벡터: {indices} 그 거리: {distance}')
    print('<<<<<<<')


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

query = '요즘 인기있는 영화는?'
# query = '너는 뭐야?'
# query = '홍길동은 누구야??'
# query = 'Python은 개발 언어 중에 가장 쉽다고 하는데, 그렇게 쉬운 언어는 아닙니다.'

print(rag_query(query))