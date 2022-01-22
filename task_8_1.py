
import re


def email_parse(email_address):
    key_ = ["username", "domain"]
    re_address = re.findall(r"([A-z0-9_+.-]+)@([A-z0-9_+.-]+\.[a-z]+)$", email_address)
    if not re_address:
        raise ValueError(f"wrong email: {email_address}")
    return dict(zip(key_ , re_address[0]))

print(email_parse('someone@geekbrains.ru'))
