def check_if_in_list(item_to_check, list_to_check:list) -> bool:
    if not list_to_check:
        return False

    if list_to_check[0] == item_to_check:
        return True

    return check_if_in_list(item_to_check, list_to_check[1:])


if __name__ == "__main__":
    pass
