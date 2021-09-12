from random import shuffle
import asyncio
import discord
from discord.ext import commands
from discord.utils import get
from settings import *
import copy
import os
from dotenv import load_dotenv
from keep_alive import keep_alive
load_dotenv()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')

client = commands.Bot(command_prefix='$', help_command=None)

key = {
    'ma sói':872494848517763154,
    'sói nguyền':872494874413396018,
    'couple': 872494932336713828,
    'bảo vệ':872495019116879922, 
    'bán sói':872494986791387176,
    'tiên tri':872495086200565760,
    'phù thuỷ':872495057993859153,
    'thợ săn':872495103376240640,
    'cupid':872494905245708298,
    'thảo luận': 872488550954860587,
}

channels = {
    'ma sói':872024343029354526,
    'sói nguyền':872091054248177684,
    'couple': 872026916008374292, 
    'bảo vệ':872091236054478889 ,
    'bán sói':872090616971018260, 
    'tiên tri':872090741818667049, 
    'phù thuỷ':872090939395571752,
    'thợ săn':872090783619108914, 
    'cupid':872350367936020481,
    'thảo luận': 872104827541397515,
}

lop = {
    'ma sói':885082189631475742,
    'sói nguyền':885082165614882836,
    'couple': 885082217594892378, 
    'bảo vệ':885082269717524521 ,
    'bán sói':885082817007091743, 
    'tiên tri':885082252369879050, 
    'phù thuỷ':885082292748435466,
    'thợ săn':885082332984377374, 
    'cupid':885082205662097428, 
    'thảo luận':885829759261605938,
}

def check_player(lst):
    if len(set(lst)) >= 2:
        dict_value = {index: lst.count(index) for index in lst}
        target = max(dict_value, key = dict_value.get)
        value1 = dict_value[target]
        del dict_value[target]
        max2 = max(dict_value, key = dict_value.get)
        value2 = dict_value[max2]
        if value1 == value2:
            return None
        else:
            return target 
    elif len(set(lst)) == 1:
        dict_value = {index: lst.count(index) for index in lst}
        target = max(dict_value, key = dict_value.get)
        value1 = dict_value[target]
        return target
    elif len(lst) == 0:
        return None

@client.event
async def on_ready():
    print(f'{client.user.display_name} has connected to Discord!')

@client.command()
async def ping(ctx):
    await ctx.send("pong")

