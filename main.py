from random import shuffle
import discord
from discord.ext import commands
from discord.utils import get
from settings import *

client = commands.Bot(command_prefix='$', help_command=None)

channels = {
    'ma sói':872494848517763154,
    'sói nguyền':872494874413396018,
    'couple': 872494932336713828,
    'bảo vệ':872495019116879922, 
    'bán sói':872494986791387176,
    'tiên tri':872495086200565760,
    'phù thuỷ':872495057993859153,
    'thợ săn':872495103376240640,
    'cupid':872494905245708298,
}

channels1 = {
    'ma sói':872024343029354526,
    'sói nguyền':872091054248177684,
    'couple': 872026916008374292, 
    'bảo vệ':872091236054478889 ,
    'bán sói':872090616971018260, 
    'tiên tri':872090741818667049, 
    'phù thuỷ':872090939395571752,
    'thợ săn':872090783619108914, 
    'cupid':872350367936020481,
}


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.command()
async def ping(ctx):
    await ctx.send("pong")


@client.command()
@commands.has_role('Quản trò')
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_role('Quản trò')
async def reset(ctx): 
    global werewolfs, dict_num_player, dict_role_player, num_players, roles, list_id,players, dict_player, dict_num_role, isdone, kick, lives, deaths, max_value, live_death, couples, iscupid, blackwolf, curseguy, guard,  witch, seer, hunter, cupid
    
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
    kick = False
    isdone = False
    iscupid = False
    lives = 0
    deaths = 0
    max_value = 0
    num_players = 0

    await ctx.send("Reset game mới")
    await ctx.message.delete()

@client.command()
@commands.has_role('Quản trò')
async def addrole(ctx, *, role):
    global roles, num_players, players
    roles = role.split(', ')
    num_players = len(roles)
    players = list(range(1,num_players+1))
    embed = discord.Embed(title="Roles", colour=discord.Color.blue())
    embed.add_field(name = f"Có {num_players} chức năng trong game", value = " - ".join(role for role in roles))
    await ctx.send(embed = embed)
    await ctx.message.delete()

@client.command()
async def play(ctx):
    global kick
    member = ctx.author
    role = get(ctx.guild.roles, name="Werewolf player")
    if role not in member.roles and kick == False:
        await member.add_roles(role, atomic=False)
        await ctx.send(f"{member.mention} đã tham gia vào game!")
    elif role in member.roles:
        await ctx.send("Bạn đã ở trong game rồi!")
    elif kick:
        await ctx.send("Game chưa kết thúc.")
    await ctx.message.delete()


@client.command()
async def quit(ctx):
    member = ctx.author
    role = get(ctx.guild.roles, name="Werewolf player")
    if role in member.roles:
        await member.remove_roles(role, atomic=False)
        await ctx.send(f"{member.mention} đã thoát game.")
    else:
        await ctx.send("Bạn chưa tham gia vào game.")
    await ctx.message.delete()


