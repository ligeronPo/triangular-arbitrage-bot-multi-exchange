import asyncio
from telegram import Bot, Update

TOKEN = '7204730367:AAFha8VzlPCcL5LMsh_wpOE2B6UxM4v5J2s'

async def get_chat_id(token):
    bot = Bot(token)
    try:
        updates = await bot.get_updates()
        if updates:
            for update in updates:
                if isinstance(update, Update) and update.message:
                    chat_id = update.message.chat_id
                    print(f"Chat ID: {chat_id}")
                    return chat_id
            print("No messages found in updates")
            return None
        else:
            print("No updates found")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

chat_id = asyncio.run(get_chat_id(TOKEN))
print(f"Your chat_id is: {chat_id}")
