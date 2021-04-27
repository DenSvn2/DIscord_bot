import discord,random
from discord.ext import commands
from pyowm import OWM
import datetime
import wikipedia
from forex_python.converter import CurrencyRates


list_1 = ['https://i.gifer.com/WJRx.gif', 'https://i.gifer.com/3uvT.gif', 'https://i.gifer.com/1dTC.gif', 'https://i.gifer.com/QD5k.gif', 'https://i.gifer.com/79UW.gif', 'https://i.gifer.com/C4wf.gif', 'https://i.gifer.com/YAg6.gif', 'https://i.gifer.com/Wtya.gif', 'https://i.gifer.com/Tvnq.gif', 'https://i.gifer.com/B8Vk.gif', 'https://i.gifer.com/9hQM.gif', 'https://i.gifer.com/8Nwv.gif', 'https://i.gifer.com/Jq9s.gif', 'https://i.gifer.com/Jnt.gif', 'https://i.gifer.com/3qsD.gif', 'https://i.gifer.com/28ee.gif', 'https://i.gifer.com/R0FD.gif', 'https://i.gifer.com/8YuB.gif', 'https://i.gifer.com/ItBU.gif', 'https://i.gifer.com/WpCj.gif', 'https://i.gifer.com/VeC.gif', 'https://i.gifer.com/Pw0.gif', 'https://i.gifer.com/Pvg.gif', 'https://i.gifer.com/3SfS.gif', 'https://i.gifer.com/52O8.gif', 'https://i.gifer.com/np2.gif', 'https://i.gifer.com/WEpo.gif', 'https://i.gifer.com/3BBP.gif', 'https://i.gifer.com/4N14.gif', 'https://i.gifer.com/nS2.gif', 'https://i.gifer.com/Awch.gif', 'https://i.gifer.com/PjFM.gif', 'https://i.gifer.com/5YI9.gif', 'https://i.gifer.com/i0I.gif', 'https://i.gifer.com/33Hn.gif', 'https://i.gifer.com/Pxwc.gif', 'https://i.gifer.com/3RwI.gif', 'https://i.gifer.com/Wtpp.gif', 'https://i.gifer.com/TLcI.gif', 'https://i.gifer.com/I0Wr.gif', 'https://i.gifer.com/2Vdb.gif', 'https://i.gifer.com/YEqS.gif', 'https://i.gifer.com/7V0.gif', 'https://i.gifer.com/6kg.gif', 'https://i.gifer.com/3gXi.gif', 'https://i.gifer.com/19wO.gif', 'https://i.gifer.com/3v9C.gif', 'https://i.gifer.com/Qu9x.gif', 'https://i.gifer.com/14pU.gif', 'https://i.gifer.com/hwr.gif', 'https://i.gifer.com/WUuf.gif', 'https://i.gifer.com/IEZf.gif', 'https://i.gifer.com/7BW.gif', 'https://i.gifer.com/c3g.gif', 'https://i.gifer.com/fyBd.gif', 'https://i.gifer.com/noq.gif', 'https://i.gifer.com/WKzd.gif', 'https://i.gifer.com/3aVN.gif', 'https://i.gifer.com/OSyd.gif', 'https://i.gifer.com/y2.gif', 'https://i.gifer.com/UMhr.gif', 'https://i.gifer.com/HFJ6.gif', 'https://i.gifer.com/aw.gif', 'https://i.gifer.com/6A89.gif', 'https://i.gifer.com/AEw5.gif', 'https://i.gifer.com/4GZ9.gif', 'https://i.gifer.com/O8kd.gif', 'https://i.gifer.com/JSJ.gif', 'https://i.gifer.com/Q3p.gif', 'https://i.gifer.com/967Q.gif', 'https://i.gifer.com/1kXE.gif', 'https://i.gifer.com/Nkfp.gif', 'https://i.gifer.com/Pvm.gif', 'https://i.gifer.com/EXUr.gif', 'https://i.gifer.com/Xhne.gif', 'https://i.gifer.com/Xhne.gif', 'https://i.gifer.com/MWJO.gif', 'https://i.gifer.com/fyI0.gif', 'https://i.gifer.com/c0M.gif', 'https://i.gifer.com/3VTL.gif', 'https://i.gifer.com/3ea7.gif']

list_2 = ["Вам повезет!","Эхх..Увы удача не на вашей стороне","Точно должно повезти","Спрячьтесь в шкаф на вас идет буря дерьма",
"Этот день был замечательный","Ты опять придешь ко мне неудачник.. Ахаха.."]


c = CurrencyRates()
prefix = '!'
client = commands.Bot(command_prefix = prefix)
client.remove_command('help')


@client.event
async def on_ready():
    print("Бот успешно подключен!")


