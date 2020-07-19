from nonebot import on_command, CommandSession  # 命令的对话
from nonebot import permission as perm
from .. import sql_tables as sql_

# def 前要加async
# send 前加await
# （二者搭配使用）试图处理多个消息（来自不同人消息）
# 用于python引进异步IO的两个关键字


@on_command('喵一个', aliases=['miao', '喵喵喵'])
async def _(session: CommandSession):  # 为了补全session的方法
    await session.send('喵~')


@on_command('get_menber_count', aliases=['总人数'], permission=perm.GROUP_MEMBER)
async def _(session: CommandSession):
    group_id = session.ctx['group_id']
    member_list = await session.bot.get_group_member_list(
        group_id=group_id
    )
    await session.send(f'群里一共有{len(member_list)}个人')


@on_command('daka', aliases=['我要参加打卡'], permission=perm.GROUP_MEMBER)
async def _(session: CommandSession):
    msg: str = await session.bot.get_
    u_id = await session.ctx['user_id']
    u_name = await session.ctx['sender']['nickname']
    u_sex = await session.ctx['sender']['sex']
    u_age = await session.ctx['sender']['age']
    sql_.add_uesr(u_id, u_name, u_sex, u_age)
    group_id = session.ctx['group_id']
    await session.send('成功参加打卡')

    # await session.send(f'群里一共有{len(member_list)}个人')
