from flask import Flask, send_from_directory, jsonify, request
import os
from dotenv import load_dotenv
from openai import OpenAI

app = Flask(__name__, static_folder='public')
load_dotenv()
openai_key = os.getenv('OPENAI_KEY')
client = OpenAI(api_key=openai_key)

reviews = [] # 사용자들의 댓글을 저장할 변수 (평점과 후기가 함께 dict로 들어감 {'rating': 1, 'comment': '...'})

# ----------------
# API 라우팅
# ----------------
@app.route('/api/reviews', methods=['POST']) # POST로 받기
def add_review():
    # 리뷰 저장
    review = request.get_json()
    reviews.append(review)
    return jsonify({'message': '미완성'})

@app.route('/api/reviews') # GET으로 받기
def get_review():
    # 리뷰 가져와서 반환
    # print(reviews)
    return jsonify({'message': '미완성'})

@app.route('/api/ai-summary') # GET으로 받기
def get_ai_summary():
    # 리뷰 가져와서 여기에서 프롬프트 및 api 호출 코드 작성
    comment_list = []
    rating_count = 0
    for review in reviews:
        rating_count += int(review['rating'])
        avg_rating = round(rating_count/len(reviews), 2)
        comment_list.append(review['comment'])

    prompt = (
        "너는 상품 리뷰를 요약하는 시스템이다.\n"
        "아래 리뷰들을 바탕으로 핵심 내용을 한국어 한 문장으로 요약하라.\n"
        "출력 규칙:\n"
        "- 요약문만 출력한다.\n"
        "- '알겠습니다', '요약:', '리뷰 요약:' 같은 말을 쓰지 않는다.\n"
        "- 리뷰에 없는 내용을 추측하지 않는다.\n"
        "- 40자 이내로 작성한다.\n\n"
        "[리뷰 목록]\n"
        f"{', \n'.join(comment_list)}"
    )

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role': 'system', 'content': "너는 리뷰 요약문만 출력하는 엔진이다. 인사말, 설명, 접두어 없이 결과만 출력한다."},
            {'role': 'user', 'content': prompt}
        ]
    )
    ai_summary = response.choices[0].message.content
    # print(avg_rating, ai_summary)

    return jsonify({'avg_rating': avg_rating, 'ai_summary': ai_summary})

# ----------------
# 웹서비스 라우팅
# ----------------
@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)