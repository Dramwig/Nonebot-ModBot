from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.adapters import Bot, Event

from typing import Literal
from io import BytesIO
from pathlib import Path

from nonebot_plugin_imageutils import Text2Image

allowed_group_id = [543864096]

# 帮助
oc_help = on_command(
    "help", aliases={"帮助", "查口令", "口令", "命令"}, priority=10, block=True)

# 服务
oc_help_serve = on_command(
    "服务", aliases={"服务查询", "服务列表"}, priority=10, block=True)

# 游戏
oc_help_game = on_command(
    "game", aliases={"休闲", "娱乐", "游戏"}, priority=10, block=True)

# 指南
oc_help_guide = on_command(
    "指南", aliases={"攻略"}, priority=7, block=True)

# 数模导航
oc_mathnav = on_command(
    "数模导航", aliases={"数学建模导航", "数学建模指南", "数模指南", "数模学习资料", "数模资料库", "怎么学数学建模"}, priority=7, block=True)

# 数学建模介绍
oc_mathmodeling_introduction = on_command("数学建模介绍", aliases={"数学建模是什么", "数学建模是干什么", "数学建模要做什么"}, priority=5, block=True)

# 协会介绍
oc_association_introduction = on_command("协会介绍", aliases={"社团介绍", "社团是干什么的"}, priority=10, block=True)

# 部门介绍
oc_departmental_introduction = on_command("部门介绍", aliases={"有哪些部门", "有什么部门", "部门有哪些"}, priority=10, block=True)

# 快递位置
oc_serve1 = on_command("快递位置", priority=10, block=True)

# 往年试卷/学习资料
oc_serve2 = on_command("往年试卷", aliases={"学习资料"}, priority=10, block=True)

# 水卡充值
oc_serve3 = on_command("水卡充值", priority=10, block=True)

# 群聊导航
oc_serve4 = on_command("群聊导航", priority=10, block=True)

# 校车时间
oc_serve5 = on_command("校车时间", priority=10, block=True)

# 社团导航
oc_serve6 = on_command("社团导航", aliases={"学校社团"},priority=11, block=True)

# 新生入学指南
oc_guide1 = on_command("入学指南", aliases={"新生入学指南"}, priority=10, block=True)

# 转专业指南
oc_guide2 = on_command("转专业指南", aliases={"怎么转专业"},priority=10, block=True)

# 保研数据
oc_guide3 = on_command("保研数据", priority=10, block=True)

# 竞赛目录/A类学科竞赛目录
oc_guide4 = on_command("竞赛目录", aliases={"A类学科竞赛目录"}, priority=10, block=True)

@oc_help.handle()
async def handle_function():
    await oc_help.finish("help:\n├─ 数模导航/数模资料库\n├─ 数学建模/协会/介绍\n├─ 服务\n├─ 指南\n└─ game")

@oc_help_serve.handle()
async def handle_function():
    await oc_help.finish("服务:\n├─ 教务通知\n├─ 快递位置\n├─ 往年试卷/学习资料\n├─ 水卡充值\n├─ 群聊导航\n├─ 社团导航\n└─ 校车时间")

@oc_help_guide.handle()
async def handle_function():
    await oc_help.finish("指南:\n├─ 新生入学指南\n├─ 转专业指南\n├─ 保研数据\n└─ 竞赛目录/A类学科竞赛目录")

@oc_help_game.handle()
async def handle_function():
    await oc_help_game.finish('''game:
    开启游戏：装弹 [子弹数] [金额](默认200金币) [at](指定决斗对象，为空则所有群友都可接受决斗)
        示例：装弹 1 10
    接受对决：接受对决/拒绝决斗
    开始对决：开枪 [子弹数](默认1)（轮流开枪，根据子弹数量连开N枪械，30秒未开枪另一方可使用‘结算’命令结束对决并胜利）
    结算：结算（当某一方30秒未开枪，可使用该命令强行结束对决并胜利）
    我的战绩：我的战绩
    排行榜：金币排行/胜场排行/败场排行/欧洲人排行/慈善家排行
    商店：1抽照片
    给予：给予/赠送/送给 [at] [金额]
''')
    
@oc_mathnav.handle()
async def handle_function():
    await oc_help_game.finish("数模导航/资料库：\nhttps://mathnav.wangzixi.top")


