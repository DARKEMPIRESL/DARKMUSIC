#
# Copyright (C) 2022 by DARKEMPIRESL@Github, < https://github.com/DARKEMPIRESL >.
#
# This file is part of < https://github.com/DARKEMPIRESL/DARKMUSIC > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DARKEMPIRESL/DARKMUSIC/blob/master/LICENSE >
#
# All rights reserved.

from DARKMUSIC.core.bot import YukkiBot
from DARKMUSIC.core.dir import dirr
from DARKMUSIC.core.git import git
from DARKMUSIC.core.userbot import Userbot
from DARKMUSIC.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = YukkiBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
