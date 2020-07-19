import nonebot, os

from complex_bot import config

# 在用load_plugins（）时，注意俩个参数的名称

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_builtin_plugins()
    nonebot.load_plugins(
        os.path.join(os.path.dirname(__file__), 'plugins'),
        'complex_bot.plugins')
    nonebot.run()
