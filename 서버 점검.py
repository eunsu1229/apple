import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == '서버 점검':
            await message.channel.send('@everyone ```※서버가 점검중입니다※```')

client = MyClient()
client.run('NjYxNzQzNzQ2MTI3NDk1MTc3.XgwGbw.fbJkF5Uq78rXeecla9h_f30N-bI')


