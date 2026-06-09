import asyncio
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    server_params = StdioServerParameters(command="python", args=["2_mcp_server"])

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            print(f"[Client] 서버 HS전", file=sys.stderr)
            await session.initialize()
            print(f"[Client] 서버 HS후", file=sys.stderr)

            tools = (await session.list_tools()).tools
            print(f"[Client] 서버가 쓸 수 있는 tool은 뭐가 있니?")

            result = await session.call_tool("hello", {'name': "John"})

            print(result.content[0].text)


if __name__ == "__main__":
    print(f"[Client] 클라이언트가 시작됨", file=sys.stderr)
    asyncio.run((main()))