@client.command(pass_context = True)
async def rand(ctx,arg):
    result = random.randrange(int(arg))
    await ctx.send(f"{ctx.message.author.mention}, Ваше случайное число:{result}")


@client.command(pass_context = True)
async def help(ctx):

    emb = discord.Embed(title  = 'Все команды LiriceL' ,colour = 0x008B8B)
    emb.add_field(name ='{}clear'.format(prefix),value = 'Очистка чата.')
    emb.add_field(name ='{}kick'.format(prefix),value = "Изгнание из Сервера.")
    emb.add_field(name ='{}ban'.format(prefix),value = "Блокирования пользователя.")
    emb.add_field(name ='{}unban'.format(prefix),value = "Разблокирования пользователя.")
    emb.add_field(name ='{}pog Любой город'.format(prefix),value = "Узнаеот погоду в любом городе.")
    emb.add_field(name ='{}dol'.format(prefix),value = "Курс Доллара.")
    emb.add_field(name ='{}wiki Любое слово'.format(prefix),value = "Ищет слово в Википедии.")
    emb.add_field(name ='{}cute'.format(prefix),value = "Кидает случайную гифку.")
    emb.add_field(name ='{}send @ник пользователя любое слово'.format(prefix),value = "Отправляет указанному пользователю сообщения.")
    emb.add_field(name ='{}repack'.format(prefix),value = "Отправляет сайт.")
    emb.add_field(name ='{}emoji'.format(prefix),value = "Гадание вашего дня.")
    emb.add_field(name ='{}rand число'.format(prefix),value = "Выпадает число из выбранного диапозона.")

    await ctx.send(embed = emb)



@client.command(pass_context = True)
async def pog(ctx,place):
    try:
        owm = OWM('660085338beccf764c6de212eb8f0ef8')
        observation = owm.weather_manager().weather_at_place(place)
        w = observation.weather
        t = w.temperature('celsius')
        t1 = t['temp']
        wi = w.wind()['speed']
        humi = w.humidity
        cl = w.clouds
        st = w.status
        await ctx.send(f"В {place} температура {t1}°C\nСкорость ветра: {wi}м\с\nВлажность: {humi}%\nОбщий прогноз: {st}")
    except:
        await ctx.send("Произошла ошибка!")



@client.command(pass_context = True)
async def dol(ctx):
    answer = c.get_rate('USD','RUB')
    await ctx.send(f"{ctx.message.author.mention}, Курс Доллора: {answer}")



@client.command(pass_context = True)
async def wiki(ctx,arg1):
    try:
        wikipedia.set_lang("RU")
        text = wikipedia.summary(arg1, sentences=4)
        await ctx.send(text)
    except:
        await ctx.send("Не удалось ничего найти, пишите конкретнее!")



@client.command(pass_context = True)
async def cute(ctx):
    rem = random.choice(list_1)
    await ctx.send(f"{ctx.message.author.mention}, Держи гифку\n{rem}")



@client.command(pass_context = True)
async def send(ctx,member:discord.Member,arg2):
    await member.send(f"{member.name}, {arg2}")



@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def clear(ctx,amount = 1000):
    await ctx.channel.purge(limit = amount)



@client.command(pass_context = True)
async def repack(ctx):
    emb = discord.Embed(title = "Online-Fix",colour= discord.Color.blue(),url = "https://online-fix.me/")
    emb.set_author(name = client.user.name,icon_url = client.user.avatar_url)
    emb.set_image(url = "https://www.kino-teatr.ru/art/2104/17910.jpg")
    now_date = datetime.datetime.now()
    emb.add_field(name = "Online-Fix",value = 'Time : {}'.format(now_date))
    await ctx.send(embed = emb)



@client.command(pass_context = True)
async def emoji(ctx):
    result_2 = random.choice(list_2)
    await ctx.send(f"Сегодня {ctx.message.author.mention} : {result_2}")



@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def kick(ctx,member:discord.Member,*,reason = None):
    await ctx.channel.purge(limit = 1)
    await member.kick(reason = reason)
    await ctx.send(f"Пользователь был удален из дискорд канала {member.mention}")



@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def ban(ctx,member:discord.Member,*,reason = None):
    await ctx.channel.purge(limit = 1)
    await member.ban(reason = reason)
    await ctx.send(f"Пользователь получил бан: {member.mention}")



@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()

    for ban_entry in banned_users:
        user = ban_entry.user

        await ctx.guild.unban(user)
        await ctx.send(f"Пользователь разблокирован: {user.mention}")

        return



client.run("ODA2ODIyNTA2MjkxMjY1NTM2.YBvCAw.jOWhipzO-HGTKmDysXw13_oMyRw")
