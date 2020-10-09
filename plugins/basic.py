import lightbulb

class Basic(lightbulb.Plugin):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        
    @lightbulb.command()
    async def ping(self, ctx):
        await ctx.reply("Pong!")
    
    @lightbulb.command()
    async def ihatedogs(self, ctx):
        await ctx.reply("Max hates the dog")
        
def load(bot):
    bot.add_plugin(Basic(bot))