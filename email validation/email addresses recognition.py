import re


def validate_email(email):
    password_pattern = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@[a-z0-9.-]+[.]\S{2,3}$"
    match = re.match(password_pattern, email)
    return bool(match)


def read_txt(name):
    with open(name, "r") as f:
        emails = f.readlines()
    return emails


def write_txt(filename, info):
    with open(filename, "a") as f:
        f.write(info)


def main(input_file, output_file):
    emails = read_txt(input_file)
    for email in emails:
        if validate_email(email):
            write_txt(output_file, email)


if __name__ == '__main__':
    main("list of email.txt", "list of valid email.txt")
