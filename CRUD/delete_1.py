import read_1



def delete_user(email, user_emails, user_storage):
    user_storage.pop(email)
    user_emails.remove(email)
    return read_1.all_user_info(user_storage)


def delete(email, user_emails, user_storage):
    if email == "all":
        user_emails.clear()
        user_storage.clear()
        message = "All users was deleted"
    else:
        if email in user_emails:
            message = delete_user(email, user_emails, user_storage)
        else:
            message = "No user with email: " + email
    return message