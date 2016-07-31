import asyncio, discord, logging, pdb

logging.basicConfig(level=logging.DEBUG)
client = discord.Client()

@asyncio.coroutine
def hailSatan():
    login = yield from client.login('josephjarriel@gmail.com', 'Mypass321')
    print(login)
    print('returned from login')
    connected = yield from client.connect()
    print('returned from connect')
    print(connect)
    print('probably done')

@client.async_event
#def on_message(message):
#    if message.content.startswith('$greet'):
#        yield from client.send_message(message.channel, 'Say hello')
#        msg = yield from client.wait_for_message(author=message.author, content='hello')
#        yield from client.send_message(message.channel, 'Hello.')

def on_message(message):
    if message.content.startswith('$test'):
        #yield from client.send_message(message.channel, 'Say hello')
        #msg = yield from client.wait_for_message(author=message.author, content='hello')
        yield from client.send_message(message.channel, 'Test Message.')


loop = asyncio.get_event_loop()
#tasks = [hailSatan()]
#loop.run_until_complete(asyncio.wait(tasks))
loop.run_until_complete(hailSatan())

#def main():
#    loop = asyncio.get_event_loop()
#    loop.run_until_complete(hailSatan())
#
#if __name__ == '__main__':
#    main()
