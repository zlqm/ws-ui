from aiohttp import web


async def echo(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    await ws.send_str('ready')
    async for msg in ws:
        await ws.send_str(f'received "{msg.data}"')
    return ws


app = web.Application()
app.add_routes([web.get('/', echo)])
web.run_app(app)
