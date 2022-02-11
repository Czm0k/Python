import create_1
import read_1
import update_1
import delete_1
import help_1
import const
import argparse

help_txt = "help.txt"
user_emails = []
users_storage = {}

parser = argparse.ArgumentParser(description='man')
parser.add_argument('--Help', action="store_true", help='description of program commands')
args = parser.parse_args()
if args.Help:
    help_1.act_help()

while not args.Help:
    action = input("Please enter create or read, or update, or delete actions: ")
    if action == "create":
        email = input(const.s_email)
        name = input(const.s_name)
        password = input(const.s_passwd)
        phone = input(const.s_phone)
        print(const.s_del + "\n"
              + create_1.create_user(email, name, password, phone, user_emails, users_storage)
              + "\n" + const.s_del)
    elif action == "read":
        email = input("Enter email of user or all to read info of all users: ")
        print(const.s_del + "\n"
              + read_1.read_info(email, user_emails, users_storage)
              + "\n" + const.s_del)
    elif action == "update":
        email = input("Enter user email: ")
        print(const.s_del + "\n"
              + update_1.update(email, user_emails, users_storage)
              + "\n" + const.s_del)
    elif action == "delete":
        email = input("Enter email of user whom you want to delete t or all to delete all users: ")
        print(const.s_del + "\n"
              + delete_1.delete(email, user_emails, users_storage)
              + "\n" + const.s_del)
    elif action == "exit":
        break
    else:
        print("Wrong action. Please enter create or read, or update, or delete actions: ")