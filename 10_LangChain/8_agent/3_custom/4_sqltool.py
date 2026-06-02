import sqlite3

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_agent

load_dotenv()

conn = sqlite3.connect(':memory:', check_same_thread=False)
conn.executescript(
    """
    CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, city TEXT, age INTEGER);
    CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price INTEGER, category TEXT);
    CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INTEGER, product_id INTEGER, qty INTEGER, ordered_at TEXT);

    INSERT INTO users (id, name, city, age) VALUES
    (1, 'Kim', 'Seoul', 28), (2, 'Lee', 'Busan', 34),
    (3, 'Park', 'Incheon', 25), (4, 'Choi', 'Daegu', 41);

    INSERT INTO products (id, name, price, category) VALUES
    (1, 'Laptop', 1500, 'Electronics'), (2, 'Mouse', 30, 'Electronics'),
    (3, 'Desk', 250, 'Furniture'), (4, 'Chair', 120, 'Furniture');

    INSERT INTO orders (id, user_id, product_id, qty, ordered_at) VALUES
    (1, 1, 1, 1, '2025-06-01'), (2, 3, 2, 3, '2025-06-02'),
    (3, 2, 4, 3, '2025-06-03'), (4, 1, 3, 4, '2025-06-04'),
    (5, 2, 1, 3, '2025-06-05'), (6, 4, 3, 4, '2025-06-06');
    """
)
conn.commit()

SCHEMA = """
users(id, name, city, age)
products (id, name, price, category) -- price 단위: 원
orders (id, user_id, product_id, qty, ordered_at) --user_id=user.id, product_id=product.id
"""

@tool
def run_sql(query: str) -> str:
    """SQLite DB에 SQL 구문을 실행하고 결과를 반환한다."""
    q = query.strip().rstrip(";")
    cur = conn.execute(q)
    cols = [d[0] for d in cur.description]
    rows = cur.fetchall()
    if not rows:
        return "결과 없음"
    
    out = [" | ".join(cols)]
    out += [" | ".join(str(v) for v in row) for row in rows]
    return "\n".join(out)

SYSTEM = f"""
당신은 SQLite 데이터 분석가 입니다. 아래 스키마를 사용해서 질문에 응답하시오.

[스키마]
{SCHEMA}

규칙:
 - 답변을 할 때에는 run_sql툴을 사용해서 쿼리문을 실행하시오.
 -SQLite 문법만 사용하고 JOIN, GROUP BY 등도 사용 가능함.
"""

llm = ChatOpenAI(model="gpt-4o-mini")
agent = create_agent(llm, [run_sql], system_prompt=SYSTEM)

questions = [
    "서울사 사는 사용자는 몇 명이야?",
    "가장 비싼 상품 3개를 가격 높은 순으로 보여줘",
    "홍길동이 주문한 상품 이름과 수량을 보여줘",
    "카테고리별 총 주문 수량을 알려줘"
]

for q in questions:
    print(f"[질문]: {q}")
    result = agent.invoke({"messages": [("user", q)]})

    for m in result["messages"]:
        for call in getattr(m, "tool_calls", None) or []:
            print(f"  [실행한 쿼리] {call['args'].get('query')}")
    print(f"[답변] {result['messages'][-1].content}")