@client.command()
@commands.has_role("Werewolf player")
async def getrole(ctx):
    channel1 = client.get_channel(channels['ma sói'])
    channel2 = client.get_channel(channels['sói nguyền'])
    channel3 = client.get_channel(channels['bán sói'])
    channel4 = client.get_channel(channels['bảo vệ'])
    channel5 = client.get_channel(channels['phù thuỷ'])
    channel6 = client.get_channel(channels['tiên tri'])
    channel7 = client.get_channel(channels['thợ săn'])
    channel8 = client.get_channel(channels['cupid'])

    global roles, players, dict_player, dict_num_player, dict_num_role, dict_role_player, blackwolf, curseguy, guard,  witch, seer, hunter, werewolfs, cupid, num_players

    shuffle(roles)
    shuffle(players)
    if len(roles) == 0:
        await ctx.send("Có thể game chưa bắt đầu hoặc đã đủ người chơi rồi")
    elif len(roles) != 0:
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

                perms1 = channel1.overwrites_for(ctx.author)
                perms1.view_channel = True
                await channel1.set_permissions(ctx.author, overwrite=perms1)

                await ctx.message.author.send("Chức năng của bạn là Sói thường")
            elif role_player == "Sói nguyền":
                dict_num_role[player] = role_player
                dict_role_player[ctx.author] = role_player
                werewolfs.append(ctx.author)
                list_id.append(ctx.author.id)
                dict_player[player] = ctx.author
                dict_num_player[ctx.author] = player

                perms1 = channel1.overwrites_for(ctx.author)
                perms1.view_channel = True
                await channel1.set_permissions(ctx.author, overwrite=perms1)

                perms2 = channel2.overwrites_for(ctx.author)
                perms2.view_channel = True
                await channel2.set_permissions(ctx.author, overwrite=perms2)

                blackwolf.append(ctx.author)

                await ctx.message.author.send("Chức năng của bạn là Sói nguyền")
            elif role_player == "Bán sói":
                dict_num_role[player] = role_player
                dict_role_player[ctx.author] = role_player
                list_id.append(ctx.author.id)
                dict_player[player] = ctx.author
                dict_num_player[ctx.author] = player

                perms3 = channel1.overwrites_for(ctx.author)
                perms3.view_channel = True
                await channel3.set_permissions(ctx.author, overwrite=perms3)

                await ctx.message.author.send("Chức năng của bạn là Bán sói")
                curseguy.append(ctx.author)
            elif role_player == "Bảo vệ":
                dict_num_role[player] = role_player
                dict_role_player[ctx.author] = role_player
                list_id.append(ctx.author.id)
                dict_player[player] = ctx.author
                dict_num_player[ctx.author] = player

                perms4 = channel4.overwrites_for(ctx.author)
                perms4.view_channel = True
                await channel4.set_permissions(ctx.author, overwrite=perms4)

                await ctx.message.author.send("Chức năng của bạn là Bảo vệ")
                guard.append(ctx.author)
            elif role_player == "Cupid":
                dict_num_role[player] = role_player
                dict_role_player[ctx.author] = role_player
                list_id.append(ctx.author.id)
                dict_player[player] = ctx.author
                dict_num_player[ctx.author] = player

                perms8 = channel8.overwrites_for(ctx.author)
                perms8.view_channel = True
                await channel8.set_permissions(ctx.author, overwrite=perms8)

                await ctx.message.author.send("Chức năng của bạn là Cupid")
                cupid.append(ctx.author)

            elif role_player == "Tiên tri":
                dict_num_role[player] = role_player
                dict_role_player[ctx.author] = role_player
                list_id.append(ctx.author.id)
                dict_player[player] = ctx.author
                dict_num_player[ctx.author] = player

                perms6 = channel6.overwrites_for(ctx.author)
                perms6.view_channel = True
                await channel6.set_permissions(ctx.author, overwrite=perms6)

                await ctx.message.author.send("Chức năng của bạn là Tiên tri")
                seer.append(ctx.author)
            elif role_player == "Phù thuỷ":
                dict_num_role[player] = role_player
                dict_role_player[ctx.author] = role_player
                list_id.append(ctx.author.id)
                dict_player[player] = ctx.author
                dict_num_player[ctx.author] = player

                perms5 = channel5.overwrites_for(ctx.author)
                perms5.view_channel = True
                await channel5.set_permissions(ctx.author, overwrite=perms5)

                await ctx.message.author.send("Chức năng của bạn là Phù thuỷ")
                witch.append(ctx.author)
            elif role_player == "Thợ săn":
                dict_num_role[player] = role_player
                dict_role_player[ctx.author] = role_player
                list_id.append(ctx.author.id)
                dict_player[player] = ctx.author
                dict_num_player[ctx.author] = player

                perms7 = channel7.overwrites_for(ctx.author)
                perms7.view_channel = True
                await channel7.set_permissions(ctx.author, overwrite=perms7)

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
    await ctx.message.delete()

@client.command()
@commands.has_role("Werewolf player")
async def skipvote(ctx):
    global list_vote_player, num_vote_player
    if voting_time:
        if ctx.author.id not in list_vote_player:
            list_vote_player.append(ctx.author.id)
            num_vote_player = num_vote_player
            await ctx.send(f"{ctx.author.display_name} đã skip vote!")
            await ctx.message.delete()
        else:
            await ctx.send(f"{ctx.author.display_name} đã vote hoặc skip vote rồi!")
    else:
        await ctx.send("Chưa đến thời gian để biểu quyết")
    await ctx.message.delete()

@client.command()
@commands.has_role("Werewolf player")
async def vote(ctx, player):
    global num_players, list_vote_player, dict_player
    if num_players != 0 and voting_time:
        if int(player) in dict_player and ctx.author.id not in list_vote_player:
            num_vote_player.append(int(player))
            list_vote_player.append(ctx.author.id)
            await ctx.send(f"{ctx.author.display_name} đã chọn {dict_player[int(player)].mention} là người lên dàn")
        elif ctx.author.id in list_vote_player:
            await ctx.send(f"{ctx.author.display_name} đã vote hoặc skip vote rồi!")
        elif int(player) not in dict_player:
            await ctx.send("Player không hợp lệ")
    elif num_players == 0:
        await ctx.send("Game chưa bắt đầu để vote!")
    elif voting_time == False:
        await ctx.send("Chưa đến thời gian để biểu quyết")
    await ctx.message.delete()

