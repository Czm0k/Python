import const
import read_1



def create_user(email, name, password, phone, user_emails, user_storage):
    if const.unique_check(email, user_emails):
        user_emails.append(email)
        user_storage[email] = {"name": name, "password": password, "phone": phone}
        return read_1.msg_user_form(email, user_storage)
    else:
        return const.s_exist