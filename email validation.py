def check_email(email):
    email = email.strip()

    if "@" not in email:
        return "Invalid email: missing @."

    if not email.endswith(".com"):
        return "Invalid email: email must end with .com."

    if email.startswith(".com"):
        return "Invalid email."

    if email.startswith("@"):
        return "Invalid email: missing username."

    if email.endswith("@"):
        return "Invalid email: missing domain."

    if email.count("@") != 1:
        return "Invalid email: email must contain only one @."

    username, domain = email.split("@")

    if username == "":
        return "Invalid email: missing username."

    if domain == ".com":
        return "Invalid email: missing domain name."

    return "Valid email."


email = input("Enter your email: ")

result = check_email(email)
print(result)