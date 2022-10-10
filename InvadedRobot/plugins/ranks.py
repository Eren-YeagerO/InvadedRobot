import config
import asyncio
import media

from pyrogram import filters
from pyrogram.types import *

from InvadedRobot import bot
from InvadedRobot.rank import RANK_USERS , TROOP_USERS
from InvadedRobot.helpers.ranksdb import *
from InvadedRobot.helpers.troopsdb import *

@bot.on_message(filters.command("rank"))
async def rank(_, message):
    reply = message.reply_to_message
    user_id = message.from_user.id
    if not user_id in config.DEVS:
        msg = await message.reply_text("`Only Invaders Can Access This...`")
        await asyncio.sleep(10)
        await msg.delete()
    elif reply:
       try:
           user_id = int(reply.from_user.id)
           if user_id in (await RANK_USERS()):
              await message.reply_text("`The Following User Is Invader You Can Demote Him Into Troop or Civilian`",
              reply_markup=InlineKeyboardMarkup([[
InlineKeyboardButton("Demote To Troop", callback_data=f"demote_to_troops:{user_id}"),],[
InlineKeyboardButton("Demote to Civilian", callback_data=f"demote_to_civilian:{user_id}")]]))

           elif user_id in (await TROOP_USERS()):
              await message.reply_text("`The Following User Is Troop You Can Promote Him Into Invader Or Civilian`",
              reply_markup=InlineKeyboardMarkup([[
InlineKeyboardButton("Promote To Invader", callback_data=f"promote_to_invader:{user_id}"),],[
InlineKeyboardButton("Demote To Civilian", callback_data=f"demote_to_civilian:{user_id}")]]))
           else:
              await message.reply_text("`The Following User Is Civilian You Can Promote Him Into Invader or Troop`",
              reply_markup=InlineKeyboardMarkup([[
InlineKeyboardButton("Promote To Invader", callback_data=f"promote_to_invader:{user_id}"),],[
InlineKeyboardButton("Promote To Troop", callback_data=f"promote_to_troops:{user_id}")]]))          
       except Exception as e:
          await message.reply_photo(photo=media.ERROR_IMG,caption=e)
    elif not reply:
       try:
           if len(message.command) <2:
                 msg = await message.reply_text("`You Need To Use Correct Formatting Method...`")
                 await asyncio.sleep(10)
                 await msg.delete() 
           user_id = int(message.text.split("-u")[1])
           if user_id in (await RANK_USERS()):
              await message.reply_text("`The Following User Is Invader You Can Demote Him Into Troop or Civilian`",
              reply_markup=InlineKeyboardMarkup([[
InlineKeyboardButton("Demote To Troop", callback_data=f"demote_to_troops:{user_id}"),],[
InlineKeyboardButton("Demote To Civilian", callback_data=f"demote_to_civilian:{user_id}")]]))

           elif user_id in (await TROOP_USERS()):
              await message.reply_text("`the user is Troop you can promote to Invader or demote to Civilian`",
              reply_markup=InlineKeyboardMarkup([[
InlineKeyboardButton("promote to Invader", callback_data=f"promote_to_invader:{user_id}"),],[
InlineKeyboardButton("demoet to Civilian", callback_data=f"demote_to_civilian:{user_id}")]]))
           else:
              await message.reply_text("`the user is Civilian you can promote to Invader or promote to troops`",
              reply_markup=InlineKeyboardMarkup([[
InlineKeyboardButton("promote to Invader", callback_data=f"promote_to_invader:{user_id}"),],[
InlineKeyboardButton("promote to Troops", callback_data=f"promote_to_troops:{user_id}")]]))           
       except Exception as e:
          await message.reply_photo(photo=media.ERROR_IMG,caption=e)

@bot.on_callback_query(filters.regex("demote_to_civilian"))
async def demote_to_civilian(_, query):
   user_id = int(query.data.split(":")[1])
   try:
      if not query.from_user.id in config.DEVS:
          return await query.answer("Only work dev users.", show_alert=True)
      elif user_id in (await RANK_USERS()):
           await remove_rank(user_id)
           await query.message.edit("`Successfully Invader user Demoted to Civilian!`")
      elif user_id in (await TROOP_USERS()):
           await remove_troop(user_id)
           await query.message.edit("`Successfully troop user Demoted to Civilian!`")
   except Exception as e:
       await query.message.reply_photo(media.ERROR_IMG, caption=e)

@bot.on_callback_query(filters.regex("demote_to_troops"))
async def demote_to_troops(_, query):
   user_id = int(query.data.split(":")[1])
   try:
      if not query.from_user.id in config.DEVS:
          return await query.answer("Only work dev users.", show_alert=True)
      elif user_id in (await RANK_USERS()):
           await remove_rank(user_id)
           await add_troop(user_id)
           await query.message.edit("`Successfully Invader user Demoted to Troops!`")
   except Exception as e:
       await query.message.reply_photo(media.ERROR_IMG, caption=e)

@bot.on_callback_query(filters.regex("promote_to_troops"))
async def promote_to_troops(_, query):
   user_id = int(query.data.split(":")[1])
   try:
      if not query.from_user.id in config.DEVS:
          return await query.answer("Only work dev users.", show_alert=True)
      else:
           await add_troop(user_id)
           await query.message.edit("`Successfully Civilian promote to Troops!`")
   except Exception as e:
       await query.message.reply_photo(media.ERROR_IMG, caption=e)

@bot.on_callback_query(filters.regex("promote_to_invader"))
async def promote_to_invader(_, query):
   user_id = int(query.data.split(":")[1])
   try:
      if not query.from_user.id in config.DEVS:
          return await query.answer("Only work dev users.", show_alert=True)
      elif user_id in (await TROOP_USERS()):
            await remove_troop(user_id)
            await add_rank(user_id)
            await query.message.edit("`Successfully Troop user Promoted to Invader`")
      else:
          await add_rank(user_id)
          await query.message.edit("`Successfully Civilian Promoted to Invader`")
   except Exception as e:
       await query.message.reply_photo(media.ERROR_IMG, caption=e)
