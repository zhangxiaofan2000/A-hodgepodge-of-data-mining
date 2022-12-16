# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2022/12/15 9:41
# File : TCP1.py
import asyncio

async def handle_client(reader, writer):
    # Read data from the client
    data = await reader.read(1024)
    message = data.decode()

    # Process the client's request and generate a response
    response = process_request(message)

    # Send the response back to the client
    writer.write(response.encode())
    await writer.drain()
    writer.close()

def process_request(request):
    # Process the client's request and generate a response
    # ...
    response  =request

    return response

async def main():
    # Create a TCP server
    server = await asyncio.start_server(
        handle_client, 'localhost', 8888)

    # Accept incoming connections
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())
