# 금융 도우기 에이전트 챗봇 만들기

# 툴들 추가

# 1. 네이버 뉴스를 가져온다. 
# 2. 구글 검색으로 해당 기업 개요/최근 정보 조회 
# 3. 환율을 조회한다. 
# 4. 주가를 조회한다.

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from fil_tools import TOOLS

SYSTEM = """
당신은 금융 정보 비서입니다. 뉴스검색, 기업정보조회, 환율, 주가 도구를 사용해서 한국어로 간결하게 답변을 주는 금융 비서입니다.
- 환율/주가 같은 수치 데이터는 반드시 도구를 통해서 확인하시오. (추측 또는 과거 데이터 이용 금지)
- 출처 링크가 있으면 함께 제시하시오.
"""

agent = create_agent(ChatOpenAI(model='gpt-4o-mini'), TOOLS, system_prompt=SYSTEM)


def ask(question):
    # agent를 통해서 해당 질문을 호출한다.
    print('[질문]', question)
    result = agent.invoke({"messages": [('user', question)]})
    tool_used = [c['name'] for m in result['messages']
                if getattr(m, "tool_calls", None) for c in m.tool_calls]
    print(f"[사용 도구] {tool_used or '(없음)'}")
    print(f"[답변] {result['messages'][-1].content}")

if __name__ == "__main__":
    print('=== 데모 명령어 ===')
    for question in ["삼성주가 알려줘.", "달러 환율 얼마야?", "엔비디아 관련 최근 뉴스는 뭐가 있어?"]:
        ask(question)


    print('=== 수동 질의 응답 시작 ===')
    while True:
        # 사용자로부터 질문을 받아서 'q', 'quit', 'exit', 가 올때까지 반복한다.
        ask(question)
        if not question or question.lower() in ("q", "quit", "exit"):
            break