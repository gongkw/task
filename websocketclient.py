#!/usr/bin/env python
import asyncio
import websockets

@asyncio.coroutine
def hello():
    websocket = websockets.connect('ws://localhost:8765/')

    name = input("What's your name? ")
    websocket.send(name)
    print("> {}".format(name))

    greeting = websocket.recv()
    print("< {}".format(greeting))

    websocket.close()

asyncio.get_event_loop().run_until_complete(hello())


# #!/usr/bin/env python
# import asyncio
# import websockets
# async def hello(uri):
# async with websockets.connect(uri) as websocket:
# await websocket.send("Hello world!")
# asyncio.get_event_loop().run_until_complete(
# hello('ws://localhost:8765'))