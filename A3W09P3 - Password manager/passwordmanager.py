class PasswordManager:
    def __init__(self, initial_password: str = ""):
        if initial_password:
            self.old_passwords = [initial_password]
        else:
            self.old_passwords = []

    def get_password(self):
        if self.old_passwords:
            return self.old_passwords[-1]
        return None

    def set_password(self, new_password: str):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)

    def is_correct(self, attempt: str):
        return attempt == self.get_password()


if __name__ == "__main__":
    my_manager = PasswordManager("Test123")

    print("Testing set_password...")
    my_manager.set_password("Test1234")

    print(f"Current password is: {my_manager.get_password()}")
    print(f"Password history: {my_manager.old_passwords}")