@oc_association_introduction.handle()
async def handle_function(bot: Bot, event: Event):
    if event.message_type == "group":
        group_id = event.group_id
        # 在这里可以使用 group_id 进行后续的处理
        if group_id in allowed_group_id:
            await oc_departmental_introduction.send(f"调试1")
        elif group_id == 893487303:
            await oc_departmental_introduction.send("【数学建模协会】秋季招新！\n我们是一个致力于促进数学建模技能发展和分享的学生组织。在数学建模协会，你将有机会参与竞赛培训、体验欢脱的社团氛围、获得国赛获奖者的倾情指导，以及参与多样化的团建活动。\n\n近五年来，我们的学校在全国大学生数学建模竞赛中取得了显著成绩，共获得国家级奖项47项，省级奖项367项。其中，2021年，由协会成员组成的学生团队在本科组位列全国第一，夺得本科组唯一的最高奖项——高教社杯，刷新了学校获奖记录。此外，我们的学生在市调赛中也取得了优异成绩，获奖率逐年递增。\n\n如果你想度过一个充实而精彩的大学生活，结交志同道合的朋友，参加国家A类竞赛并为保研和综测加分积累经验，那么我们诚邀你加入数学建模协会！")
        elif group_id == 247685614:
            await oc_departmental_introduction.send("【ACM协会】\nACM协会成立于2006年，是在西南交通大学计算机与人工智能学院指导下，秉持自由、创新、勤奋和互助精神，致力于编程和算法技术分享与进步的学术科技类社团。 以赛促学，以赛促练，协会以朋辈分享会、名师讲坛、新秀杯赛事等活动为依托，注重传帮带，以阶梯式团队培养方式组建ACM校队，年均获得国家级奖项超20项。2021年以来共获国家级以上奖项60余次，获奖比例100%%，并在2021年国际大学生程序设计竞赛亚洲区赛中斩获金奖，刷新学校获奖记录。")
        else:
            # 在其他群组中提示无权限
            await oc_association_introduction.send("抱歉，本群未配置对应信息。")
    elif event.message_type == "private":
        # 处理私聊消息的代码
        await oc_association_introduction.send("仅支持群内消息。")

@oc_mathmodeling_introduction.handle()
async def handle_function():
    await oc_help.finish("数学建模是根据实际问题来建立数学模型，对数学模型进行求解，然后根据结果去解决实际问题的过程")

@oc_departmental_introduction.handle()
async def handle_function(bot: Bot, event: Event, args: Message = CommandArg(), ):
    if event.message_type == "group":
        group_id = event.group_id
        # 在这里可以使用 group_id 进行后续的处理
        if group_id in allowed_group_id:
            await oc_departmental_introduction.send(f"调试1")
        elif group_id == 893487303:
            department = args.extract_plain_text()
            if department == "活动部":
                await oc_departmental_introduction.send(f"{department}：负责组织集会、活动准备、奖状分发和物资领取等工作。该部门不仅能提高活动组织能力，还能结识优秀的人，是一个氛围很好的团队。")
            elif department == "新媒体" or department == "新媒体部":
                await oc_departmental_introduction.send(f"{department}：负责协会的宣传与设计工作，包括制作推送、海报、奖状等，并承担各类设计任务。加入新媒体部，将为你提供一个展示才华、与他人交流数学建模的平台。")
            elif department == "外联部" or department == "外联":
                await oc_departmental_introduction.send(f"{department}：负责讲座、聚会等活动的主持工作。不论你是活泼还是内向，都可以在这里找到展示自己的机会。同时，外联部的任务相对简单且集中，会给你很多空闲时间。部门还提供学习机会和丰富的团建活动。")
            elif department == "市调部" or department == "市调":
                await oc_departmental_introduction.send(f"{department}：市调部旨在培养优秀的建模手、写手和市场调查与分析的好手，提供同时参与两项A类竞赛的机会，并在前辈带领下提升成员的能力，延续交大数模和市调赛的辉煌。欢迎加入市调部！")
            elif department == "办公室":
                await oc_departmental_introduction.send(f"{department}：作为协会的重要部门，培养建模能力、综合素质和办公能力。在这里，你可以处理各种奖状，锻炼自身综合能力，快速入门数学建模。此外，办公室也提供丰富的娱乐活动，为你打造一个有趣的团队。")
            elif department == "学术部":
                await oc_departmental_introduction.send(f"{department}：作为协会的重要部门，学术部在寒假前后面向内外招新。该部门由国赛最高荣誉和一等奖获得者组成的部长团领导，部员的获奖率在国家级高达45.5%%，省级以上高达95.5%%。学术部提供朋辈导师制度、内部讲座、培训计划和参与赛题分析等机会，旨在帮助你感受数学建模的魅力，并助你在建模路上取得优异成绩，问鼎高教社杯。")
            elif department == "图片" or department == "三折页":
                pic_path = Path() / "data" / "三折页.png"
                await oc_departmental_introduction.send(MessageSegment.image(pic_path))
            elif department:
                pass
            else:
                await oc_departmental_introduction.send(f"数学建模协会是一个致力于促进数学建模技能发展和分享的学生组织。协会分为以下几个部门：\n1.新媒体:主要负责公众号【交大建模】的运营、各种宣传海报的制作（招新/竞赛/讲座），新秀杯和校赛奖状的设计.\n2.办公室:主要负责各种信息收集（竞赛报名/竞赛资格审核/获奖情况统计/讲座签到统计）、在竞赛群中发布通知.\n3.活动部:主要负责处理文件资料，线下活动前准备材料、布置场地，活动后打扫教室、实验室。\n4.外联部:主要负责安排活动流程，对外联络，发放奖状证书.\n5.学术部:每学年的第二学期，吸纳协会内外的、数学建模能力较强的同学进入学术部进行培养，提供细致的朋辈指导。\n6.市调部:主要负责“正大杯”市场调查与分析大赛的协办，包括组织选拔，协助答辩，发放奖状等。部门不进行招新，在换届时直接从办公室，新媒体，活动部三个部门选举负责人。\n【详细部门介绍见群文件】\nps：可以通过部门介绍+部门名/图片了解更多")
        elif group_id == 247685614:
            await oc_departmental_introduction.send("ACM协会主要分为五个部门，分别是：\n 办公室：负责协会日常工作安排、日常财务管理和比赛数据统计。\n 宣传部：负责推送、海报等宣传工作。\n 活动部：负责全员大会、校赛新秀杯等活动的流程策划与布置。\n 外联部：负责校内外各项赛事的组织报名工作，与友校交流活动和其他对外活动的联络与组织。\n 集训队：寒假前后面向全校选拔，代表学校参与ICPC系列赛事，负责校内赛事的出题工作与校内培训。")
        else:
            # 在其他群组中提示无权限
            await oc_departmental_introduction.send("抱歉，本群未配置对应信息。")
    elif event.message_type == "private":
        # 处理私聊消息的代码
        await oc_departmental_introduction.send("仅支持群内消息。")

