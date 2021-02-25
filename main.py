import discord as dis
from time import sleep

client = dis.Client()

data_dict = {}
ids = [670295612016820237, 447334561496432640]

class pingsession:
    canstop = False
    amt = None
    member = None
    channel = None

    def __init__(self, member, amt, channel):
        data_dict[member.id] = self
        self.amt = amt
        self.member = member
        self.channel = channel
           
    async def start(self):
         while (not self.canstop) and self.amt != 0 :
            if self.amt > 0:
                self.amt = self.amt - 1
            await self.channel.send(f'<@!{self.member.id}>')
            sleep(0.5)
         data_dict[self.ember.id] = None
   
    def stop(self):
        self.canstop = True


def getargs(message):
    return message.strip("!").split()


@client.event
async def on_ready():
    print("Ready")

@client.event
async def on_message(message):
    if not message.content.startswith("!"): 
        return

    args = getargs(message.content)
    if not (message.author.id in ids):
        return
    if args[0] == "ping":
        recipient = args[1].strip("<").strip(">").strip("@").strip("!")
        member = await message.guild.fetch_member(recipient)

        if member:
            if member.id in data_dict.keys(): 
                data_dict[member.id].stop()
                data_dict[member.id] = None
                return
            amt = args[2]
            await pingsession(member, amt.lower() == "inf" and -1 or int(amt), message.channel).start()
        
        else:
            await message.channel.send("User not found") 
     
client.run()


