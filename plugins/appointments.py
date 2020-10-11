import lightbulb
import hikari

class Appointments(lightbulb.Plugin):

    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    async def create_appointment(self, ctx, class_name: str, reason: str):
            
    @lightbulb.command() 
    async def appointment(self, ctx, class_name: str = None, *, reason: str = None):
        if class_name:
            if reason:
                await self.create_appointment(ctx, class_name, reason)
            else:
                await ctx.reply("Please enter reason to make an appointment.")
        else:
            await ctx.reply("Please enter the class name.")
    
def load(bot):
    bot.add_plugin(Appointments(bot))