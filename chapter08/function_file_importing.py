def user_info(first, last, **info_user):
    info_user['first_name'] = first.title()
    info_user['last_name'] = last.title()
    return info_user

