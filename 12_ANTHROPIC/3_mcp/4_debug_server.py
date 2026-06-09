from mcp.server.fastmcp import FastMCP
import sys

mcp = FastMCP("HelloWorld")

@mcp.tool()
def hello(name: str) -> str:
    print(f"[SERVER] hello 함수 호출됨: name={name}", file=sys.stderr)
    return f'hello, {name}'

if __name__ == "__main__":
    print(f"[SERVER] hello 함수 호출됨", file=sys.stderr)
    mcp.run()