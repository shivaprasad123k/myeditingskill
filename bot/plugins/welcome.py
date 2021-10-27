import os
from pyrogram import Client as wasim
from pyrogram.types import Message, User

@wasim.on_message(filters.new_chat_members)
async def welcome(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"**Hey there {message.from_user.mention}, welcome to {message.chat.username} How are you 🥰**",chat_id=chatid)
	
@wasim.on_message(filters.left_chat_member)
async def goodbye(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"Bye ,  {message.from_user.mention} , Have a Nice Day",chat_id=chatid)
	
