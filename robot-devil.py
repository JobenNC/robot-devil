import asyncio, discord, random, logging, sys, pdb
from yarnSpin.fanFicMadLib import getStory

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
    print(connected)
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
            pass
            #return
        if message.content.find('$Storytime') >= 0:
            #peopleList = ["<@" + member.id + ">" for member in optedIn]
            peopleList = ["<@" + member.id + ">" for member in client.get_all_members()]
            #pdb.set_trace()
            #peopleList.remove("<@" + client.user.id + ">")
            peopleList = list(filter(lambda a: a != "<@" + client.user.id + ">", peopleList))
            random.shuffle(peopleList)

            names, story = getStory()
            #for i, name in enumerate(names):
            #    story = story.replace(name, peopleList[i % len(peopleList)])
            for i, person in enumerate(peopleList):
                story = story.replace(names[i % len(names)], person)

            storyText = story
            storyText = storyText.replace("\\n", "\n")
            #storyUrl = story[1]

            #pdb.set_trace()
            print(storyText)

            yield from client.send_message(message.channel, 'Once upon a time...')
            while len(storyText) > 1900:
                yield from client.send_message(message.channel, storyText[:1900])
                storyText = storyText[1900:]
            yield from client.send_message(message.channel, storyText)
            #yield from client.send_message(message.channel, storyUrl)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hailSatan(sys.argv[1]))
