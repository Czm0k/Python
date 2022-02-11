import const


def msg_user_form(email, user_storage):
    message = const.s_email + email + '\n'\
              + const.s_name + user_storage[email]["name"] + '\n'\
              + const.s_passwd + user_storage[email]["password"] + '\n'\
              + const.s_phone + user_storage[email]["phone"]
    return message


def read_info(email, user_emails, user_storage):
    if email in user_emails:
        return msg_user_form(email, user_storage)
    elif email == "all":
        message = all_user_info(user_storage)
    else:
        message = "No user with email: " + email
    return message


def all_user_info(user_storage):
    message = ""
    for k, v in user_storage.items():
        message = message + const.s_email + k + ", " \
        + const.s_name + v["name"] + ", " \
        + const.s_passwd + v["password"] + ", "\
        +const.s_phone + v["phone"] + '\n'
    return message.rstrip()