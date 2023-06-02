import re


def validate_email(email):
    password_pattern = r"^[\w.-]+[@][a-z0-9.-]+[.]\S{2,3}$"
    match = re.match(password_pattern, email)
    return bool(match)


def read_txt(name):
    with open(name, "r") as f:
        emails = f.readlines()
    return emails


def main(file_name):
    emails = read_txt(file_name)
    for email in emails:
        if validate_email(email):
            with open("list of valid email.txt", "a") as f:
                f.write(email)


if __name__ == '__main__':
    main("list of email.txt")
