from discord.ext import commands
from prsaw import RandomStuff
bot = commands.Bot(command_prefix=".")

rs = RandomStuff(async_mode=True)
@bot.event
async def on_message(message):
	response = await rs.get_ai_response(message.content)
	await msg.reply(response)

	await bot.process_commands(message)

bot.run("OTU3MjcxMzA4ODEzNjMxNDg4.Yj8WYQ.QQa02Nr0I5FBu_PHD9Hmz8Hxd3g")