@client.command()
@commands.has_role("Quản trò")
async def kiemtra(ctx):
    global num_vote_player, isdone, dict_value, max_value
    if len(set(num_vote_player)) >= 2:
        dict_value = {index: num_vote_player.count(index) for index in num_vote_player}
        max_value = max(dict_value, key = dict_value.get)
        value1 = dict_value[max_value]
        del dict_value[max_value]
        max2 = max(dict_value, key = dict_value.get)
        value2 = dict_value[max2]
        if value1 == value2:
            await ctx.send(f"Sáng hôm nay chúng ta không có ai bị lên dàn bởi có 2 người trở lên sỡ hữu cùng phiếu vote!")
            num_vote_player.clear()
            list_vote_player.clear()
            dict_value.clear()
            isdone = False
        else:
            await ctx.send(f"Sáng hôm nay chúng ta có một người bị lên dàn. Đó là {dict_player[max_value].mention} sở hữu {value1} phiếu vote")
            num_vote_player.clear()
            list_vote_player.clear()
            dict_value.clear()
            isdone = True
    elif 1 <= len(set(num_vote_player)) < 2:
        dict_value = {index: num_vote_player.count(index) for index in num_vote_player}
        max_value = max(dict_value, key = dict_value.get)
        value1 = dict_value[max_value]
        await ctx.send(f"Sáng hôm nay chúng ta có một người bị lên dàn. Đó là {dict_player[max_value].mention} sở hữu {value1} phiếu vote")
        num_vote_player.clear()
        list_vote_player.clear()
        dict_value.clear()
        isdone = True
    elif len(num_vote_player) == 0:
        await ctx.send("Sáng hôm nay chúng ta không có ai bị lên dàn bởi mọi người đã skip vote!")
        num_vote_player.clear()
        list_vote_player.clear()
        dict_value.clear()
        isdone = False
    await ctx.message.delete()

@client.command()
@commands.has_role("Werewolf player")
async def song(ctx):
    global lives, live_death, dict_player
    if isdone and dict_player[max_value].name != ctx.author.name and ctx.author.id not in live_death:
        lives += 1
        live_death.append(ctx.author.id)
        await ctx.send(f"{ctx.author.display_name} đã vote Sống cho {dict_player[max_value].mention}")
    elif dict_player[max_value].name == ctx.author.name:
        await ctx.send("Bạn không thể bầu sống hoặc chết cho bản thân mình")
    elif ctx.author.id in live_death:
        await ctx.send("Bạn đã biểu quyết rồi!")
    elif isdone == False:
        await ctx.send("Không có cuộc biểu quyết sống/chết nào cả!")
    await ctx.message.delete()

@client.command()
@commands.has_role("Werewolf player")
async def chet(ctx):
    global deaths, live_death, dict_player
    if isdone and dict_player[max_value].name != ctx.author.name and ctx.author.id not in live_death:
        deaths += 1
        live_death.append(ctx.author.id)
        await ctx.send(f"{ctx.author.display_name} đã vote Chết cho {dict_player[max_value].mention}")
    elif dict_player[max_value].name == ctx.author.name:
        await ctx.send("Bạn không thể bầu sống hoặc chết cho bản thân mình")
    elif ctx.author.id in live_death:
        await ctx.send("Bạn đã biểu quyết rồi!")
    elif isdone == False:
        await ctx.send("Không có cuộc biểu quyết sống/chết nào cả!")
    await ctx.message.delete()

