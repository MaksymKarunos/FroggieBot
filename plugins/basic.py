import lightbulb

class Basic(lightbulb.Plugin):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        
    @lightbulb.command()
    async def ping(self, ctx):
        await ctx.reply("Pong!")
        
        
def load(bot):
    bot.add_plugin(Basic(bot))