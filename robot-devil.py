import discord
import logging
import asyncio
import aiohttp
import pdb

logging.basicConfig(level=logging.DEBUG)

@asyncio.coroutine
def fetch_page(url):
    resp = yield from aiohttp.request('GET', url)
    assert resp.status == 200
    content = yield from resp.read()
    print('URL: {0}: Content: {1}'.format(url, url))

@asyncio.coroutine
def new(future, name, seconds=2):
    print('{0} sleeping for: {1}'.format(name, seconds))
    yield from asyncio.sleep(seconds)
    print("{} I'm awake!".format(name))
    yield from asyncio.sleep(seconds)
    future.set_result('{0} is done!'.format(name))

def done(future):
    print(future.result())

@asyncio.coroutine
def discordConn():
    client = discord.Client()
    login = yield from client.login('josephjarriel@gmail.com', 'Mypass321')
    print(login)
    print('returned from login')
    connected = yield from client.connect()
    print('returned from connect')
    print(connect)

loop = asyncio.get_event_loop()

future1 = asyncio.Future()
future2 = asyncio.Future()

tasks1 = [
    new(future1, 'task1', 4),
    new(future2, 'task2', 3),
]

tasks2 = [
    fetch_page('http://google.com'),
    fetch_page('http://cnn.com'),
    fetch_page('http://twitter.com'),
]

tasks3 = [
    discordConn()
]

future1.add_done_callback(done)
future2.add_done_callback(done)

loop.run_until_complete(
    asyncio.wait(tasks3)
)
loop.close()

