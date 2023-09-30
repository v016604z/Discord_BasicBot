import logging
import discord

discord.utils.setup_logging()

# or, for example
discord.utils.setup_logging(level=logging.INFO, root=False)