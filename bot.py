import os
import importlib
import lightbulb
import logging
import os

logging.getLogger("lightbulb").setLevel(logging.DEBUG)
bot = lightbulb.Bot(token=os.environ['TOKEN'], prefix="t.")

"""Looping over all the files in the plugins folder"""
for i in os.listdir('./plugins'):
    """Checking if it's a Python file"""
    if i.endswith(".py"):
        """Importing the plugin with importlib"""
        plugin = importlib.import_module(f"plugins.{i[:-3]}")
        """Running the load function from that plugin file"""
        plugin.load(bot)

bot.run()