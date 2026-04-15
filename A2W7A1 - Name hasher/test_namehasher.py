from namehasher import set_dict_key, encode_string, decode_string, encode_list, decode_list, validate_values


def get_fresh_state():
    return {"key": {}, "encoded": [], "decoded": []}


def test_encode_string():
    state = get_fresh_state()
    set_dict_key("A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@")

    assert "**9 (?##*(;* :0;=?!5;" == encode_string("EEN CORRECTE UITKOMST")
    assert "*en (orrecte :itkomst" == encode_string("Een Correcte Uitkomst")


def test_decode_string():
    state = get_fresh_state()
    set_dict_key("A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@")

    assert "ANDERSOM WERKT OOK" == decode_string("%9)*#5?! ]*#=; ??=")
    assert "Ook Met Kleine Letters" == decode_string("?ok !et =leine 1etters")


def test_encode_list():
    state = get_fresh_state()
    set_dict_key("A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@")

    assert [">0*;*#", ">%9"] == encode_list(["PIETER", "PAN"])


def test_decode_list():
    state = get_fresh_state()
    set_dict_key("A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@")

    assert ["PIETER", "PAN"] == decode_list([">0*;*#", ">%9"])


def test_validate_values():
    state = get_fresh_state()
    set_dict_key("A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@")

    assert True == validate_values(">0*;*#", "PIETER")
    assert False == validate_values(">0*;*#", "Pieter")