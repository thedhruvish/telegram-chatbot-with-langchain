from dotenv import load_dotenv
from pyrogram import Client, filters  # type: ignore
import os
from utile.main import llm_called

load_dotenv()


app = Client(
    "my_bot",
    bot_token=os.getenv("BOT_TOKEN", ""),
    api_id=os.getenv("API_ID", ""),
    api_hash=os.getenv("API_HASH", ""),
)


@app.on_message(filters.text & filters.private)
async def echo(client, message):
    res = llm_called(message.text)
    await message.reply(res)


if __name__ == "__main__":
    app.run()
