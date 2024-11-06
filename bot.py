from aiohttp import web
from plugins import web_server

import pyromod.listen
from pyrogram import Client
import pyrogram.utils
from pyrogram.enums import ParseMode
import sys
from datetime import datetime
from database.database import present_channel, present_channel2

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, CHANNEL_ID, PORT


pyrogram.utils.MIN_CHANNEL_ID = -1009147483647
class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        # Assuming add_1 and add_2 functions return the channel IDs for forced subscriptions
        self.FORCESUB_CHANNEL = await present_channel()
        self.FORCESUB_CHANNEL2 = await present_channel2()

        if self.FORCESUB_CHANNEL:
            try:
                link = (await self.get_chat(self.FORCESUB_CHANNEL)).invite_link
                if not link:
                    await self.export_chat_invite_link(self.FORCESUB_CHANNEL)
                    link = (await self.get_chat(self.FORCESUB_CHANNEL)).invite_link
                self.invitelink1 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't export invite link from Force Sub Channel 1!")
                self.LOGGER(__name__).warning(f"Please double check the channel ID and make sure the bot is an admin in the channel with 'Invite Users via Link' permission. Current Channel ID: {self.FORCESUB_CHANNEL}")
                self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/Hunters_Discussion for support")
                sys.exit()

        if self.FORCESUB_CHANNEL2:
            try:
                link = (await self.get_chat(self.FORCESUB_CHANNEL2)).invite_link
                if not link:
                    await self.export_chat_invite_link(self.FORCESUB_CHANNEL2)
                    link = (await self.get_chat(self.FORCESUB_CHANNEL2)).invite_link
                self.invitelink2 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't export invite link from Force Sub Channel 2!")
                self.LOGGER(__name__).warning(f"Please double check the channel ID and make sure the bot is an admin in the channel with 'Invite Users via Link' permission. Current Channel ID: {self.FORCESUB_CHANNEL2}")
                self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/Hunters_Discussion for support")
                sys.exit()
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/Animetalks0 for support")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot Running..!\n\nCreated by \nhttps://t.me/Animes_X_Hunters")
        self.LOGGER(__name__).info(f""" \n\n       
░█████╗░███╗░░██╗██╗███╗░░░███╗███████╗██╗░░██╗██╗░░░██╗███╗░░██╗████████╗███████╗██████╗░░██████╗
██╔══██╗████╗░██║██║████╗░████║██╔════╝██║░░██║██║░░░██║████╗░██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝
███████║██╔██╗██║██║██╔████╔██║█████╗░░███████║██║░░░██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝╚█████╗░
██╔══██║██║╚████║██║██║╚██╔╝██║██╔══╝░░██╔══██║██║░░░██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗░╚═══██╗
██║░░██║██║░╚███║██║██║░╚═╝░██║███████╗██║░░██║╚██████╔╝██║░╚███║░░░██║░░░███████╗██║░░██║██████╔╝
╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░
                                          """)
        self.username = usr_bot_me.username
        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
