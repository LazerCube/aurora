def is_owner(request, account):
    if request.user:
        return account == request.user
    return False
