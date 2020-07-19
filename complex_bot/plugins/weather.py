from nonebot import on_command, CommandSession  # 命令的对话


# def 前要加async
# send 前加await
# （二者搭配使用）试图处理多个消息（来自不同人消息）
# 用于python引进异步IO的两个关键字


@on_command('天气', aliases=['查天气', 'chatianqi'])
async def weather(session: CommandSession):  # 为了补全session的方法
    city = session.get('city', prompt='你想查哪个城市呢？')
    date = session.get('date', prompt='你想查哪一天呢？')
    await session.send('你查询的城市是' + city)
    await session.send('你查询的日期是' + date)


@weather.args_parser
async def _(session: CommandSession):
    if session.is_first_run:
        return
    session.args[session.current_key] = session.current_arg_text

