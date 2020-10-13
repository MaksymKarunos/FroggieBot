import lightbulb
import hikari
import random
import time
import asyncio
import pytz
import json
from datetime import datetime
from datetime import timedelta  


class Appointments(lightbulb.Plugin):

    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    async def create_appointment(self, ctx, class_name: str, reason: str):
        tz_NY = pytz.timezone('America/New_York') 
        nz_time = datetime.now(tz_NY)
        tommorrow = nz_time + timedelta(days=1)
        with open("database.json", "r") as f:
            json_data = json.loads(f.read())
        month, date, year = tommorrow.strftime("%m-%d-%Y").split("-")
        
        appointments = []
        for i in json_data:
            if i.split("-")[1]:
                print(i.split("-")[1])
                appointments.append(i.split("-")[1])
        if appointments == []:
            appointments.append(date)
        date = max(appointments)
        if appointments.count(max(appointments)) > 3:
            date = int(max(appointments)) +  1
        while True:
            time = random.randint(13,19)
            if f"{month}-{date}-{year}-{time}" not in json_data:
                break
        appointment_date = datetime(int(year),int(month),int(date),int(time), tzinfo=tz_NY)
        json_data[f"{month}-{date}-{year}-{time}"] = {'subject' : class_name, 'reason' : reason, 'student' : ctx.message.author.id}
        with open("database.json", "w") as f:
            f.write(json.dumps(json_data, indent=4))
        wait_time = appointment_date - nz_time
        seconds = int(wait_time.total_seconds())
        await ctx.reply(f"An appointment with **Maksym Karunos** has been scheduled for {appointment_date.strftime('%d %B, %Y at %-I %p')} (New York Timezone).")
        maksym = await self.bot.rest.fetch_user(406882130577063956)
        maxdm = await self.bot.rest.create_dm_channel(maksym)
        em = hikari.Embed(color=random.randint(0, 0xFFFFFF), title=f"Appointment scheduled with {ctx.message.author}")
        em.add_field(name="Class", value=class_name)
        em.add_field(name="Reason", value=reason)
        em.add_field(name="Date", value=appointment_date.strftime('%d %B, %Y at %-I %p'))
        await maxdm.send(em)
        await asyncio.sleep(seconds)
        with open("database.json", "w") as f:
            json_data.pop(f"{month}-{date}-{year}-{time}")
            f.write(json.dumps(json_data, indent=4))
        await maxdm.send(f"<@406882130577063956>, It's time for your appointment with {ctx.message.author}!")
        channel = await self.bot.rest.create_dm_channel(ctx.message.author)
        await channel.send("<@{ctx.message.author.id}>, It's time for your appointment with **Maksym Karunos**!")
        
        
            
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