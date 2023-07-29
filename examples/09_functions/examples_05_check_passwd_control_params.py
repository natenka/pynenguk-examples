def password_check(
    username, password, min_len=8, check_user=True, min_spec_symbols=2
):
    spec_symbols = set("$#%@_=%")
    if len(password) < min_len:
        return False
    elif check_user and username.lower() in password.lower():
        return False
    elif len(set(password) & spec_symbols) < min_spec_symbols:
        return False
    else:
        return True


print(password_check("user1", "password", min_len=15))
print(password_check("user1", "passwo#rd+"))
print(password_check("user1", "passuse$r1w_ord"))
