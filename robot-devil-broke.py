import asyncio, discord, random, logging, pdb
from yarnSpin import yarnSpin

logging.basicConfig(level=logging.DEBUG)
client = discord.Client()
optedIn = set()

@asyncio.coroutine
def hailSatan(token):
    login = yield from client.login(token)
    print(login)
    print('returned from login')
    connected = yield from client.connect()
    print('returned from connect')
    print(connect)
    print('probably done')

@client.async_event
def on_message(message):
    if message.channel.name not in ('crows-nest', 'general'):
        return

    if client.user in message.mentions:
        if message.content.find("$SellSoul") >= 0:
            optedIn.add(message.author)
            yield from client.send_message(message.channel, "<@" + message.author.id +  "> You'll soon regret this.")
        if message.content.find("$ReclaimSoul") >= 0:
            yield from client.send_message(message.channel, "<@" + message.author.id +  "> You've choses wisely.")
            optedIn.remove(message.author)

        if not optedIn:
            return
        if message.content.find('$Storytime') >= 0:
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

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hailSatan(sys.argv[1]))
