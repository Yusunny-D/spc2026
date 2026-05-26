import asyncio # 비동기 스레드
import websockets

# 클라이언트가 요청하면 부를 함수
async def handle_client(websocket):
    print('이 함수 호출')
    await websocket.send('서버에 연결되었습니다.')
    
    try:
        async for message in websocket:
            print('클라이언트 메세지: ', message)
            await websocket.send(f'서버가 받은 메세지: {message}')
    except websockets.exceptions.ConnectionClosed:
        print('클라이언트가 연결 종료함')

async def main():
    print('메인 함수')
    async with websockets.serve(handle_client, "localhost", 8000):
        print('웹소켓을 열었음: ws//:localhost:8000')
        await asyncio.Future()

asyncio.run(main())