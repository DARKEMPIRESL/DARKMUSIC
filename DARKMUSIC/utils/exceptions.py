#
# Copyright (C) 2022 by DARKEMPIRESL@Github, < https://github.com/DARKEMPIRESL >.
#
# This file is part of < https://github.com/DARKEMPIRESL/DARKMUSIC > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DARKEMPIRESL/DARKMUSIC/blob/master/LICENSE >
#
# All rights reserved.


class AssistantErr(Exception):
    def __init__(self, errr: str):
        super().__init__(errr)
