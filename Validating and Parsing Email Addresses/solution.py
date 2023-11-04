import email.utils
import re

n_cases = int(input())

for _ in range(n_cases):
    user_input_name_with_email_address = email.utils.parseaddr(input())
    user_name = user_input_name_with_email_address[0]
    user_email_address = user_input_name_with_email_address[1]
    match = re.search('(^[a-zA-Z]{1}[\w\-\.]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$)', user_email_address)
    if match:
        print(email.utils.formataddr((user_name, user_email_address)))