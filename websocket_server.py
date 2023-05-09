import asyncio
import websockets
import os
from dotenv import load_dotenv

load_dotenv()
HOST = "127.0.0.1"
PORT = int(os.getenv('PORT'))
clients = set()


async def handle_client(websocket, path):
    print(f"Conexão estabelecida com {websocket.remote_address}")
    clients.add(websocket)
    
    try:
        async for message in websocket:
            print(f"Mensagem recebida de {websocket.remote_address}: {message}")
            # envia a mensagem recebida para todos os clientes, exceto o remetente
            for client in clients:
                # if client != websocket:
                await client.send(message)
    finally:
        # Remove o websocket do cliente desconectado da lista de clientes conectados
        clients.remove(websocket)
        print(f"Cliente {websocket.remote_address} desconectado")

async def main():
    async with websockets.serve(handle_client, HOST, PORT):
        print(f"Servidor ouvindo na porta {PORT}...")
        await asyncio.Future()  # mantém o loop de eventos rodando

asyncio.run(main())
