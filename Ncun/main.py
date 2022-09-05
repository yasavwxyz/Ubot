from pyrogram import idle 
 from uvloop import install 
  
 from config import BOT_VER 
 from Ncun import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots 
 from Ncun.helpers.misc import create_botlog, git, heroku 
  
 MSG_ON = """ 
 **Ubot Activated.** 
 ** Userbot Version -** `{}` 
 **Ketik** `.Ncun` **untuk Mengecheck Bot** 
 """ 
  
  
 async def main(): 
     for bot in bots: 
         try: 
             await bot.start() 
             bot.me = await bot.get_me() 
             await bot.join_chat("Lunatic0de") 
             await bot.join_chat("SharingUserbot") 
             try: 
                 await bot.send_message( 
                     BOTLOG_CHATID, MSG_ON.format(BOT_VER) 
                 ) 
             except BaseException: 
                 pass 
             LOGGER("Ncun").info( 
                 f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]" 
             ) 
         except Exception as a: 
             LOGGER("main").warning(a) 
             
         LOGGER("Ncun").info(f"Ncun-Ubot v{BOT_VER} ⚙️[AKTIF]) 
     if bot1 and not str(BOTLOG_CHATID).startswith("-100"): 
         await create_botlog(bot1) 
     await idle() 
     await aiosession.close() 
  
  
 if __name__ == "__main__": 
     LOGGER("Ncun").info("Memulai Ubot") 
     install() 
     git() 
     heroku() 
     LOOP.run_until_complete(main())