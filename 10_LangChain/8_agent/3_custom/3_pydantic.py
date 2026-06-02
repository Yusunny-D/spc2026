import json
from typing import Literal
from pydantic import BaseModel, Field

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_agent

load_dotenv()

class SendEmailInput(BaseModel):
    """ 이메일 전송 도구의 인자 """
    to: str = Field(description="수신자 이메일 주소 (반드시 유효한 이메일 주소)")
    subject: str = Field(description="이메일 제목(50자 이내, 간결하게)")
    body: str = Field(description="이메일 본문 (반드시 한국어로 작성)")
    priority: Literal["low", "normal", "high"] = Field(default="normal", description="우선순위 .urgent한 경우에는 high 사용")

@tool(args_schema=SendEmailInput)
def send_email(to: str, subject: str, body: str, priority: str="normal") -> str:
    """사용자가 요청할 때 이메일을 보낸다."""
    print(f"[가짜 전송] to={to}, subject={subject}, body={body}, priority={priority}")


class SearchInput(BaseModel):
    """검색 도구의 인자"""
    query: str = Field(description="검색어")
    max_results: int = Field(default=5, ge=1, le=20, description="결과 갯수 (1~20)")
    sort_by: Literal["relevence", 'date'] = Field(
        default="relevence",
        description="정렬 기준. 최신 정보가 중요하면 date 사용"
    )

@tool(args_schema=SearchInput)
def search(query: str, max_results: str, sort_by: str = 'relevence') -> list[str]:
    """주어진 쿼리로 검색을 수행한다."""
    return [f"결과 {i+1}: {query} (정렬={sort_by})" for i in range(max_results)]

llm = ChatOpenAI(model="gpt-4o-mini")
llm_with_tools = llm.bind_tools([send_email, search])

print(f"=== 도구 명세 살펴보기 ===")
print(json.dumps(send_email.args_schema.model_json_schema(), indent=2, ensure_ascii=False))

print('=== 도구 실제 호출 ===')

questions = [
    "alice@example.com에게 회의 일정 변경이라는 제목으로 메일 보내줘. 본문은 '회의가 내일 3시로 변경되었습니다.'로 보내고, 긴급해.",
    "파이썬 비동기 프로그래밍 최신 자료 10개만 날짜순으로 검색해줘."
]

SYSTEM = (
    "도구는 적합할 때만 사용하세요. 그리고 입력 인자들을 잘 확인해서 "
)

for q in questions:
    print(f"\n질문: {q}")
    r = llm_with_tools.invoke(q)

    if not r.tool_calls:
        print("도구가 없는 결과:", r.content)
    else:
        for call in r.tool_calls:
            print(f" -> {call['name']} ({call['args']})")

            # 실제 실행을 원하면?
            name2call = {t.name: t for t in [send_email, search]}
            result = name2call[call["name"]].invoke(call["args"])
            print("결과: ", result)
