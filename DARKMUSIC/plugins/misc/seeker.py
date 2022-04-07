#
# Copyright (C) 2022 by DARKEMPIRESL@Github, < https://github.com/DARKEMPIRESL >.
#
# This file is part of < https://github.com/DARKEMPIRESL/DARKMUSIC > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DARKEMPIRESL/DARKMUSIC/blob/master/LICENSE >
#
# All rights reserved.

import asyncio

from DARKMUSIC.misc import db
from DARKMUSIC.utils.database import (get_active_chats,
                                       is_music_playing)


async def timer():
    while not await asyncio.sleep(1):
        active_chats = await get_active_chats()
        for chat_id in active_chats:
            if not await is_music_playing(chat_id):
                continue
            playing = db.get(chat_id)
            if not playing:
                continue
            file_path = playing[0]["file"]
            if "index_" in file_path or "live_" in file_path:
                continue
            duration = int(playing[0]["seconds"])
            if duration == 0:
                continue
            db[chat_id][0]["played"] += 1


asyncio.create_task(timer())