@client.command()
@commands.has_role("Quản trò")
async def ketqua(ctx):
    global lives, deaths, max_value, kick, dict_player,live_death, isdone, voting_time
    member = dict_player[max_value]
    role = get(ctx.guild.roles, name="Werewolf player")
    if lives >= deaths and isdone:
        await ctx.send(f"{dict_player[max_value].mention} sống với số biểu quyết {lives} Sống và {deaths} Chết")
    elif lives < deaths and isdone:
        await ctx.send(f"{dict_player[max_value].mention} chết với số biểu quyết {lives} Sống và {deaths} Chết")
        await member.remove_roles(role, atomic=False)
        dict_player.pop(max_value)
        kick = True
        if member in werewolfs and member not in blackwolf:
            channel = client.get_channel(channels['ma sói'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            werewolfs.remove(member)
        elif member in couples:
            channel = client.get_channel(channels['couple'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite= perms)
            couples.remove(member)
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
        elif member in guard and member not in guard:
            channel = client.get_channel(channels['bảo vệ'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            guard.remove(member)
        elif member in guard and member in werewolfs:
            channel = client.get_channel(channels['bảo vệ'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
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
        await ctx.send("Sáng nay không ai chết vì không có biểu quyết!")
        
    if len(werewolfs) == len(dict_player) - len(werewolfs):
            await ctx.send("Endgame, Sói thắng bởi vì số sói hiện tại bằng số dân!")
    if len(werewolfs) == 0:
            await ctx.send("Endgame, Dân thắng!")
    lives = 0
    deaths = 0
    max_value = 0
    live_death.clear()
    isdone = False
    voting_time = False
    await ctx.message.delete()

@client.command()
async def ghepdoi(ctx, arg1, arg2):
    global couples, iscupid
    channel = client.get_channel(channels['couple'])
    channel1 = client.get_channel(channels['cupid'])
    if dict_role_player[ctx.author] == "Cupid" and iscupid == False:
        if int(arg1) > num_players or int(arg2) > num_players:
            await channel1.send("Số player không phù hợp mời bạn chọn lại")
        else:
            player1 = dict_player[int(arg1)]
            player2 = dict_player[int(arg2)]
            couples.append(player1)
            couples.append(player2)
            for couple in couples:
                perms = channel.overwrites_for(couple)
                perms.view_channel = True
                await channel.set_permissions(couple, overwrite=perms)
            await channel1.send(f"Bạn đã ghép Player {dict_player[int(arg1)].display_name} và Player {dict_player[int(arg2)].display_name} thành một cặp")
            await channel.send(f"Cupid đã ghép Player {dict_player[int(arg1)].mention} và Player {dict_player[int(arg2)].mention} thành một cặp")
            iscupid = True
    elif dict_role_player[ctx.author] != "Cupid":
        await ctx.message.author.send("Bạn không phải là cupid để ghép đượp cặp đôi")
    elif iscupid:
        await ctx.message.author.send("Cupid đã ghép cặp đôi cho mình rồi!")

@client.command()
@commands.has_role("Quản trò")
async def thubai(ctx, member: discord.Member):
    global kick, dict_player, dict_num_player
    role = get(ctx.guild.roles, name="Werewolf player")
    if dict_num_player[member] in dict_player:
        dict_player.pop(dict_num_player[member])
        kick = True
        await member.remove_roles(role, atomic= False)
        await ctx.send(f"{member.mention} đã chết")
        if member in werewolfs and member not in blackwolf:
            channel = client.get_channel(channels['ma sói'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            werewolfs.remove(member)
        elif member in couples:
            channel = client.get_channel(channels['couple'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite= perms)
            couples.remove(member)
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
        elif member in guard and member not in guard:
            channel = client.get_channel(channels['bảo vệ'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
            guard.remove(member)
        elif member in guard and member in werewolfs:
            channel = client.get_channel(channels['bảo vệ'])
            perms = channel.overwrites_for(member)
            perms.view_channel = False
            await channel.set_permissions(member, overwrite=perms)
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
    else:
        await ctx.send("Player không hợp lệ")

    if len(werewolfs) == len(dict_player) - len(werewolfs):
            await ctx.send("Endgame, Sói thắng bởi vì số sói hiện tại bằng số dân!")
    if len(werewolfs) == 0:
            await ctx.send("Endgame, Dân thắng!")
    await ctx.message.delete()

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
    await ctx.message.delete()

@client.command()
@commands.has_role("Quản trò")
async def mod(ctx):
    global dict_role_player
    role_player = dict_role_player.keys()
    if len(role_player) != 0:
        embed = discord.Embed(title="Role player", colour=discord.Color.green())
        for i in role_player:
            embed.add_field(name = f"Player", value = f"Number: {dict_num_player[i]}   -   Name: {i.display_name}   -   Role: {dict_role_player[i]}", inline= False)
        await ctx.send(embed = embed)
    else:
        await ctx.send("Game chưa bắt đầu")
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
    await ctx.message.delete()

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
    await ctx.message.delete()

@client.command()
@commands.has_role("Quản trò")
async def voting(ctx):
    global voting_time
    voting_time = True
    await ctx.send("Thời gian vote bắt đầu!")
    await ctx.message.delete()

@client.command()
@commands.has_role("Quản trò")
async def makeww(ctx, member: discord.Member):
    global werewolfs
    werewolfs.append(member)
    channel = client.get_channel(channels['ma sói'])
    perms = channel.overwrites_for(member)
    perms.view_channel = True
    await channel.set_permissions(member, overwrite=perms)
    dm_channel = await member.create_dm()
    await dm_channel.send("Bạn đã hoá sói!")
    await ctx.message.author.send(f"{member.display_name} đã hoá sói!")
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
    embed.add_field(name = "$vote [number player]", value = "Lệnh này dùng để biểu quyết 1 player nào đó, chỉ dùng được khi trong thời gian biểu quyết")
    embed.add_field(name = "$song", value = "Lệnh này dùng để vote sống cho một người bị lên dàn nếu có, nếu bản thân bị lên dàn thì không dùng được")
    embed.add_field(name = "$chet", value = "Ngược lại với vote sống")
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
    global roles, num_players
    embed = discord.Embed(title="Chức năng có trong game", colour=discord.Color.blue())
    embed.add_field(name = f"Có {num_players} chức năng trong game", value = " - ".join(role for role in roles))
    await ctx.send(embed = embed)
    await ctx.message.delete()
 
client.run(TOKEN)
