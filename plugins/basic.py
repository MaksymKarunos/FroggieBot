import lightbulb

class Basic(lightbulb.Plugin):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        
    @lightbulb.command()
    async def ping(self, ctx):
        await ctx.reply("Pong!")
        
    @lightbulb.command()
    async def squared(self, ctx, num: int): # Taking input here. Just add a new argument and that will be the input
        await ctx.reply(f"Square of {num} is {num**2}")
    
        
def load(bot):
    bot.add_plugin(Basic(bot))