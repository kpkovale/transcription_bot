def get_message_link(chat_id: int, message_id: int):
    link = "[аудио ](https://t.me/c/{}/{})"
    if str(chat_id)[0:4] == '-100':
        chat_id = int(str(chat_id).replace("-100", ""))
    elif str(chat_id)[0:4] == "-400":
        return None

    return link.format(abs(chat_id), message_id)
