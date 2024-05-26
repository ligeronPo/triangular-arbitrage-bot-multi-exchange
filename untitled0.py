from telegram import Bot

TOKEN = '7204730367:AAFha8VzlPCcL5LMsh_wpOE2B6UxM4v5J2s'

def get_chat_id(token):
    bot = Bot(token)
    updates = bot.get_updates()
    if updates:
        chat_id = updates[-1].message.chat_id
        print(f"Chat ID: {chat_id}")
        return chat_id
    else:
        print("No messages found")
        return None

chat_id = get_chat_id(TOKEN)
print(f"Your chat_id is: {chat_id}")
