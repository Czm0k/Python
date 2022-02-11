s_email = "User_email: "
s_name = "User_name: "
s_passwd = "User_password: "
s_phone = "User_phone: "
s_exist = "User with entered email already exists or email forbidden! Data not changed!"
s_del = "___________________========================____________________"


def unique_check(email, user_emails):
    if (email in user_emails) or email == "all":
        return False
    else:
        return True