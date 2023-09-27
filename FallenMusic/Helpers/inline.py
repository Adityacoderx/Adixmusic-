# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from FallenMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="✯ ᴄʟᴏsᴇ ✯", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▷", callback_data="resume_cb"),
            InlineKeyboardButton(text="II", callback_data="pause_cb"),
            InlineKeyboardButton(text="↻", callback_data="replay_cb"),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_cb"),
            InlineKeyboardButton(text="▢", callback_data="end_cb"),
        ],
        [
            InlineKeyboardButton(text="☆ 𝗥𝗘𝗦𝗨𝗠𝗘 🥀", callback_data="resume_cb"),
            InlineKeyboardButton(text="☆ 𝗣𝗔𝗨𝗦𝗘 🥀", callback_data="pause_cb"),
        ], 
        [
            InlineKeyboardButton(text="☆ 𝗦𝗞𝗜𝗣 🥀", callback_data="skip_cb"),
            InlineKeyboardButton(text="☆ 𝗘𝗔𝗗 🥀", callback_data="end_cb"), 
        ],  
        [    
            InlineKeyboardButton(text="☆ 𝗕𝗥𝗔𝗡𝗗𝗘𝗗 𝗞𝗜𝗡𝗚 🥀", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="☆ 𝗕𝗥𝗔𝗡𝗗𝗘𝗗 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 🥀", url=config.SUPPORT_CHAT),
        ], 
    ]   
)  


pm_buttons = [
    [
        InlineKeyboardButton(
            text="🌹 𝗔𝗗𝗗 𝗠𝗘 𝗜𝗡 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 🦋",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="🌹 𝗛𝗘𝗟𝗣 & 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 🦋", callback_data="fallen_help")],
    [
        InlineKeyboardButton(text="🌹 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 🦋", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text=" 🌹 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 🦋", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="🌹 𝗦𝗢𝗨𝗥𝗖𝗘 🦋", url="https://github.com/WCGKING/BRANDED-KING-MUSIC1"
        ),
        InlineKeyboardButton(text="🌹 𝗕𝗥𝗔𝗡𝗗𝗘𝗗 𝗞𝗜𝗡𝗚 🦋", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="🌹 𝗔𝗗𝗗 𝗠𝗘 𝗜𝗡 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 🦋",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="🌹 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 🦋", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="🌹 𝗕𝗥𝗔𝗡𝗗𝗘𝗗 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 🦋", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="🌹 𝗦𝗢𝗨𝗥𝗖𝗘  🦋 ", url="https://github.com/WCGKING/BRANDED-KING-MUSIC1"
        ),
        InlineKeyboardButton(text="🌹 𝗕𝗥𝗔𝗡𝗗𝗘𝗗 𝗞𝗜𝗡𝗚 🦋 ", user_id=config.OWNER_ID),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="ᴇᴠᴇʀʏᴏɴᴇ",
            callback_data="fallen_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="🌹 𝗦𝗨𝗗𝗢 🦋", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="🌹 𝗕𝗥𝗔𝗡𝗗𝗘𝗗 𝗞𝗜𝗡𝗚 🦋", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="🌹 𝗕𝗔𝗖𝗞 🦋", callback_data="fallen_home"),
        InlineKeyboardButton(text="🌹 𝗖𝗟𝗢𝗦𝗘 🦋", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="🌹 𝗕𝗥𝗔𝗡𝗗𝗘𝗗 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 🦋", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="🌹 𝗕𝗔𝗖𝗞 🦋", callback_data="fallen_help"),
        InlineKeyboardButton(text="🌹 𝗖𝗟𝗢𝗦𝗘 🦋", callback_data="close"),
    ],
]
