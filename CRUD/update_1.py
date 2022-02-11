import read_1
import const



def update_email(email, user_emails, user_storage):
    new_email = input("Enter new email: ")
    if const.unique_check(new_email, user_emails):
        for i in range(len(user_emails)):
            if user_emails[i] == email:
                user_emails[i] = new_email
                break
        user_storage[new_email] = user_storage.pop(email)
        return read_1.msg_user_form(new_email, user_storage)
    else:
        return const.s_exist


def update_name(email, user_storage):
    new_name = input("Enter new name: ")
    user_storage[email]["name"] = new_name
    return read_1.msg_user_form(email, user_storage)


def update_password(email, user_storage):
    new_passwd = input("Enter new password: ")
    user_storage[email]["password"] = new_passwd
    return read_1.msg_user_form(email, user_storage)


def update_phone(email, user_storage):
    new_phone = input("Enter new phone: ")
    user_storage[email]["phone"] = new_phone
    return read_1.msg_user_form(email, user_storage)


def update(email, user_emails, user_storage):
    message = ""
    if email in user_emails:
        param = input("Input parameter to change: ")
        if param == "email":
            message = update_email(email, user_emails, user_storage)
        elif param == "name":
            message = update_name(email, user_storage)
        elif param == "password":
            message = update_password(email, user_storage)
        elif param == "phone":
            message = update_phone(email, user_storage)
        else:
            message = "Incorrect parametr!"
    else:
        message = "No user with email: " + email
    return message