import asyncio
import logging
import os
import random
from collections import deque

import toml
from vk import VK
from vk import types
from vk.bot_framework import Dispatcher, get_group_id
from vk.exceptions import APIException
from vk.keyboards import ButtonColor
from vk.keyboards import Keyboard
from vk.types import message
from vk.utils import TaskManager


with open("config.toml", "r", encoding="utf-8") as f:
    if "message_text" in os.environ and "token" in os.environ:
        config = dict(os.environ)
        for key, value in toml.load(f).items():
            if key not in config:
                config[key] = value
    else:
        config = toml.load(f)

logging.basicConfig(level=config["logging_level"])

vk = VK(config["token"])
task_manager = TaskManager(vk.loop)
api = vk.get_api()

dp = Dispatcher(vk)


def adjust_message_text():
    message_text = config["message_text"].encode()
    if len(message_text) < 4096:
        message_text = message_text * int(4096 / len(message_text))
        config["message_text"] = message_text.decode()


async def apply_required_settings(group_id: int):
    await vk.api_request(
        "groups.setSettings",
        {
            "group_id": group_id,
            "messages": 1,
            "bots_capabilities": 1,
            "bots_add_to_chat": 1,
        },
    )
    await vk.api_request(
        "groups.setLongPollSettings",
        {"group_id": group_id, "enabled": 1, "api_version": "5.103", "message_new": 1},
    )


@dp.message_handler(chat_action=message.Action.chat_invite_user)
async def chat_invite_user(msg: types.Message, _):
    logging.info(f"Started raiding {msg.peer_id}.")
    sent_message_count = 0
    while True:
        try:
            keyboard = Keyboard(one_time=False)
            for row in range(0, 10):
                button_colors = deque(
                    [
                        ButtonColor.POSITIVE,
                        ButtonColor.NEGATIVE,
                        ButtonColor.SECONDARY,
                        ButtonColor.PRIMARY,
                    ]
                )
                button_colors.rotate(sent_message_count % len(button_colors))
                for button in range(0, 4):
                    keyboard.add_text_button(
                        config["buttons_text"], color=button_colors[button]
                    )
                if row != 9:
                    keyboard.add_row()
            await api.messages.send(
                random_id=random.getrandbits(31) * random.choice([-1, 1]),
                peer_id=msg.peer_id,
                message=config["message_text"],
                keyboard=keyboard.get_keyboard(),
            )
            sent_message_count += 1
            await asyncio.sleep(config["delay"])
        except APIException as e:
            logging.info(f"Stopped raiding {msg.peer_id}. Reason: {e}")
            break


async def run():
    group_id = await get_group_id(vk)
    await apply_required_settings(group_id)
    adjust_message_text()
    dp.run_polling(group_id)


if __name__ == "__main__":
    task_manager.add_task(run)
    task_manager.run(auto_reload=False)
