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
    cre_a, na_a = sql_.select_user_credit(u_id)

    if cre_a != -1:
        await session.send('您已经参加打卡了哦~~~，希望你这个小马猴可以坚持下去呀')
    else:
        sql_.add_uesr(u_id, u_name, u_sex, u_age)
        await session.send('成功参加打卡，希望马猴可以按时打卡哟~')
        await session.send('打卡的规则：一天仅能打两次卡，高数一次，英语一次。')
        await session.send('若要打卡，请艾特我发送需要打卡的科目')
        await session.send('格式：英语打卡、英语、高数打卡、高数')


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
    flag = sql_.add_record(u_id, c_type, c_credit, today)
    cre_a, na_a = sql_.select_user_credit(u_id)
    if flag == -1:
        await session.send(na_a + "，今日已打过英语，不能重复打卡")
    else:

        await session.send(na_a + '打卡成功')
        await session.send('英语积分+1')
        await session.send('当前总积分为' + str(cre_a))


@on_command('高数打卡', aliases=['高数', '数学'], permission=perm.GROUP_MEMBER)
async def _(session: CommandSession):
    msg = session.ctx
    pprint(msg)
    today = datetime.date.today()
    u_id = msg['user_id']
    c_type = 'Math'
    c_credit = 1
    flag = sql_.add_record(u_id, c_type, c_credit, today)
    cre_a, na_a = sql_.select_user_credit(u_id)
    if flag == -1:
        await session.send(na_a + "，今日已打过高数，不能重复打卡")
    else:

        await session.send(na_a + '打卡成功')
        await session.send('高数积分+1')
        await session.send('当前总积分为' + str(cre_a))


@on_command('积分', aliases=['查询积分', '查询'], permission=perm.GROUP_MEMBER)
async def _(session: CommandSession):
    msg = session.ctx
    pprint(msg)
    u_id = msg['user_id']
    cre_a, na_a = sql_.select_user_credit(u_id)
    if cre_a != -1:
        await session.send('当前总积分为' + str(cre_a))
    else:
        await session.send('暂时没有您的数据呢')
