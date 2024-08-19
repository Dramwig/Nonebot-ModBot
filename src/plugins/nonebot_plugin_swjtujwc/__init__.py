from nonebot import require
require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler

from . import spider_jwc_swjtu as sp
from datetime import datetime

from nonebot import get_bot
from nonebot.adapters import Bot, MessageSegment
from nonebot.log import logger
from nonebot.plugin import on_command

import os

import asyncio
lock = asyncio.Lock()

async def jwc_swjtu_locked(arg1: int = 1, arg2: int = 2):
    """设置锁，防止多个定时任务同时执行
    """

    async with lock:
        file_address = "./data/swjtu_jwc/lasttime.txt"

        # 读取上一条通知的时间 
        try:
            with open(file_address, "r") as f:
                lasttime = f.read()
        except FileNotFoundError:
            # 保存最新通知的时间
            lasttime = '2021-01-01 00:00:00.000000'
            # 获取文件夹路径
            folder_path = os.path.dirname(file_address)  
            # 创建文件夹（如果不存在）
            os.makedirs(folder_path, exist_ok=True)
            # 创建文件并写入内容
            with open(file_address, "w") as f:
                f.write(lasttime)
            logger.info(f"文件{file_address}不存在，已创建。")

        # 解析字符串为datetime对象
        last_time_obj = datetime.strptime(lasttime, "%Y-%m-%d %H:%M:%S.%f")

        try:
            # 读取最新通知
            (title, time, link) = sp.SWJTU_scrape_notices()

            # 解析字符串为datetime对象
            new_time_obj = datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f") 

            logger.info(f"上一条通知时间：{last_time_obj}，最新通知时间：{new_time_obj}")

            # 如果有新通知且新通知与当前时间差不小于一小时
            if new_time_obj > last_time_obj:

                logger.info("教务网有新通知！")

                # 保存最新通知的时间
                with open(file_address, "w") as f:
                    f.write(time)

                # 发送通知
                bot = get_bot()
                await bot.send_group_msg(group_id=929601827, message=f"教务网新通知：{title}\n{link}")
                await bot.send_group_msg(group_id=893487303, message=f"教务网新通知：{title}\n{link}") 
                await bot.send_group_msg(group_id=1058118797, message=f"教务网新通知：{title}\n{link}")

        except:
            
            logger.info("教务网查询错误，可能是网络出现问题，请稍后再试。")


# 基于装饰器的方式的定时任务
@scheduler.scheduled_job("interval", seconds=300, id="job_0", kwargs={"arg2": 2})
async def scheduled_jwc_swjtu(arg1: int = 1, arg2: int = 2):
    """定时任务：教务网通知
    """
    await jwc_swjtu_locked(arg1, arg2)

# 读取最新通知
oc_new_notice = on_command(
    "教务通知", aliases={"最新通知", "最新教务通知"}, priority=5, block=True)

@oc_new_notice.handle()
async def handle_function():
    try:
        (title, time, link) = sp.SWJTU_scrape_notices()
        message = f"教务网最新通知：{title}\n{time}\n{link}"
        await oc_new_notice.send(message)
    except:
        await oc_new_notice.send("查询错误，可能是网络出现问题，请稍后再试。")