@oc_serve1.handle()
async def handle_function():
    await oc_help_game.finish("快递位置信息：\nhttps://wiki.swjtu.top/pages/post/")

@oc_serve2.handle()
async def handle_function():
    await oc_help_game.finish("学习资料：\nhttps://swjtuhub.cn\nhttps://github.com/swjtuhub/SWJTU-Courses")

@oc_serve3.handle()
async def handle_function():
    await oc_help_game.finish('''水卡充值时间和地址：

======= 犀浦校区 =======

时间：每周一至周五9:00-12:00,15:30-18:30，每周六、周日14:00-18:00（节假日时间另行通知）
地点：犀浦2号教学楼1楼师生服务大厅购水购电处 
联系电话：66367967

======= 九里校区 =======

时间：每周一至周日：14:00-17:00 19:30-22:00（节假日时间另行通知）
地点：眷诚斋4号楼 
联系电话：87634197''')

@oc_serve4.handle()
async def handle_function():
    await oc_help_game.finish("群聊导航：\nhttps://wiki.swjtu.top/pages/groups/")

@oc_serve5.handle()
async def handle_function():
    await oc_help_game.finish("校车时刻表：\nhttps://wiki.swjtu.top/pages/schoolbus/")

@oc_serve6.handle()
async def handle_function():
    await oc_help_game.finish("所有社团导航：\nhttps://wiki.swjtu.top/pages/c198d6/#%%E7%%A4%%BE%%E5%%9B%%A2%%E7%%BB%%84%%E7%%BB%%87%%E6%%8E%%A8%%E5%%B9%%BF\nhttps://docs.qq.com/sheet/DQW5BSlR0TWpFRlVi?tab=BB08J2&u=c5f809aff56847269008edd6f1834452")

@oc_guide1.handle()
async def handle_function():
    await oc_help_game.finish("新生入学指南：\nhttps://wiki.swjtu.top/freshman/")

@oc_guide2.handle()
async def handle_function():
    await oc_help_game.finish("转专业指南：\nhttps://wiki.swjtu.top/change/")

@oc_guide3.handle()
async def handle_function():
    await oc_help_game.finish("保研数据：\nhttps://wiki.swjtu.top/free_major/")

@oc_guide4.handle()
async def handle_function():
    await oc_help_game.finish("A类学科竞赛目录：\nhttps://wiki.swjtu.top/free_contest/")