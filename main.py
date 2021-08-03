from random import shuffle
import discord
from discord.ext import commands
from discord.utils import get
from settings import *

client = commands.Bot(command_prefix='$', help_command=None)

channels = {
    'ma sói': 872024343029354526,
    'sói nguyền':872091054248177684,
    'couple': 872026916008374292,
    'bảo vệ':872091236054478889,
    'bán sói':872090616971018260,
    'tiên tri':872090741818667049,
    'phù thuỷ':872090939395571752,
    'thợ săn':872090783619108914,
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
async def resetwerewolf(ctx):
    global werewolfs, num_players, roles, list_id, players,dict_player, dict_num_role, isdone, kick, lives, deaths, max1, live_death, couples, iscupid, one, two, three, four, five, six, blackwolf, curseguy, guard,  witch, seer, hunter
    players.clear()
    roles.clear()
    list_id.clear()
    dict_player.clear()
    dict_num_role.clear()
    live_death.clear()
    kick = False
    isdone = False
    lives = 0
    deaths = 0
    max1 = 0
    for werewolf in werewolfs:
        channel = client.get_channel(channels['ma sói'])
        perms = channel.overwrites_for(werewolf)
        perms.view_channel = False
        await channel.set_permissions(werewolf, overwrite=perms)
    for coup in couples:
        channel = client.get_channel(channels['couple'])
        perms = channel.overwrites_for(coup)
        perms.view_channel = False
        await channel.set_permissions(coup, overwrite= perms)
    for i in blackwolf:
        channel = client.get_channel(channels['sói nguyền'])
        perms = channel.overwrites_for(i)
        perms.view_channel = False
        await channel.set_permissions(werewolf, overwrite=perms)
    for i in curseguy:
        channel = client.get_channel(channels['bán sói'])
        perms = channel.overwrites_for(werewolf)
        perms.view_channel = False
        await channel.set_permissions(werewolf, overwrite=perms)
    for i in guard:
        channel = client.get_channel(channels['bảo vệ'])
        perms = channel.overwrites_for(werewolf)
        perms.view_channel = False
        await channel.set_permissions(werewolf, overwrite=perms)
    for i in witch:
        channel = client.get_channel(channels['phù thuỷ'])
        perms = channel.overwrites_for(werewolf)
        perms.view_channel = False
        await channel.set_permissions(werewolf, overwrite=perms)
    for i in seer:
        channel = client.get_channel(channels['tiên tri'])
        perms = channel.overwrites_for(werewolf)
        perms.view_channel = False
        await channel.set_permissions(werewolf, overwrite=perms)
    for i in hunter: 
        channel = client.get_channel(channels['thợ săn'])
        perms = channel.overwrites_for(werewolf)
        perms.view_channel = False
        await channel.set_permissions(werewolf, overwrite=perms)

    werewolfs.clear()
    couples.clear()
    blackwolf.clear()
    curseguy.clear()
    seer.clear()
    guard.clear()
    witch.clear()
    hunter.clear()
    iscupid = False

    one, two, three, four, five, six = False, False, False, False, False, False
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
async def playwerewolf(ctx):
    global kick
    member = ctx.author
    role = get(ctx.guild.roles, name="Werewolf player")
    if member.id not in list_player_id and kick == False:
        list_player_id.append(member.id)
        await member.add_roles(role, atomic=False)
        await ctx.send(f"{member.name} đã tham gia vào game!")
    elif role in member.roles and member.id in list_player_id:
        await ctx.send("Bạn đã ở trong game rồi!")
    elif kick:
        await ctx.send("Game chưa kết thúc.")
    print(list_player_id)
    await ctx.message.delete()


@client.command()
async def quitwerewolf(ctx):
    member = ctx.author
    role = get(ctx.guild.roles, name="Werewolf player")
    if role in member.roles and member.id in list_player_id:
        list_player_id.remove(member.id)
        await member.remove_roles(role, atomic=False)
        await ctx.send(f"{member.name} đã thoát game.")
    elif role in member.roles and member.id not in list_player_id:
        await member.remove_roles(role, atomic=False)
        await ctx.send(f"{member.name} đã thoát game.")
    else:
        await ctx.send("Bạn chưa tham gia vào game.")
    print(list_player_id)
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

    global roles, players, dict_player, dict_num_role, dict_role_player, blackwolf, curseguy, guard,  witch, seer, hunter, werewolfs
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
                list_id.append(ctx.author)
                dict_player[player] = ctx.author
    
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

                perms4 = channel4.overwrites_for(ctx.author)
                perms4.view_channel = True
                await channel4.set_permissions(ctx.author, overwrite=perms4)

                await ctx.message.author.send("Chức năng của bạn là Bảo vệ")
                guard.append(ctx.author)
            elif role_player == "Cupid":
                dict_num_role[player] = role_player
                list_id.append(ctx.author.id)
                dict_player[player] = ctx.author
                dict_role_player[ctx.author] = role_player
                await ctx.message.author.send("Chức năng của bạn là Cupid")
            elif role_player == "Tiên tri":
                dict_num_role[player] = role_player
                dict_role_player[ctx.author] = role_player
                list_id.append(ctx.author.id)
                dict_player[player] = ctx.author

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
                await ctx.message.author.send("Chức năng của bạn là Dân làng")
            await ctx.send(f"{ctx.author.name} là Player số {player}")
        else:
            await ctx.send("Bạn đã nhận chức năng của mình rồi!")
    await ctx.message.delete()

@client.command()
@commands.has_role("Werewolf player")
async def vote(ctx, player):
    global num_players, list_vote_player, dict_player, votedone
    if num_players != 0:
        if int(player) in dict_player and ctx.author.id not in list_vote_player:
            num_vote_player.append(int(player))
            list_vote_player.append(ctx.author.id)
            await ctx.send(f"{ctx.author.name} đã chọn {dict_player[int(player)].name} là người lên dàn")
            print(num_vote_player)
        elif ctx.author.id in list_vote_player:
            await ctx.send("Bạn đã dùng lượt vote của mình!")
        elif int(player) not in dict_player:
            await ctx.send("Player không hợp lệ")
    elif num_players == 0:
        await ctx.send("Game chưa bắt đầu để vote!")
    votedone = False
    await ctx.message.delete()

@client.command()
@commands.has_role("Quản trò")
async def check(ctx): 
    global num_vote_player, isdone, dict1, max1, votedone
    if len(set(num_vote_player)) >= 2:
        dict1 = {index: num_vote_player.count(index) for index in num_vote_player}
        max1 = max(dict1, key = dict1.get)
        value1 = dict1[max1]
        del dict1[max1]
        max2 = max(dict1, key = dict1.get)
        value2 = dict1[max2]
        if value1 == value2:
            await ctx.send(f"Sáng hôm nay chúng ta không có ai bị lên dàn bởi có 2 người trở lên sỡ hữu cùng phiếu vote!")
            num_vote_player.clear()
            list_vote_player.clear()
            dict1.clear()
        else:
            await ctx.send(f"Sáng hôm nay chúng ta có một người bị lên dàn. Đó là {dict_player[max1].name} sở hữu {value1} phiếu vote")
            num_vote_player.clear()
            list_vote_player.clear()
            dict1.clear()
            isdone = True
    else:   
        dict1 = {index: num_vote_player.count(index) for index in num_vote_player}
        max1 = max(dict1, key = dict1.get)
        value1 = dict1[max1]
        await ctx.send(f"Sáng hôm nay chúng ta có một người bị lên dàn. Đó là {dict_player[max1].name} sở hữu {value1} phiếu vote")
        num_vote_player.clear()
        list_vote_player.clear()
        dict1.clear()
        isdone = True
    votedone = False
    await ctx.message.delete()

@client.command()
@commands.has_role("Werewolf player")
async def live(ctx):
    global lives, live_death, dict_player, votedone
    if isdone == True and dict_player[max1].name != ctx.author.name and ctx.author.id not in live_death:
        lives += 1
        live_death.append(ctx.author.id)
        await ctx.send(f"{ctx.author.name} đã vote Sống cho {dict_player[max1].name}")
    elif dict_player[max1].name == ctx.author.name:
        await ctx.send("Bạn không thể bầu sống hoặc chết cho bản thân mình")
    elif ctx.author.id in live_death:
        await ctx.send("Bạn đã biểu quyết rồi!")
    else:
        await ctx.send("Không có cuộc biểu quyết nào cả!")
    votedone = False
    await ctx.message.delete()

@client.command()
@commands.has_role("Werewolf player")
async def death(ctx):
    global deaths, live_death, dict_player,votedone
    if isdone == True and dict_player[max1].name != ctx.author.name and ctx.author.id not in live_death:
        deaths += 1
        live_death.append(ctx.author.id)
        await ctx.send(f"{ctx.author.name} đã vote Chết cho {dict_player[max1].name}")
    elif dict_player[max1].name == ctx.author.name:
        await ctx.send("Bạn không thể bầu sống hoặc chết cho bản thân mình")
    elif ctx.author.id in live_death:
        await ctx.send("Bạn đã biểu quyết rồi!")
    else:
        await ctx.send("Không có cuộc biểu quyết nào cả!")
    votedone = False
    await ctx.message.delete()

@client.command()
@commands.has_role("Quản trò")
async def result(ctx):
    global lives, deaths, max1, kick, dict_player,live_death, one, two, three, four, five, six, votedone, isguard
    member = dict_player[max1]
    role = get(ctx.guild.roles, name="Werewolf player")
    if lives >= deaths:
        await ctx.send(f"{dict_player[max1].name} sống với số biểu quyết {lives} Sống và {deaths} Chết")
    else:
        await ctx.send(f"{dict_player[max1].name} chết với số biểu quyết {lives} Sống và {deaths} Chết")
        await member.remove_roles(role, atomic=False)
        # list_player_id.remove(member.id)
        kick = True
        del member
    lives = 0
    deaths = 0
    max1 = 0
    live_death.clear()
    one, two, three, four, five, six = False, False, False, False, False, False
    votedone = True
    isguard = False
    await ctx.message.delete()
    
@client.command()
@commands.has_role("Werewolf player")
async def roleingame(ctx):
    global roles, num_players
    embed = discord.Embed(title="Roles", colour=discord.Color.blue())
    embed.add_field(name = f"Có {num_players} chức năng trong game", value = " - ".join(role for role in roles))
    await ctx.send(embed = embed)
    await ctx.message.delete()

@client.command()
async def couple(ctx, arg1, arg2):
    global couples, iscupid, one
    channel = client.get_channel(channels['couple'])
    if dict_role_player[ctx.author] == "Cupid" and iscupid == False:
        if int(arg1) > num_players or int(arg2) > num_players:
            await ctx.message.author.send("Số player không phù hợp mời bạn chọn lại")
        else:
            player1 = dict_player[int(arg1)]
            player2 = dict_player[int(arg2)]
            couples.append(player1)
            couples.append(player2)
            for i in couples:
                perms = channel.overwrites_for(i)
                perms.view_channel = True
                await channel.set_permissions(i, overwrite=perms)
            await ctx.message.author.send(f"Bạn đã ghép Player số {arg1} và Player số {2} thành một cặp")
            iscupid = True
            one = True
    elif dict_role_player[ctx.author] != "Cupid":
        await ctx.send("Bạn không phải là cupid để ghép đượp cặp đôi")
    elif iscupid:
        await ctx.send("Cupid đã ghép cặp đôi cho mình rồi!")


# @client.command()
# async def baove(ctx, arg):
#     global two, guard_list, guard_target, isguard, votedone
#     if one and votedone and dict_role_player[ctx.author] == "Bảo vệ":
#         if int(arg) not in dict_player:
#             await ctx.message.author.send("Player bạn bảo vệ không hợp lệ")
#         else:
#             if len(guard_list) == 0 and isguard == False:
#                 guard_target = int(arg)
#                 await ctx.message.author.send(f"Bạn đã bảo vệ Player số {arg}")
#                 guard_list.append(int(arg))
#                 isguard = True
#             elif len(guard_list) != 0 and int(arg) != guard_list[-1] and isguard == False:
#                 guard_target = int(arg)
#                 await ctx.message.author.send(f"Bạn đã bảo vệ Player số {arg}")
#                 guard_list.append(int(arg))
#                 isguard = True
#             elif len(guard_list) != 0 and int(arg) == guard_list[-1] and isguard == False:
#                 await ctx.message.author.send("Không thể bảo vệ một người 2 đêm liên tiếp")
#             elif isguard:
#                 await ctx.message.author.send("Bạn đã bảo vệ một người rồi, không thể bảo vệ tiếp!")
#     elif dict_role_player[ctx.author] != "Bảo vệ":
#         await ctx.message.author.send("Bạn không phải là bảo vệ")
#     elif votedone == False or one == False:
#         await ctx.message.author.send("Chưa đến lượt của bảo vệ")

# @client.command()
# @commands.has_role("Werewolf player")
# async def target(ctx, arg1):
#     global total_target, three, votedone
#     if votedone:
#         if one and ctx.author in werewolfs:
#             total_target.append(int(arg1))
#         elif one == False:
#             await ctx.send("Chưa tới turn của Ma sói")
#         elif ctx.author not in werewolfs:
#             await ctx.send("Bạn không phải là Ma sói")
#     else:
#         await ctx.send("Không thể cắn khi chưa đến turn")

# def return_target():
#     global three
#     if len(set(total_target)) >= 2:
#         dict_target1 = {index: total_target.count(index) for index in total_target}
#         max1 = max(dict_target1, key = dict_target1.get)
#         del dict1[max1]
#         max2 = max(dict1, key = dict1.get)
#         if max1 == max2:
#             three = True
#             player_target = 0
#             return player_target
#         else:
#             three = True
#             player_target = max1
#     else:
#         player_target = max(set(total_target), key = total_target.count)
#         three = True
#         return player_target

# def check_death():
#     player_target = return_target()
#     if guard_target == player_target:
#         death_target = 0
#         return death_target
#     elif dict_num_role[player_target] == "Bán sói":
#         death_target = 1
#         return death_target
#     else:
#         death_target = 2
    
# @client.command
# async def nguyen(ctx):
#     global death_target, danguyen
#     channel = client.get_channel(channels['ma sói'])
#     death_target = check_death()
#     if dict_role_player[ctx.author] == "Sói nguyền" and danguyen == False:
#         if death_target == 0:
#             await ctx.send.message.send("Bạn không thể nguyền mục tiêu này")
#         elif death_target == 1:

#         elif death_target == 2:
#             await ctx.send.message.send("Bạn đã nguyền người bị cắn thành sói")
#             danguyen = True
#             perms = channel.overwrites_for(dict_player[death_target])
#             perms.view_channel = True
#             await channel.set_permissions(dict_player[death_target], overwrite=perms)

#     else:
#         await ctx.message.author.send("Bạn không phải là sói nguyền")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')


            
        













































client.run(TOKEN)
