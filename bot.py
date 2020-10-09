import os
import lightbulb 

bot = lightbulb.Bot(token=os.environ['TOKEN'], prefix="!") 

@bot.command()
async def ping(ctx):
    await ctx.reply("Pong!")

bot.run()