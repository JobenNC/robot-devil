import asyncio, discord, random, logging, pdb
from yarnSpin import yarnSpin

logging.basicConfig(level=logging.DEBUG)
client = discord.Client()
optedIn = set()

@asyncio.coroutine
def hailSatan():
    #print(discord.utils.oauth_url('215277164000444416', None, None, 'robot-devil'))
    #return

    #login = yield from client.login('josephjarriel@gmail.com', 'Mypass321')
    login = yield from client.login('MjE1Mjc3MTY0MDAwNDQ0NDE2.CpVctQ.dOxr9W2xI_aMxncmc2yw6P-0Pdg')
    print(login)
    print('returned from login')
    connected = yield from client.connect()
    print('returned from connect')
    print(connect)
    print('probably done')

#@client.async_event
#def on_message(message):
#    if message.content.startswith('$greet'):
#        yield from client.send_message(message.channel, 'Say hello')
#        msg = yield from client.wait_for_message(author=message.author, content='hello')
#        yield from client.send_message(message.channel, 'Hello.')

@client.async_event
def on_message(message):
    if message.channel.name not in ('crows-nest', 'general'):
        return

    if client.user in message.mentions:
        if message.content.find("$SellSoul") >= 0:
            optedIn.add(message.author)
            #yield from client.send_message(message.author, 'okay')
            yield from client.send_message(message.channel, "<@" + message.author.id +  "> You'll soon regret this.")
        if message.content.find("$ReclaimSoul") >= 0:
            yield from client.send_message(message.channel, "<@" + message.author.id +  "> You've choses wisely.")
            optedIn.remove(message.author)

        if not optedIn:
            return

        if message.content.find('$Storytime') >= 0:
            #yield from client.send_message(message.channel, 'Say hello')
            #msg = yield from client.wait_for_message(author=message.author, content='hello')
            #yield from client.send_message(message.channel, 'Once upon a time...')

            #members = client.get_all_members()
            #members = set(member for member in members)
            #for member in members:
            #    pdb.set_trace()
            #    print(member.name)
            #shuffledList = [member.name for member in members]

            peopleList = ["<@" + member.id + ">" for member in optedIn]
            random.shuffle(peopleList)
            story = yarnSpin.findYarn(peopleList)
            storyText = story[0]
            storyUrl = story[1]

            yield from client.send_message(message.channel, 'Once upon a time...')
            while len(storyText) > 1900:
                yield from client.send_message(message.channel, storyText[:1900])
                storyText = storyText[1900:]
            yield from client.send_message(message.channel, storyText)
            yield from client.send_message(message.channel, storyUrl)
            

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