@client.command()
@commands.has_role('Quản trò')
async def clear(ctx, amount=50):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_role('Quản trò')
async def reset(ctx): 
    global info_death, werewolfs, dict_num_player, dict_role_player, num_players, roles, list_id,players, dict_player, dict_num_role, isdone, kick, lives, deaths, player_kick, live_death, couples, iscupid, blackwolf, curseguy, guard,  witch, seer, hunter, cupid, turn, fire, list_guarded, guarded, witch_kill, witch_rescure, isblackwolf, isseer, hunter_list, fire, player_death, list_werewolf_select, list_target, curseguyww, info_death,endgame, startgame
    general = client.get_channel(channels['thảo luận'])
    for member in werewolfs:
            channel = client.get_channel(channels['ma sói'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
    for member in couples:
            channel = client.get_channel(channels['couple'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite= perms)
    for member in blackwolf:
            channel = client.get_channel(channels['sói nguyền'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
    for member in curseguy:
            channel = client.get_channel(channels['bán sói'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
    for member in guard:
            channel = client.get_channel(channels['bảo vệ'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
    for member in witch:
            channel = client.get_channel(channels['phù thuỷ'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
    for member in seer:
            channel = client.get_channel(channels['tiên tri'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
    for member in hunter:
            channel = client.get_channel(channels['thợ săn'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
    for member in cupid:
            channel = client.get_channel(channels['cupid'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)        
    players.clear()
    info_death.clear()
    roles.clear()
    list_id.clear()
    dict_player.clear()
    dict_num_role.clear()
    dict_num_player.clear()
    dict_role_player.clear()
    list_vote_player.clear()
    num_vote_player.clear()
    live_death.clear()
    dict_value.clear()
    werewolfs.clear()
    blackwolf.clear()
    curseguy.clear()
    seer.clear()
    guard.clear()
    witch.clear()
    hunter.clear()
    cupid.clear()
    list_guarded.clear()
    list_target.clear()
    hunter_list.clear()
    list_werewolf_select.clear()
    hunter_list.clear()
    roles_in_game.clear()
    fire = False
    turn = 0
    witch_kill = 1
    witch_rescure = 1
    isblackwolf = False
    isseer = False
    player_death = None
    kick = False
    isdone = False
    iscupid = False
    guarded = False
    lives = 0
    deaths = 0
    player_kick = 0
    num_players = 0
    endgame = False
    startgame = False
    curseguyww = False
    info_death.clear()
    await general.send("Reset game mới")

@client.command()
@commands.has_role('Werewolf player')
async def addrole(ctx, *, role):
    global roles, num_players, players, endgame, roles_in_game
    await ctx.message.delete()
    endgame = False
    if startgame == False:
        roles = role.split(', ')
        roles_in_game = copy.copy(roles)
        num_players = len(roles)
        players = list(range(1,num_players+1))
        embed = discord.Embed(title="Roles", colour=discord.Color.blue())
        embed.add_field(name = f"Có {num_players} chức năng trong game", value = " - ".join(role for role in roles))
        await ctx.send(embed = embed)
    else:
        await ctx.send("Game đã được bắt đầu rồi!")

@client.command()
async def play(ctx):
    global kick
    general = client.get_channel(channels['thảo luận'])
    member = ctx.author
    role = get(ctx.guild.roles, name="Werewolf player")
    if role not in member.roles and kick == False:
        await member.add_roles(role, atomic=False)
        await general.send(f"{member.mention} đã tham gia vào game!")
    elif role in member.roles:
        await general.send("Bạn đã ở trong game rồi!")
    elif kick:
        await general.send("Game chưa kết thúc.")
    await ctx.message.delete()


@client.command()
async def quit(ctx):
    general = client.get_channel(channels['thảo luận'])
    member = ctx.author
    role = get(ctx.guild.roles, name="Werewolf player")
    if role in member.roles:
        await member.remove_roles(role, atomic=False)
        await general.send(f"{member.mention} đã thoát game.")
    else:
        await general.send("Bạn chưa tham gia vào game.")
    await ctx.message.delete()


@client.command()
@commands.has_role("Werewolf player")
async def getrole(ctx):
    werewolf_channel = client.get_channel(channels['ma sói'])
    blackwolf_channel = client.get_channel(channels['sói nguyền'])
    curseguy_channel = client.get_channel(channels['bán sói'])
    guard_channel = client.get_channel(channels['bảo vệ'])
    witch_channel = client.get_channel(channels['phù thuỷ'])
    seer_channel = client.get_channel(channels['tiên tri'])
    hunter_channel = client.get_channel(channels['thợ săn'])
    cupid_channel = client.get_channel(channels['cupid'])
    general = client.get_channel(channels['thảo luận'])

    global roles_in_game, startgame, roles, players, dict_player, dict_num_player, dict_num_role, dict_role_player, blackwolf, curseguy, guard,  witch, seer, hunter, werewolfs, cupid, num_players

    shuffle(roles)
    shuffle(players)
    await ctx.message.delete()
    if len(roles_in_game) == 0:
        await ctx.send("Quản trò chưa setup xong!")
    if len(roles) == 0 and startgame == True:
        await ctx.send("Game đã được được bắt đầu")
    elif len(roles) != 0 and startgame == False:
        if ctx.author.id not in list_id:
            role_player = roles.pop()
            player = players.pop()
            if role_player == "Sói thường":
                dict_num_role[player] = role_player
                dict_role_player[ctx.author] = role_player
                werewolfs.append(ctx.author)
                list_id.append(ctx.author.id)
                dict_player[player] = ctx.author
                dict_num_player[ctx.author] = player

                perms1 = werewolf_channel.overwrites_for(ctx.author)
                perms1.view_channel = True
                await werewolf_channel.set_permissions(ctx.author, overwrite=perms1)


                await ctx.message.author.send("Chức năng của bạn là Sói thường")
            elif role_player == "Sói nguyền":
                dict_num_role[player] = role_player
                dict_role_player[ctx.author] = role_player
                werewolfs.append(ctx.author)
                list_id.append(ctx.author.id)
                dict_player[player] = ctx.author
                dict_num_player[ctx.author] = player

                perms1 = werewolf_channel.overwrites_for(ctx.author)
                perms1.view_channel = True
                await werewolf_channel.set_permissions(ctx.author, overwrite=perms1)

                perms2 = blackwolf_channel.overwrites_for(ctx.author)
                perms2.view_channel = True
                await blackwolf_channel.set_permissions(ctx.author, overwrite=perms2)

                blackwolf.append(ctx.author)
                await ctx.message.author.send("Chức năng của bạn là Sói nguyền")
            elif role_player == "Bán sói":
                dict_num_role[player] = role_player
                dict_role_player[ctx.author] = role_player
                list_id.append(ctx.author.id)
                dict_player[player] = ctx.author
                dict_num_player[ctx.author] = player

                perms3 = curseguy_channel.overwrites_for(ctx.author)
                perms3.view_channel = True
                await curseguy_channel.set_permissions(ctx.author, overwrite=perms3)

                await ctx.message.author.send("Chức năng của bạn là Bán sói")
                curseguy.append(ctx.author)
            elif role_player == "Bảo vệ":
                dict_num_role[player] = role_player
                dict_role_player[ctx.author] = role_player
                list_id.append(ctx.author.id)
                dict_player[player] = ctx.author
                dict_num_player[ctx.author] = player

                perms4 = guard_channel.overwrites_for(ctx.author)
                perms4.view_channel = True
                await guard_channel.set_permissions(ctx.author, overwrite=perms4)

                await ctx.message.author.send("Chức năng của bạn là Bảo vệ")
                guard.append(ctx.author)
            elif role_player == "Cupid":
                dict_num_role[player] = role_player
                dict_role_player[ctx.author] = role_player
                list_id.append(ctx.author.id)
                dict_player[player] = ctx.author
                dict_num_player[ctx.author] = player

                perms8 = cupid_channel.overwrites_for(ctx.author)
                perms8.view_channel = True
                await cupid_channel.set_permissions(ctx.author, overwrite=perms8)

                await ctx.message.author.send("Chức năng của bạn là Cupid")
                cupid.append(ctx.author)

            elif role_player == "Tiên tri":
                dict_num_role[player] = role_player
                dict_role_player[ctx.author] = role_player
                list_id.append(ctx.author.id)
                dict_player[player] = ctx.author
                dict_num_player[ctx.author] = player

                perms6 = seer_channel.overwrites_for(ctx.author)
                perms6.view_channel = True
                await seer_channel.set_permissions(ctx.author, overwrite=perms6)

                await ctx.message.author.send("Chức năng của bạn là Tiên tri")
                seer.append(ctx.author)
            elif role_player == "Phù thuỷ":
                dict_num_role[player] = role_player
                dict_role_player[ctx.author] = role_player
                list_id.append(ctx.author.id)
                dict_player[player] = ctx.author
                dict_num_player[ctx.author] = player

                perms5 = witch_channel.overwrites_for(ctx.author)
                perms5.view_channel = True
                await witch_channel.set_permissions(ctx.author, overwrite=perms5)

                await ctx.message.author.send("Chức năng của bạn là Phù thuỷ")
                witch.append(ctx.author)
            elif role_player == "Thợ săn":
                dict_num_role[player] = role_player
                dict_role_player[ctx.author] = role_player
                list_id.append(ctx.author.id)
                dict_player[player] = ctx.author
                dict_num_player[ctx.author] = player

                perms7 = hunter_channel.overwrites_for(ctx.author)
                perms7.view_channel = True
                await hunter_channel.set_permissions(ctx.author, overwrite=perms7)

                await ctx.message.author.send("Chức năng của bạn là Thợ săn")
                hunter.append(ctx.author)
            else:
                dict_num_role[player] = role_player
                dict_role_player[ctx.author] = role_player
                list_id.append(ctx.author.id)
                dict_player[player] = ctx.author
                dict_num_player[ctx.author] = player

                await ctx.message.author.send("Chức năng của bạn là Dân làng")
            await ctx.send(f"{ctx.author.mention} là Player số {player}")
        else:
            await ctx.send("Bạn đã nhận chức năng của mình rồi!")
    if len(dict_player) == num_players and startgame == False and num_players != 0:
        startgame = True
        await general.send("Đã đủ người chơi, Game xin được bắt đầu!")
        await danhsach(general)
        if "Cupid" in roles_in_game:
            await turnround(ctx,0)
        else:
            await turnround(ctx,1)


@client.command()
@commands.has_role("Werewolf player")
async def skipvote(ctx):
    global list_vote_player, num_vote_player
    general = client.get_channel(channels['thảo luận'])
    if voting_time:
        if ctx.author.id not in list_vote_player:
            list_vote_player.append(ctx.author.id)
            num_vote_player = num_vote_player
            await general.send(f"{ctx.author.display_name} đã skip vote!")
        else:
            await general.send(f"{ctx.author.display_name} đã vote hoặc skip vote rồi!")
    else:
        await general.send("Chưa đến thời gian để biểu quyết")
    await ctx.message.delete()


@client.command()
@commands.has_role("Werewolf player")
async def vote(ctx, num_player):
    num_player = int(num_player)
    global num_players, list_vote_player, dict_player
    general = client.get_channel(channels['thảo luận'])
    if num_players != 0 and voting_time:
        member = dict_player[num_player]
        if num_player in dict_player and ctx.author.id not in list_vote_player:
            num_vote_player.append(num_player)
            list_vote_player.append(ctx.author.id)
            await general.send(f"{ctx.author.display_name} đã chọn {member.mention} là người lên dàn")
        elif ctx.author.id in list_vote_player:
            await general.send(f"{ctx.author.display_name} đã vote hoặc skip vote rồi!")
        elif num_player not in dict_player:
            await general.send("Player không hợp lệ")
    elif num_players == 0:
        await general.send("Game chưa bắt đầu để vote!")
    elif voting_time == False:
        await general.send("Chưa đến thời gian để biểu quyết")
    await ctx.message.delete()


@client.command()
@commands.has_role("Quản trò")
async def kiemtra(ctx):
    global num_vote_player, isdone, dict_value, player_kick
    general = client.get_channel(channels['thảo luận'])
    if len(set(num_vote_player)) >= 2:
        dict_value = {index: num_vote_player.count(index) for index in num_vote_player}
        player_kick = max(dict_value, key = dict_value.get)
        value1 = dict_value[player_kick]
        del dict_value[player_kick]
        max2 = max(dict_value, key = dict_value.get)
        value2 = dict_value[max2]
        if value1 == value2:
            await general.send(f"Sáng hôm nay chúng ta không có ai bị lên dàn bởi có 2 người trở lên sỡ hữu cùng phiếu vote!")
            num_vote_player.clear()
            list_vote_player.clear()
            dict_value.clear()
            isdone = False
        else:
            await general.send(f"Sáng hôm nay chúng ta có một người bị lên dàn. Đó là {dict_player[player_kick].mention} sở hữu {value1} phiếu vote")
            num_vote_player.clear()
            list_vote_player.clear()
            dict_value.clear()
            isdone = True
    elif len(set(num_vote_player)) == 1:
        dict_value = {index: num_vote_player.count(index) for index in num_vote_player}
        player_kick = max(dict_value, key = dict_value.get)
        value1 = dict_value[player_kick]
        await general.send(f"Sáng hôm nay chúng ta có một người bị lên dàn. Đó là {dict_player[player_kick].mention} sở hữu {value1} phiếu vote")
        num_vote_player.clear()
        list_vote_player.clear()
        dict_value.clear()
        isdone = True
    elif len(num_vote_player) == 0:
        await general.send("Sáng hôm nay chúng ta không có ai bị lên dàn bởi mọi người đã skip vote!")
        num_vote_player.clear()
        list_vote_player.clear()
        dict_value.clear()
        isdone = False
    

@client.command()
@commands.has_role("Werewolf player")
async def song(ctx):
    general = client.get_channel(channels['thảo luận'])
    global lives, live_death, dict_player
    if isdone and dict_player[player_kick].name != ctx.author.name and ctx.author.id not in live_death:
        lives += 1
        live_death.append(ctx.author.id)
        await general.send(f"{ctx.author.display_name} đã vote Sống cho {dict_player[player_kick].mention}")
    elif dict_player[player_kick].name == ctx.author.name:
        await general.send("Bạn không thể bầu sống hoặc chết cho bản thân mình")
    elif ctx.author.id in live_death:
        await general.send("Bạn đã biểu quyết rồi!")
    elif isdone == False:
        await general.send("Không có cuộc biểu quyết sống/chết nào cả!")
    await ctx.message.delete()


@client.command()
@commands.has_role("Werewolf player")
async def chet(ctx):
    general = client.get_channel(channels['thảo luận'])
    global deaths, live_death, dict_player
    if isdone and dict_player[player_kick].name != ctx.author.name and ctx.author.id not in live_death:
        deaths += 1
        live_death.append(ctx.author.id)
        await general.send(f"{ctx.author.display_name} đã vote Chết cho {dict_player[player_kick].mention}")
    elif dict_player[player_kick].name == ctx.author.name:
        await general.send("Bạn không thể bầu sống hoặc chết cho bản thân mình")
    elif ctx.author.id in live_death:
        await general.send("Bạn đã biểu quyết rồi!")
    elif isdone == False:
        await general.send("Không có cuộc biểu quyết sống/chết nào cả!")
    await ctx.message.delete()


@client.command()
@commands.has_role("Quản trò")
async def ketqua(ctx):
    general = client.get_channel(channels['thảo luận'])
    global hunter_list, list_guarded, endgame, lives, deaths, player_kick, kick, dict_player,live_death, isdone, voting_time, fire, guarded,player_death, isseer, turn, info_death
    role = get(ctx.guild.roles, name="Werewolf player")
    if lives >= deaths and isdone:
        member = dict_player[player_kick]
        await general.send(f"{dict_player[player_kick].mention} sống với số biểu quyết {lives} Sống và {deaths} Chết")
    elif lives < deaths and isdone:
        member = dict_player[player_kick]
        await general.send(f"{dict_player[player_kick].mention} chết với số biểu quyết {lives} Sống và {deaths} Chết")
        await member.remove_roles(role, atomic=False)
        dict_player.pop(player_kick)
        kick = True
        if member in werewolfs and member not in blackwolf:
            werewolf_channel = client.get_channel(channels['ma sói'])
            perms = werewolf_channel.overwrites_for(member)
            perms.view_channel = False
            await werewolf_channel.set_permissions(member, overwrite=perms)
            werewolfs.remove(member)
        elif member in couples and member not in werewolfs:
            couple_channel = client.get_channel(channels['couple'])
            perms = couple_channel.overwrites_for(member)
            perms.view_channel = False
            await couple_channel.set_permissions(member, overwrite= perms)
            couples.remove(member)
            if len(couples) == 1:
                for member in couples:
                    await thubai(ctx, member)
        elif member in couples and member in werewolfs:
            couple_channel = client.get_channel(channels['couple'])
            perms_couple = couple_channel.overwrites_for(member)
            perms_couple.view_channel = False
            await couple_channel.set_permissions(member, overwrite= perms_couple)
            couples.remove(member)
            werewolf_channel = client.get_channel(channels['ma sói'])
            perms_werewolf = werewolf_channel.overwrites_for(member)
            perms_werewolf.view_channel = False
            await werewolf_channel.set_permissions(member, overwrite=perms_werewolf)
            werewolfs.remove(member)
            if len(couples) == 1:
                for member in couples:
                    await thubai(ctx, member)
        elif member in blackwolf:
            werewolf_channel = client.get_channel(channels['ma sói'])
            perms_werewolf = werewolf_channel.overwrites_for(member)
            perms_werewolf.view_channel = False
            await werewolf_channel.set_permissions(member, overwrite=perms_werewolf)
            blackwolf_channel = client.get_channel(channels['sói nguyền'])
            perms_blackwolf = blackwolf_channel.overwrites_for(member)
            perms_blackwolf.view_channel = False
            await blackwolf_channel.set_permissions(member, overwrite=perms_blackwolf)
            blackwolf.remove(member)
            werewolfs.remove(member)
        elif member in curseguy and member not in werewolfs:
            channel = client.get_channel(channels['bán sói'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            curseguy.remove(member)
        elif member in curseguy and member in werewolfs:
            channel = client.get_channel(channels['bán sói'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            curseguy.remove(member)
            werewolfs.remove(member)
        elif member in guard and member not in werewolfs:
            channel = client.get_channel(channels['bảo vệ'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            guard.remove(member)
            list_guarded.clear()
        elif member in guard and member in werewolfs:
            channel = client.get_channel(channels['bảo vệ'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            guard.remove(member)
            werewolfs.remove(member)
            list_guarded.clear()
        elif member in witch and member not in werewolfs:
            channel = client.get_channel(channels['phù thuỷ'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            witch.remove(member)
        elif member in witch and member in werewolfs:
            channel = client.get_channel(channels['phù thuỷ'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            witch.remove(member)
            werewolfs.remove(member)
        elif member in seer and member not in werewolfs:
            channel = client.get_channel(channels['tiên tri'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            seer.remove(member)
        elif member in seer and member in werewolfs:
            channel = client.get_channel(channels['tiên tri'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            seer.remove(member)
            werewolfs.remove(member)
        elif member in hunter and member not in werewolfs:
            channel = client.get_channel(channels['thợ săn'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            hunter.remove(member)
            await thubai(ctx, hunter_list[-1])
        elif member in hunter and member in werewolfs:
            channel = client.get_channel(channels['thợ săn'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            hunter.remove(member) 
            werewolfs.remove(member)
        elif member in cupid and member not in werewolfs:
            channel = client.get_channel(channels['cupid'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            cupid.remove(member)
        elif member in cupid and member in werewolfs:
            channel = client.get_channel(channels['cupid'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            cupid.remove(member)
            werewolfs.remove(member)

    elif isdone == False:
        await general.send("Sáng nay không ai chết vì không có biểu quyết!")

    if len(werewolfs) >= (len(dict_player) - len(werewolfs)) and len(werewolfs) != 0 and endgame == False:
        await general.send("Endgame, Sói thắng bởi vì số sói hiện tại bằng số dân!")
        await mod(ctx)
        await reset(ctx)
        endgame = True
    if len(werewolfs) == 0 and endgame == False:
        await general.send("Endgame, Dân thắng!")
        await mod(ctx)
        await reset(ctx)
        endgame = True

    if len(cupid) != 0 and endgame == False:
        player1, player2 = couples
        if (player1 in werewolfs and player2 not in werewolfs) or (player1 not in werewolfs and player2 in werewolfs):
            if len(couples) >= len(dict_player) - len(couples):
                await general.send("Endgame, Cặp đôi phe thứ 3 chiến thắng!")
                await mod(ctx)
                await reset(ctx)
                endgame = True

    live_death.clear()   
    info_death.clear()
    lives = 0
    deaths = 0
    player_kick = 0
    isdone = False
    voting_time = False
    fire = False
    guarded = False
    player_death = None
    isseer = False
    list_target.clear()
    list_werewolf_select.clear()
    if endgame == False:
        await asyncio.sleep(10)
        await general.send("Đêm đã xuống mời các bạn đi ngủ")
        await turnround(ctx, 1)

@client.command()
@commands.has_role("Werewolf player")
async def ghepdoi(ctx, arg1, arg2):
    global couples, iscupid, turn
    general = client.get_channel(channels['thảo luận'])
    couple_channel = client.get_channel(channels['couple'])
    cupid_channel = client.get_channel(channels['cupid'])
    if dict_role_player[ctx.author] == "Cupid" and iscupid == False:
        if int(arg1) > num_players or int(arg2) > num_players:
            await cupid_channel.send("Số player không phù hợp mời bạn chọn lại")
        elif int(arg1) == int(arg2):
            await cupid_channel.send("Bạn phải ghép 2 người khác nhau")
        else:
            player1 = dict_player[int(arg1)]
            player2 = dict_player[int(arg2)]
            couples.append(player1)
            couples.append(player2)
            for couple in couples:
                perms = couple_channel.overwrites_for(couple)
                perms.view_channel = True
                await couple_channel.set_permissions(couple, overwrite=perms)
            await cupid_channel.send(f"Bạn đã ghép Player {dict_player[int(arg1)].display_name} và Player {dict_player[int(arg2)].display_name} thành một cặp")
            await couple_channel.send(f"Cupid đã ghép Player {dict_player[int(arg1)].mention} và Player {dict_player[int(arg2)].mention} thành một cặp")
            iscupid = True
            await turnround(ctx, 2)
    elif dict_role_player[ctx.author] != "Cupid":
        await ctx.message.author.send("Bạn không phải là cupid để ghép đượp cặp đôi")
    elif iscupid:
        await ctx.message.author.send("Cupid đã ghép cặp đôi cho mình rồi!")
    await ctx.message.delete()


@client.command()
@commands.has_role("Quản trò")
async def thubai(ctx, member: discord.Member):
    global kick, dict_player, dict_num_player, list_guarded, hunter_list, endgame, startgame, couples, blackwolf, curseguy, guard, witch, seer, hunter, cupid
    general = client.get_channel(channels['thảo luận'])
    role = get(ctx.guild.roles, name="Werewolf player")
    if dict_num_player[member] in dict_player:
        dict_player.pop(dict_num_player[member])
        kick = True
        await member.remove_roles(role, atomic= False)
        await general.send(f"{member.mention} đã chết vào sáng hôm nay")
        if member in werewolfs and member not in blackwolf:
            channel = client.get_channel(channels['ma sói'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            werewolfs.remove(member)
        elif member in couples and member not in werewolfs:
            channel = client.get_channel(channels['couple'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite= perms)
            couples.remove(member)
            if len(couples) == 1:
                for member in couples:
                    await thubai(ctx, member)
        elif member in couples and member in werewolfs:
            couple_channel = client.get_channel(channels['couple'])
            perms_couple = couple_channel.overwrites_for(member)
            perms_couple.view_channel = False
            await couple_channel.set_permissions(member, overwrite= perms_couple)
            couples.remove(member)
            werewolf_channel = client.get_channel(channels['ma sói'])
            perms_werewolf = werewolf_channel.overwrites_for(member)
            perms_werewolf.view_channel = False
            await werewolf_channel.set_permissions(member, overwrite=perms_werewolf)
            werewolfs.remove(member)
            if len(couples) == 1:
                for member in couples:
                    await thubai(ctx, member)
        elif member in blackwolf:
            channel = client.get_channel(channels['sói nguyền'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            blackwolf.remove(member)
            werewolfs.remove(member)
        elif member in curseguy and member not in werewolfs:
            channel = client.get_channel(channels['bán sói'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            curseguy.remove(member)
        elif member in curseguy and member in werewolfs:
            channel = client.get_channel(channels['bán sói'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            curseguy.remove(member)
            werewolfs.remove(member)
        elif member in guard and member not in werewolfs:
            channel = client.get_channel(channels['bảo vệ'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            list_guarded = [0]
            guard.remove(member)
        elif member in guard and member in werewolfs:
            channel = client.get_channel(channels['bảo vệ'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            list_guarded = [0]
            guard.remove(member)
            werewolfs.remove(member)
        elif member in witch and member not in werewolfs:
            channel = client.get_channel(channels['phù thuỷ'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            witch.remove(member)
        elif member in witch and member in werewolfs:
            channel = client.get_channel(channels['phù thuỷ'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            witch.remove(member)
            werewolfs.remove(member)
        elif member in seer and member not in werewolfs:
            channel = client.get_channel(channels['tiên tri'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            seer.remove(member)
        elif member in seer and member in werewolfs:
            channel = client.get_channel(channels['tiên tri'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            seer.remove(member)
            werewolfs.remove(member)
        elif member in hunter and member not in werewolfs:
            channel = client.get_channel(channels['thợ săn'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            hunter.remove(member)
            await thubai(ctx, hunter_list[-1])
        elif member in hunter and member in werewolfs:
            channel = client.get_channel(channels['thợ săn'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            hunter.remove(member) 
            werewolfs.remove(member)
            await thubai(ctx, hunter_list[-1])
        elif member in cupid and member not in werewolfs:
            channel = client.get_channel(channels['cupid'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            cupid.remove(member)
        elif member in cupid and member in werewolfs:
            channel = client.get_channel(channels['cupid'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            cupid.remove(member)
            werewolfs.remove(member)
    else:
        await general.send("Player không hợp lệ")

    if len(werewolfs) >= (len(dict_player) - len(werewolfs)) and endgame == False and len(werewolfs) != 0:
        await general.send("Endgame, Sói thắng bởi vì số sói hiện tại bằng số dân!")
        await mod(ctx)
        await reset(ctx)
        endgame = True

    if len(werewolfs) == 0 and endgame == False:
        await general.send("Endgame, Dân thắng!")
        await mod(ctx)
        await reset(ctx)
        endgame = True

    if len(couples) == 2 and endgame == False:
        player1, player2 = couples
        if (player1 in werewolfs and player2 not in werewolfs) or (player1 not in werewolfs and player2 in werewolfs):
            if len(couples) >= len(dict_player) - len(couples):
                await general.send("Endgame, Cặp đôi phe thứ 3 chiến thắng!")
                await mod(ctx)
                await reset(ctx)
                endgame = True

@client.command()
@commands.has_role("Werewolf player")
async def danhsach(ctx):
    global dict_player
    list_player = dict_player.keys()
    if len(list_player) != 0:
        embed = discord.Embed(title="Player hiện có", colour=discord.Color.green())
        for i in sorted(list_player):
            embed.add_field(name = f"Player số {i}", value=f"Tên player: {dict_player[i].display_name}", inline=False)
        await ctx.send(embed = embed)
    else:
        await ctx.send("Game chưa bắt đầu")


@client.command()
@commands.has_role("Quản trò")
async def mod(ctx):
    global dict_role_player
    general = client.get_channel(channels['thảo luận'])
    role_player = dict_role_player.keys()
    if len(role_player) != 0:
        embed = discord.Embed(title="Role player", colour=discord.Color.green())
        for i in role_player:
            embed.add_field(name = f"Player", value = f"Number: {dict_num_player[i]}   -   Name: {i.display_name}   -   Role: {dict_role_player[i]}", inline= False)
        await general.send(embed = embed)
    else:
        await general.send("Game chưa bắt đầu")

@client.command()
@commands.has_role("Quản trò")
async def mute_werewolf(ctx):
    for member in werewolfs:
        channel = client.get_channel(channels['ma sói'])
        perms = channel.overwrites_for(member)
        perms.view_channel = False
        await channel.set_permissions(member, overwrite=perms)
@client.command()
@commands.has_role("Quản trò")
async def mute_couple(ctx):         
    for member in couples:
        channel = client.get_channel(channels['couple'])
        perms = channel.overwrites_for(member)
        perms.view_channel = False
        await channel.set_permissions(member, overwrite= perms)
@client.command()
@commands.has_role("Quản trò")
async def mute_blackwolf(ctx):
    for member in blackwolf:
        channel = client.get_channel(channels['sói nguyền'])
        perms = channel.overwrites_for(member)
        perms.view_channel = False
        await channel.set_permissions(member, overwrite=perms)
@client.command()
@commands.has_role("Quản trò")
async def mute_curseguy(ctx):
    for member in curseguy:
        channel = client.get_channel(channels['bán sói'])
        perms = channel.overwrites_for(member)
        perms.view_channel = False
        await channel.set_permissions(member, overwrite=perms)
@client.command()
@commands.has_role("Quản trò")
async def mute_guard(ctx):
    for member in guard:
        channel = client.get_channel(channels['bảo vệ'])
        perms = channel.overwrites_for(member)
        perms.view_channel = False
        await channel.set_permissions(member, overwrite=perms)
@client.command()
@commands.has_role("Quản trò")
async def mute_witch(ctx):
    for member in witch:
        channel = client.get_channel(channels['phù thuỷ'])
        perms = channel.overwrites_for(member)
        perms.view_channel = False
        await channel.set_permissions(member, overwrite=perms)
@client.command()
@commands.has_role("Quản trò")
async def mute_seer(ctx):
    for member in seer:
        channel = client.get_channel(channels['tiên tri'])
        perms = channel.overwrites_for(member)
        perms.view_channel = False
        await channel.set_permissions(member, overwrite=perms)
@client.command()
@commands.has_role("Quản trò")
async def mute_hunter(ctx):
    for member in hunter:
        channel = client.get_channel(channels['thợ săn'])
        perms = channel.overwrites_for(member)
        perms.view_channel = False
        await channel.set_permissions(member, overwrite=perms)
@client.command()
@commands.has_role("Quản trò")
async def mute_cupid(ctx):
    for member in cupid:
        channel = client.get_channel(channels['cupid'])
        perms = channel.overwrites_for(member)
        perms.view_channel = False
        await channel.set_permissions(member, overwrite=perms)

@client.command()
@commands.has_role("Quản trò")
async def unmute_werewolf(ctx):
    for member in werewolfs:
        channel = client.get_channel(channels['ma sói'])
        perms = channel.overwrites_for(member)
        perms.view_channel = True
        await channel.set_permissions(member, overwrite=perms)
@client.command()
@commands.has_role("Quản trò")
async def unmute_couple(ctx):
    for member in couples:
        channel = client.get_channel(channels['couple'])
        perms = channel.overwrites_for(member)
        perms.view_channel = True
        await channel.set_permissions(member, overwrite= perms)
@client.command()
@commands.has_role("Quản trò")
async def unmute_blackwolf(ctx):
    for member in blackwolf:
        channel = client.get_channel(channels['sói nguyền'])
        perms = channel.overwrites_for(member)
        perms.view_channel = True
        await channel.set_permissions(member, overwrite=perms)
@client.command()
@commands.has_role("Quản trò")
async def unmute_curseguy(ctx):
    for member in curseguy:
        channel = client.get_channel(channels['bán sói'])
        perms = channel.overwrites_for(member)
        perms.view_channel = True
        await channel.set_permissions(member, overwrite=perms)
@client.command()
@commands.has_role("Quản trò")
async def unmute_guard(ctx):
    for member in guard:
        channel = client.get_channel(channels['bảo vệ'])
        perms = channel.overwrites_for(member)
        perms.view_channel = True
        await channel.set_permissions(member, overwrite=perms)
@client.command()
@commands.has_role("Quản trò")
async def unmute_witch(ctx):
    for member in witch:
        channel = client.get_channel(channels['phù thuỷ'])
        perms = channel.overwrites_for(member)
        perms.view_channel = True
        await channel.set_permissions(member, overwrite=perms)
@client.command()
@commands.has_role("Quản trò")
async def unmute_seer(ctx):
    for member in seer:
        channel = client.get_channel(channels['tiên tri'])
        perms = channel.overwrites_for(member)
        perms.view_channel = True
        await channel.set_permissions(member, overwrite=perms)
@client.command()
@commands.has_role("Quản trò")
async def unmute_hunter(ctx):
    for member in hunter:
        channel = client.get_channel(channels['thợ săn'])
        perms = channel.overwrites_for(member)
        perms.view_channel = True
        await channel.set_permissions(member, overwrite=perms)
@client.command()
@commands.has_role("Quản trò")
async def unmute_cupid(ctx):
    for member in cupid:
        channel = client.get_channel(channels['cupid'])
        perms = channel.overwrites_for(member)
        perms.view_channel = True
        await channel.set_permissions(member, overwrite=perms)

@client.command()
@commands.has_role("Quản trò")
async def thaoluan(ctx):
    general = client.get_channel(channels['thảo luận'])
    global voting_time
    voting_time = True
    await general.send("Thời gian thảo luận và vote bắt đầu!")

@client.command()
@commands.has_role("Quản trò")
async def voting(ctx):
    general = client.get_channel(channels['thảo luận'])
    global voting_time
    voting_time = True
    await general.send("Thời gian vote bắt đầu!")

@client.command()
@commands.has_role("Quản trò")
async def songhoacchet(ctx):
    general = client.get_channel(channels['thảo luận'])
    await general.send("Thời gian biểu quyết sống hoặc chết bắt đầu!")

@client.command()
@commands.has_role("Quản trò")
async def makeww(ctx, member: discord.Member):
    dm_channel = await member.create_dm()
    await dm_channel.send("Bạn đã hoá sói!, Bạn sẽ thấy channel của ma sói vào đêm sau!")

@client.command()
@commands.has_role("Werewolf player")
async def can(ctx, num_player):
    await ctx.message.delete()
    global list_target, list_werewolf_select, player_death, werewolfs, list_guarded, curseguyww, witch_rescure, info_death, isblackwolf, endgame
    num_player = int(num_player)
    if ctx.author not in list_werewolf_select and ctx.author in werewolfs and num_player in dict_player and dict_player[num_player] not in werewolfs:
        list_werewolf_select.append(ctx.author)
        list_target.append(num_player)
        await ctx.send(f"{ctx.author.display_name} đã chọn Player {dict_player[num_player].display_name} là người để cắn!")
    elif ctx.author in list_werewolf_select and ctx.author in werewolfs and num_player in dict_player:
        await ctx.send("Bạn đã chọn người để cắn rồi!, Không thể chọn lại")
    elif ctx.author not in werewolfs:
        await ctx.send("Bạn không phải là ma sói để có thể cắn người!")
    elif ctx.author not in list_werewolf_select and ctx.author in werewolfs and num_player not in dict_player:
        await ctx.send("Player không hợp lệ, Vui lòng chọn lại người để cắn")
    elif ctx.author not in list_werewolf_select and ctx.author in werewolfs and dict_player[num_player] in werewolfs and num_player in dict_player:
        await ctx.send("Sói không thể cắn Sói")    
    if len(list_target) == len(werewolfs):
        targeted = check_player(list_target)
        if targeted == None:
            await ctx.send(f"Sẽ không có người chết bởi sói vì sói không thống nhất ý kiến")
        else:
            await ctx.send(f"Lấy theo số đông, Người bị đàn sói cắn đêm nay là Player {dict_player[targeted].display_name}")
        if targeted is None:
            player_death = None
        else:
            if "Bảo vệ" in dict_role_player.values() and "Bán sói" in dict_role_player.values():
                if dict_num_role[targeted] == "Bán sói" and list_guarded[-1] != targeted and curseguyww == False:
                    werewolfs.append(dict_player[targeted])
                    await makeww(ctx, dict_player[targeted])
                    player_death = None
                    curseguyww = True
                elif list_guarded[-1] == targeted:
                    player_death = None
                else:
                    player_death = targeted
                    if "Sói nguyền" in roles_in_game and "Phù thuỷ" in roles_in_game and witch_rescure == 0 and isblackwolf == True:
                        info_death.append(dict_player[player_death])
                    elif "Sói nguyền" not in roles_in_game and "Phù thuỷ" not in roles_in_game:
                        info_death.append(dict_player[player_death])
                    elif "Sói nguyền" in roles_in_game and "Phù thuỷ" not in roles_in_game and isblackwolf == True:
                        info_death.append(dict_player[player_death])
                    elif "Sói nguyền" not in roles_in_game and "Phù thuỷ" in roles_in_game and witch_rescure == 0:
                        info_death.append(dict_player[player_death]) 
            elif "Bảo vệ" in dict_role_player.values() and "Bán sói" not in dict_role_player.values():
                if targeted == list_guarded[-1]:
                    player_death = None
                else:
                    player_death = targeted
                    if "Sói nguyền" in roles_in_game and "Phù thuỷ" in roles_in_game and witch_rescure == 0 and isblackwolf == True:
                        info_death.append(dict_player[player_death])
                    elif "Sói nguyền" not in roles_in_game and "Phù thuỷ" not in roles_in_game:
                        info_death.append(dict_player[player_death])
                    elif "Sói nguyền" in roles_in_game and "Phù thuỷ" not in roles_in_game and isblackwolf == True:
                        info_death.append(dict_player[player_death])
                    elif "Sói nguyền" not in roles_in_game and "Phù thuỷ" in roles_in_game and witch_rescure == 0:
                        info_death.append(dict_player[player_death])
            elif "Bảo vệ" not in dict_role_player.values() and "Bán sói" in dict_role_player.values():
                if dict_num_role[targeted] == "Bán sói" and curseguyww == False:
                    werewolfs.append(dict_player[targeted])
                    await makeww(ctx, dict_player[targeted])
                    player_death = None
                    curseguyww = True
                else:
                    player_death = targeted
                    if "Sói nguyền" in roles_in_game and "Phù thuỷ" in roles_in_game and witch_rescure == 0 and isblackwolf == True:
                        info_death.append(dict_player[player_death])
                    elif "Sói nguyền" not in roles_in_game and "Phù thuỷ" not in roles_in_game:
                        info_death.append(dict_player[player_death])
                    elif "Sói nguyền" in roles_in_game and "Phù thuỷ" not in roles_in_game and isblackwolf == True:
                        info_death.append(dict_player[player_death])
                    elif "Sói nguyền" not in roles_in_game and "Phù thuỷ" in roles_in_game and witch_rescure == 0:
                        info_death.append(dict_player[player_death])                      
            elif "Bảo vệ" not in dict_role_player.values() and "Bán sói" not in dict_role_player.values():
                player_death = targeted
                if "Sói nguyền" in roles_in_game and "Phù thuỷ" in roles_in_game and witch_rescure == 0 and isblackwolf == True:
                    info_death.append(dict_player[player_death])
                elif "Sói nguyền" not in roles_in_game and "Phù thuỷ" not in roles_in_game:
                    info_death.append(dict_player[player_death])
                elif "Sói nguyền" in roles_in_game and "Phù thuỷ" not in roles_in_game and isblackwolf == True:
                    info_death.append(dict_player[player_death])
                elif "Sói nguyền" not in roles_in_game and "Phù thuỷ" in roles_in_game and witch_rescure == 0:
                    info_death.append(dict_player[player_death])                

@client.command()
@commands.has_role("Werewolf player")
async def nguyen(ctx):
    global isblackwolf, player_death
    if isblackwolf == False and player_death is not None and ctx.author in blackwolf:
        await ctx.send(f"Bạn đã nguyền Player {dict_player[player_death].display_name} thành sói, Họ sẽ dậy cùng sói và đêm tiếp theo!.")
        werewolfs.append(dict_player[player_death])
        werewolf_channel = client.get_channel(channels['ma sói'])
        perms = werewolf_channel.overwrites_for(dict_player[player_death])
        perms.view_channel = True
        await werewolf_channel.set_permissions(dict_player[player_death], overwrite=perms)
        await makeww(ctx, dict_player[player_death])
        isblackwolf = True
        player_death = None
    elif isblackwolf == True and ctx.author in blackwolf:
        await ctx.send("Bạn đã nguyền một người rồi, Không thể nguyền thêm nữa!")
    elif isblackwolf == False and player_death is None and ctx.author in blackwolf:
        await ctx.send("Bạn không thể nguyền người này thành sói!")
    elif ctx.author not in blackwolf:
        await ctx.send("Bạn không phải là sói nguyền!")
    await ctx.message.delete()


@client.command()
@commands.has_role("Werewolf player")
async def khongnguyen(ctx):
    global player_death
    if ctx.author in blackwolf and isblackwolf == False and player_death is not None:
        await ctx.send("Bạn quyết định không nguyền!")
    elif ctx.author not in blackwolf:
        await ctx.send("Bạn không phải là sói nguyền!")
    await ctx.message.delete()


@client.command()
@commands.has_role("Werewolf player")
async def baove(ctx, num_player):
    num_player = int(num_player)
    global list_guarded, guarded, turn
    if guarded == False and dict_role_player[ctx.author] == "Bảo vệ" and num_player in dict_player:
        member = dict_player[num_player]
        if len(list_guarded) == 0:
            list_guarded.append(num_player)
            guarded = True
            await ctx.send(f"Bạn đã bảo vệ Player {member.display_name}")
        elif len(list_guarded) >= 1 and num_player == list_guarded[-1]:
            await ctx.send("Bạn đã bảo vệ một người vào đêm trước, không thể bảo vệ một người 2 đêm liên tục")
        elif len(list_guarded) >= 1 and num_player != list_guarded[-1]:
            list_guarded.append(num_player)
            guarded = True
            await ctx.send(f"Bạn đã bảo vệ Player {member.display_name}")
    elif guarded == True and dict_role_player[ctx.author] == "Bảo vệ":
        await ctx.send("Bạn đã bảo vệ một người vào đêm nay rồi!, Không thể bảo vệ người khác")
    elif dict_role_player[ctx.author] != "Bảo vệ":
        await ctx.send("Bạn không phải là bảo vệ!")
    elif guarded == False and num_player not in dict_player:
        await ctx.send("Player không hợp lệ, mời bạn chọn lại!")
    await ctx.message.delete()

@client.command()
@commands.has_role("Werewolf player")
async def tientri(ctx, num_player):
    global isseer
    num_player = int(num_player)
    if ctx.author in seer and isseer == False and num_player in dict_player:
        member = dict_player[num_player]
        if member in werewolfs:
            await ctx.send(f"{member.display_name} thuộc phe sói!")
        else:
            await ctx.send(f"{member.display_name} thuộc phe dân làng!")
    elif ctx.author in seer and isseer == True:
        await ctx.send("Bạn đã soi một người vào đêm nay rồi!")
    elif ctx.author in seer and isseer == False and num_player not in dict_player:
        await ctx.send("Player không hợp lệ")
    elif ctx.author not in seer:
        await ctx.send("Bạn không phải là tiên tri")
    await ctx.message.delete()


@client.command()
@commands.has_role("Werewolf player")
async def cuu(ctx):
    global player_death, witch_rescure, info_death
    if ctx.author in witch and witch_rescure > 0 and player_death != None:
        await ctx.send(f"Bạn đã cứu Player {dict_player[player_death].display_name}!")
        witch_rescure -= 1
        info_death.clear()
    elif ctx.author in witch and witch_rescure == 0 and player_death != None:
        await ctx.send(f"Bạn đã dùng hết bình cứu!")
    elif ctx.author not in witch:
        await ctx.send("Bạn không phải là phù thuỷ!")
    await ctx.message.delete()

        
@client.command()
@commands.has_role("Werewolf player")
async def khongcuu(ctx):
    global player_death, witch_rescure, info_death
    if ctx.author in witch and witch_rescure > 0 and player_death is not None:
        await ctx.send(f"Bạn đã không sử dụng bình cứu")
    elif ctx.author in witch and witch_rescure == 0:
        await ctx.send(f"Bạn đã dùng hết bình cứu!")
    elif ctx.author not in witch:
        await ctx.send("Bạn không phải là phù thuỷ!")
    await ctx.message.delete()


@client.command()
@commands.has_role("Werewolf player")
async def giet(ctx, num_player):
    num_player = int(num_player)
    global player_death, witch_kill, info_death
    if ctx.author in witch and witch_kill > 0 and num_player in dict_player:
        member = dict_player[num_player]
        await ctx.send(f"Bạn đã quăng bình giết {member.display_name}")
        witch_kill -= 1
        info_death.append(member)
    elif ctx.author in witch and witch_kill == 0 and num_player in dict_player:
        await ctx.send("Bạn đã dùng hết bình giết")
    elif ctx.author in witch and witch_kill > 0 and num_player not in dict_player:
        await ctx.send("Player không hợp lệ")
    elif ctx.author not in witch:
        await ctx.send("Bạn không phải là phù thuỷ!")
    await ctx.message.delete()


@client.command()
@commands.has_role("Werewolf player")
async def khonggiet(ctx):
    if ctx.author in witch and witch_kill > 0:
        await ctx.send("Bạn đã không sử dụng bình giết")
    elif ctx.author in witch and witch_kill == 0:
        await ctx.send("Bạn đã hết bình giết")
    elif ctx.author not in witch:
        await ctx.send("Bạn không phải là phù thuỷ!")
    await ctx.message.delete()


@client.command()
@commands.has_role("Werewolf player")
async def ghim(ctx, num_player):
    global hunter_list, fire
    num_player = int(num_player)
    if ctx.author in hunter and fire == False and num_player in dict_player:
        member = dict_player[num_player]
        await ctx.send(f"Bạn đã chọn {member.display_name} làm mục tiêu. Nếu bạn chết thì {member.display_name} sẽ chết cùng bạn")
        hunter_list.append(member)
        fire = True
    elif ctx.author in hunter and fire == True:
        await ctx.send("Bạn đã chọn mục tiêu vào đêm nay rồi!.")
    elif ctx.author in hunter and fire == False and num_player not in dict_player:
        await ctx.send("Player không hợp lệ")
    elif ctx.author not in hunter:
        await ctx.send("Bạn không phải là thợ săn")
    await ctx.message.delete()


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('Bạn không phải là quản trò hoặc bạn không tham gia vào game để dùng lệnh này!.')

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Các lệnh dành cho người chơi", colour=discord.Color.green())
    embed.add_field(name = "$play", value = "Lệnh này dùng để nhận role game và tham gia vào game!")
    embed.add_field(name = "$quit", value = "Ngược lại với lệnh play, hạn chế dùng lệnh này @@!")
    embed.add_field(name = "$getrole", value = "Lệnh này dùng để nhận chức năng trong game, sau khi quản trò bắt đầu game!")
    embed.add_field(name = "$skipvote", value= "Lệnh này dùng để skip vote nếu không biết vote ai cả")
    embed.add_field(name = "$vote", value = "Lệnh này dùng để biểu quyết 1 player nào đó, chỉ dùng được khi trong thời gian biểu quyết")
    embed.add_field(name = "$song", value = "Lệnh này dùng để vote sống cho một người bị lên dàn nếu có, nếu bản thân bị lên dàn thì không dùng được")
    embed.add_field(name = "$chet", value = "Ngược lại với vote sống")
    embed.add_field(name = "$can", value = "Lệnh này dành cho ma sói để chọn mục tiêu")
    embed.add_field(name = "$nguyen", value = "Lệnh này dành cho sói nguyền để nguyền mục tiêu")
    embed.add_field(name = "$khongnguyen", value = "Lệnh này dành cho ma sói để không nguyền mục tiêu")
    embed.add_field(name = "$baove", value = "Lệnh này dành cho bảo vệ để bảo vệ mục tiêu")
    embed.add_field(name = "$tientri", value = "Lệnh này dành cho tiên tri để soi mục tiêu")
    embed.add_field(name = "$ghim", value = "Lệnh này dành cho thợ săn để chọn mục tiêu")
    embed.add_field(name = "$cuu", value = "Lệnh này dành cho phù thuỷ để cứu người bị cắn")
    embed.add_field(name = "$khongcuu", value = "Lệnh này dành cho phù thuỷ để không cứu người bị cắn")
    embed.add_field(name = "$giet", value = "Lệnh này dành cho phù thuỷ để giết một người")
    embed.add_field(name = "$khonggiet", value = "Lệnh này dành cho phù thuỷ để không giết ai cả")
    embed.add_field(name = "$chucnang" , value = "Lệnh này dùng để check lại những chức năng nào có trong game!")
    embed.add_field(name = "$danhsach", value = "Lệnh này dùng kiểm tra danh sách player còn sống")
    embed.add_field(name = "$ghepdoi [player1] [player2]", value = "Nếu chức năng của bạn là CUPID thì bạn có thể dùng lệnh này để ghép đôi 2 người bất kỳ với nhau, Lưu ý: dùng lệnh này trong text channel của Cupid")
    await ctx.send(embed = embed)
    await ctx.message.delete()

    
@client.command()
@commands.has_role("Quản trò")
async def modhelp(ctx):
    embed = discord.Embed(title="Các lệnh dành cho quản trò", colour=discord.Color.green())
    embed.add_field(name = "$addrole [chức năng]", value = "Lệnh này dùng để setup chức năng cho game, Lưu ý: Quản trò phải ghi đúng tên chức năng: Sói thường, Sói nguyền, Bảo vệ, Tiên tri, Bán sói, Phù thuỷ, Dân làng, Cupid, Thợ săn. Ghi xong 1 chức năng thì phải dùng dấu , và dùng dấu cách 1 lần rồi ghi tiếp")
    embed.add_field(name = "$voting", value = "Lệnh này dùng để bắt đầu 1 cuộc biểu quyết!")
    embed.add_field(name = "$kiemtra", value = "Lệnh này dùng sau khi mọi người đã vote hoặc skipvote xong để đếm phiếu!")
    embed.add_field(name = "$ketqua", value = "Lệnh này dùng để đếm số phiếu chết và sống của tất cả mọi người, nếu chết nhiều hơn sống thì người chơi bị lên dàn tự động chết!")
    embed.add_field(name = "$thubai [Tag player name]", value = "Lệnh này dùng để thu bài 1 người chơi khi người chơi đó bị cắn chết, bị chết theo cặp đôi hoặc bị phù thuỷ quăng bình hoặc bị thợ săn ghim theo")
    embed.add_field(name = "$makeww [Tag player name]", value = "Lệnh này dùng để biến 1 người thành sói, trường hợp dùng khi bán sói bị cắn hoặc sói nguyền nguyền được người đó thành sói!")
    embed.add_field(name = "$mute", value= "Lệnh này dùng để chặn tất cả mọi người chơi chat vào text channel vào ban ngày, đến ban đêm thì $unmute")
    embed.add_field(name = "$unmute", value = "Lệnh này dùng để bỏ chặn cho phép mọi người nc vào ban đêm")
    embed.add_field(name = "$mod", value = "Lệnh này cho quản trò biết chức năng của tất cả mọi người")
    embed.add_field(name = "$reset", value = "Lệnh này dùng để reset sau khi xong 1 game!")
    await ctx.send(embed = embed)
    await ctx.message.delete()

   
@client.command()
@commands.has_role("Werewolf player")
async def chucnang(ctx):
    global num_players, roles_in_game
    embed = discord.Embed(title="Chức năng có trong game", colour=discord.Color.blue())
    embed.add_field(name = f"Có {num_players} chức năng trong game", value = " - ".join(role for role in roles_in_game))
    await ctx.send(embed = embed)
    await ctx.message.delete()


@client.command()
@commands.has_role("Quản trò")
async def mute(ctx):
    for member in werewolfs:
        channel = client.get_channel(channels['ma sói'])
        perms = channel.overwrites_for(member)
        perms.view_channel = False
        await channel.set_permissions(member, overwrite=perms)  
    for member in couples:
        channel = client.get_channel(channels['couple'])
        perms = channel.overwrites_for(member)
        perms.view_channel = False
        await channel.set_permissions(member, overwrite= perms)
    for member in blackwolf:
        channel = client.get_channel(channels['sói nguyền'])
        perms = channel.overwrites_for(member)
        perms.view_channel = False
        await channel.set_permissions(member, overwrite=perms)
    for member in curseguy:
        channel = client.get_channel(channels['bán sói'])
        perms = channel.overwrites_for(member)
        perms.view_channel = False
        await channel.set_permissions(member, overwrite=perms)
    for member in guard:
        channel = client.get_channel(channels['bảo vệ'])
        perms = channel.overwrites_for(member)
        perms.view_channel = False
        await channel.set_permissions(member, overwrite=perms)
    for member in witch:
        channel = client.get_channel(channels['phù thuỷ'])
        perms = channel.overwrites_for(member)
        perms.view_channel = False
        await channel.set_permissions(member, overwrite=perms)
    for member in seer:
        channel = client.get_channel(channels['tiên tri'])
        perms = channel.overwrites_for(member)
        perms.view_channel = False
        await channel.set_permissions(member, overwrite=perms)
    for member in hunter:
        channel = client.get_channel(channels['thợ săn'])
        perms = channel.overwrites_for(member)
        perms.view_channel = False
        await channel.set_permissions(member, overwrite=perms)
    for member in cupid:
        channel = client.get_channel(channels['cupid'])
        perms = channel.overwrites_for(member)
        perms.view_channel = False
        await channel.set_permissions(member, overwrite=perms)
    

@client.command()
@commands.has_role("Quản trò")
async def unmute(ctx):
    for member in werewolfs:
        channel = client.get_channel(channels['ma sói'])
        perms = channel.overwrites_for(member)
        perms.view_channel = True
        await channel.set_permissions(member, overwrite=perms)
    for member in couples:
        channel = client.get_channel(channels['couple'])
        perms = channel.overwrites_for(member)
        perms.view_channel = True
        await channel.set_permissions(member, overwrite= perms)
    for member in blackwolf:
        channel = client.get_channel(channels['sói nguyền'])
        perms = channel.overwrites_for(member)
        perms.view_channel = True
        await channel.set_permissions(member, overwrite=perms)
    for member in curseguy:
        channel = client.get_channel(channels['bán sói'])
        perms = channel.overwrites_for(member)
        perms.view_channel = True
        await channel.set_permissions(member, overwrite=perms)
    for member in guard:
        channel = client.get_channel(channels['bảo vệ'])
        perms = channel.overwrites_for(member)
        perms.view_channel = True
        await channel.set_permissions(member, overwrite=perms)
    for member in witch:
        channel = client.get_channel(channels['phù thuỷ'])
        perms = channel.overwrites_for(member)
        perms.view_channel = True
        await channel.set_permissions(member, overwrite=perms)
    for member in seer:
        channel = client.get_channel(channels['tiên tri'])
        perms = channel.overwrites_for(member)
        perms.view_channel = True
        await channel.set_permissions(member, overwrite=perms)
    for member in hunter:
        channel = client.get_channel(channels['thợ săn'])
        perms = channel.overwrites_for(member)
        perms.view_channel = True
        await channel.set_permissions(member, overwrite=perms)
    for member in cupid:
        channel = client.get_channel(channels['cupid'])
        perms = channel.overwrites_for(member)
        perms.view_channel = True
        await channel.set_permissions(member, overwrite=perms)

@client.command()
@commands.has_role("Quản trò")
async def mute_general(ctx):
    for member in dict_player.values():
        channel = client.get_channel(channels['thảo luận'])
        perms = channel.overwrites_for(member)
        perms.send_messages = False
        await channel.set_permissions(member, overwrite=perms)
    
@client.command()
@commands.has_role("Quản trò")
async def unmute_general(ctx):
    for member in dict_player.values():
        channel = client.get_channel(channels['thảo luận'])
        perms = channel.overwrites_for(member)
        perms.send_messages = True
        await channel.set_permissions(member, overwrite=perms)

@client.command()
@commands.has_role("Quản trò")
async def turnround(ctx, index):
    global player_death, witch_rescure, witch_kill, info_death, roles_in_game, werewolfs, list_vote_player
    werewolf_channel = client.get_channel(channels['ma sói'])
    blackwolf_channel = client.get_channel(channels['sói nguyền'])
    guard_channel = client.get_channel(channels['bảo vệ'])
    seer_channel = client.get_channel(channels['tiên tri'])
    hunter_channel = client.get_channel(channels['thợ săn'])
    cupid_channel = client.get_channel(channels['cupid'])
    couple_channel = client.get_channel(channels['couple'])
    witch_channel = client.get_channel(channels['phù thuỷ'])
    general = client.get_channel(channels['thảo luận'])
    role = get(ctx.guild.roles, name="Werewolf player")
    if index == 1:
        await mute_general(ctx)
        await mute(ctx)
        if "Bảo vệ" in roles_in_game:
            await unmute_guard(ctx)
            for member in guard:
                await guard_channel.send(member.mention)
                await guard_channel.send("Bạn có 30s để dùng lệnh ở trong này!\nLệnh của bảo vệ: $baove [Số của player muốn bảo vệ]")
                await danhsach(guard_channel)
            await asyncio.sleep(30)
            await mute_guard(ctx)
        if "Tiên tri" in roles_in_game:
            await unmute_seer(ctx)
            for member in seer:
                await seer_channel.send(member.mention)
                await seer_channel.send("Bạn có 30s để dùng lệnh ở trong này!\nLệnh của tiên tri: $tientri [Số của player muốn tiên tri]")
                await danhsach(seer_channel)
            await asyncio.sleep(30)
            await mute_seer(ctx)
        if "Sói thường" in roles_in_game or "Sói nguyền" in roles_in_game:
            await unmute_werewolf(ctx)
            for member in werewolfs:
                await werewolf_channel.send(member.mention)
                await werewolf_channel.send("Các bạn có 45s để dùng lệnh ở trong này!\nLệnh của đàn sói: $can [Số của player muốn cắn]")
                await danhsach(werewolf_channel)
            await asyncio.sleep(45)
            await mute_werewolf(ctx)
        if "Sói nguyền" in roles_in_game:
            await unmute_blackwolf(ctx)
            for member in blackwolf:
                await blackwolf_channel.send(member.mention)
                await blackwolf_channel.send("Bạn có 30s để dùng lệnh ở trong này!\nLệnh của sói nguyền: $nguyen hoặc $khongnguyen")
                await danhsach(blackwolf_channel)
            await asyncio.sleep(30)
            await mute_blackwolf(ctx)
        if "Phù thuỷ" in roles_in_game:
            await unmute_witch(ctx)
            for member in witch:
                await witch_channel.send(member.mention)
                await witch_channel.send("Bạn có 30s để dùng lệnh ở trong này!\nLệnh của phù thuỷ: $cuu hoặc $khongcuu, $giet [Số của player muốn giết] hoặc $khonggiet")
                await danhsach(witch_channel)
                if player_death == None:
                    await witch_channel.send(f"Đêm nay không ai chết. Bạn có muốn giết thêm ai không?. Số bình hiện tại của bạn là {witch_rescure} bình cứu, {witch_kill} bình giết!")
                else:
                    await witch_channel.send(f"Đêm nay {dict_player[player_death].name} bị giết. Bạn muốn cứu thì $cuu còn không thì $khongcuu Bạn có muốn giết thêm ai thì $giet còn không thì $khongcuu. Số bình hiện tại của bạn là {witch_rescure} bình cứu, {witch_kill} bình giết!")
            await asyncio.sleep(30)
            await mute_witch(ctx)
            if witch_rescure == 1 and player_death != None:
                info_death.append(dict_player[player_death])
        if "Thợ săn" in roles_in_game:
            await unmute_hunter(ctx)
            for member in hunter:
                await hunter_channel.send(member.mention)
                await hunter_channel.send("Bạn có 30s để dùng lệnh ở trong này!\nLệnh của thợ săn: $ghim [Số của player muốn ghim]")
                await danhsach(hunter_channel)
            await asyncio.sleep(30)
            await mute_hunter(ctx)
        if "Cupid" in roles_in_game:
            await unmute_couple(ctx)
            for member in couples:
                await couple_channel.send(member.mention)
                await couple_channel.send("Các bạn có 60s để thảo luận!")
                await danhsach(couple_channel)
            await asyncio.sleep(60)
            await mute_couple(ctx)
        await unmute_general(ctx)
        await general.send(role.mention)
        shuffle(info_death)
        if len(info_death) != 0:
            for member in info_death:
                await thubai(ctx, member)
        else:
            await general.send("Sáng nay không ai chết!")
        if endgame == False:
            await thaoluan(ctx)
            await general.send("Bạn có 180s để thảo luận và để chọn 1 người lên dàn bằng lệnh $vote hoặc $skipvote nếu muốn bỏ vote!")
            await danhsach(general)
            for i in range(180):
                await asyncio.sleep(1)
                if len(list_vote_player) == len(dict_player):
                    await general.send("Mọi người đã vote xong hết!")
                    await asyncio.sleep(5)
                    await kiemtra(ctx)
                    break
            await general.send("Hết thời gian vote!")
            await general.send(role.mention)
            await asyncio.sleep(5)
            await kiemtra(ctx)
            if isdone == True:
                await asyncio.sleep(5)
                await songhoacchet(ctx)
                await general.send("Các bạn có 1 phút để biểu quyết sống hoặc chết cho người bị lên dàn. $song để vote sống $chet để vote chết")
                for i in range(60):
                    await asyncio.sleep(1)
                    if len(live_death) == len(dict_player)-1:
                        await general.send("Mọi người đã vote xong hết!")
                        await asyncio.sleep(5)
                        await ketqua(ctx)
                        break
                await general.send("Hết thời gian biểu quyết sống hoặc chết")
                await general.send(role.mention)
                await asyncio.sleep(5)
                await ketqua(ctx)
            elif isdone == False:
                await ketqua(ctx)
    if index == 0:
        await mute_general(ctx)
        await mute(ctx)
        await unmute_cupid(ctx)
        for member in cupid:
            await cupid_channel.send(member.mention)
        await cupid_channel.send("Mời bạn chọn cặp đôi cho mình!\nLệnh của cupid: $ghepdoi [Số của player1] [Số của player2]")
        await danhsach(cupid_channel)
    if index == 2:
        await mute_cupid(ctx)
        await unmute_couple(ctx)
        await couple_channel.send("Các bạn có 30s để trao đổi về chức năng!")
        await asyncio.sleep(30)
        await mute_couple(ctx)
        if "Bảo vệ" in roles_in_game:
            await unmute_guard(ctx)
            for member in guard:
                await guard_channel.send(member.mention)
                await guard_channel.send("Bạn có 30s để dùng lệnh ở trong này!\nLệnh của bảo vệ: $baove [Số của player muốn bảo vệ]")
                await danhsach(guard_channel)
            await asyncio.sleep(30)
            await mute_guard(ctx)
        if "Tiên tri" in roles_in_game:
            await unmute_seer(ctx)
            for member in seer:
                await seer_channel.send(member.mention)
                await seer_channel.send("Bạn có 30s để dùng lệnh ở trong này!\nLệnh của tiên tri: $tientri [Số của player muốn tiên tri]")
                await danhsach(seer_channel)
            await asyncio.sleep(30)
            await mute_seer(ctx)
        if "Sói thường" in roles_in_game or "Sói nguyền" in roles_in_game:
            await unmute_werewolf(ctx)
            for member in werewolfs:
                await werewolf_channel.send(member.mention)
                await werewolf_channel.send("Các bạn có 45s để dùng lệnh ở trong này!\nLệnh của đàn sói: $can [Số của player muốn cắn]")
                await danhsach(werewolf_channel)
            await asyncio.sleep(45)
            await mute_werewolf(ctx)
        if "Sói nguyền" in roles_in_game:
            await unmute_blackwolf(ctx)
            for member in blackwolf:
                await blackwolf_channel.send(member.mention)
                await blackwolf_channel.send("Bạn có 30s để dùng lệnh ở trong này!\nLệnh của sói nguyền: $nguyen hoặc $khongnguyen")
                await danhsach(blackwolf_channel)
            await asyncio.sleep(30)
            await mute_blackwolf(ctx)
        if "Phù thuỷ" in roles_in_game:
            await unmute_witch(ctx)
            for member in witch:
                await witch_channel.send(member.mention)
                await witch_channel.send("Bạn có 30s để dùng lệnh ở trong này!\nLệnh của phù thuỷ: $cuu hoặc $khongcuu, $giet [Số của player muốn giết] hoặc $khonggiet")
                await danhsach(witch_channel)
                if player_death == None:
                    await witch_channel.send(f"Đêm nay không ai chết. Bạn có muốn giết thêm ai không?. Số bình hiện tại của bạn là {witch_rescure} bình cứu, {witch_kill} bình giết!")
                else:
                    await witch_channel.send(f"Đêm nay {dict_player[player_death].name} bị giết. Bạn muốn cứu thì $cuu còn không thì $khongcuu Bạn có muốn giết thêm ai thì $giet còn không thì $khongcuu. Số bình hiện tại của bạn là {witch_rescure} bình cứu, {witch_kill} bình giết!")
            await asyncio.sleep(30)
            await mute_witch(ctx)
            if witch_rescure == 1 and player_death != None:
                info_death.append(dict_player[player_death])
        if "Thợ săn" in roles_in_game:
            await unmute_hunter(ctx)
            for member in hunter:
                await hunter_channel.send(member.mention)
                await hunter_channel.send("Bạn có 30s để dùng lệnh ở trong này!\nLệnh của thợ săn: $ghim [Số của player muốn ghim]")
                await danhsach(hunter_channel)
            await asyncio.sleep(30)
            await mute_hunter(ctx)
        if "Cupid" in roles_in_game:
            await unmute_couple(ctx)
            for member in couples:
                await couple_channel.send(member.mention)
                await couple_channel.send("Các bạn có 60s để thảo luận!")
                await danhsach(couple_channel)
            await asyncio.sleep(60)
            await mute_couple(ctx)
        await unmute_general(ctx)
        await general.send(role.mention)
        shuffle(info_death)
        if len(info_death) != 0:
            for member in info_death:
                await thubai(ctx, member)
        else:
            await general.send("Sáng nay không ai chết!")
        if endgame == False:
            await thaoluan(ctx)
            await general.send("Bạn có 180s để thảo luận và để chọn 1 người lên dàn bằng lệnh $vote hoặc $skipvote nếu muốn bỏ vote!")
            await danhsach(general)
            for i in range(180):
                await asyncio.sleep(1)
                if len(list_vote_player) == len(dict_player):
                    await general.send("Mọi người đã vote xong hết!")
                    await asyncio.sleep(5)
                    await kiemtra(ctx)
                    break
            await general.send("Hết thời gian vote!")
            await general.send(role.mention)
            await asyncio.sleep(5)
            await kiemtra(ctx)
            if isdone == True:
                await asyncio.sleep(5)
                await songhoacchet(ctx)
                await general.send("Các bạn có 1 phút để biểu quyết sống hoặc chết cho người bị lên dàn. $song để vote sống $chet để vote chết")
                for i in range(60):
                    await asyncio.sleep(1)
                    if len(live_death) == len(dict_player)-1:
                        await general.send("Mọi người đã vote xong hết!")
                        await asyncio.sleep(5)
                        await ketqua(ctx)
                        break
                await general.send("Hết thời gian biểu quyết sống hoặc chết")
                await general.send(role.mention)
                await asyncio.sleep(5)
                await ketqua(ctx)
            elif isdone == False:
                await ketqua(ctx)


if __name__ == '__main__':
    keep_alive()
    client.run(TOKEN)
