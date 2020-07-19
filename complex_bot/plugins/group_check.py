import datetime
from pprint import pprint

from nonebot import on_command, CommandSession  # 命令的对话
from nonebot import permission as perm
from .. import sql_tables as sql_


# def 前要加async
# send 前加await
# （二者搭配使用）试图处理多个消息（来自不同人消息）
# 用于python引进异步IO的两个关键字


@on_command('get_menber_count', aliases=['总人数'], permission=perm.GROUP_MEMBER)
async def _(session: CommandSession):
    group_id = session.ctx['group_id']
    member_list = await session.bot.get_group_member_list(
        group_id=group_id
    )
    await session.send(f'群里一共有{len(member_list)}个人')


@on_command('我要打卡', aliases=['我要参加打卡'], permission=perm.GROUP_MEMBER)
async def _(session: CommandSession):
    msg = session.ctx
    pprint(msg)

    u_id = msg['user_id']
    u_name = msg['sender']['nickname']
    u_sex = msg['sender']['sex']
    u_age = msg['sender']['age']
    print(u_id, u_name, u_sex, u_age)
    sql_.add_uesr(u_id, u_name, u_sex, u_age)
    # group_id = msg['group_id']
    await session.send('成功参加打卡')


# @on_command('打卡', aliases=['今日打卡'], permission=perm.GROUP_MEMBER)
# async def _(session: CommandSession):
#     msg = session.ctx
#     pprint(msg)
#
#     u_id = msg['user_id']
#     u_name = msg['sender']['nickname']
#     u_sex = msg['sender']['sex']
#     u_age = msg['sender']['age']
#     print(u_id, u_name, u_sex, u_age)
#     sql_.add_uesr(u_id, u_name, u_sex, u_age)
#     # group_id = msg['group_id']
#     await session.send('成功参加打卡')

@on_command('英语打卡', aliases=['英语'], permission=perm.GROUP_MEMBER)
async def _(session: CommandSession):
    msg = session.ctx
    pprint(msg)
    today = datetime.date.today()
    u_id = msg['user_id']
    c_type = 'English'
    c_credit = 1
    sql_.add_record(u_id, c_type, c_credit, today)
    sql_.up_user(u_id, today)

    await session.send('打卡成功')
