class User:
    """Class use to manage users registered in the database"""

    def __init__(self, user_id, name, surname, password, email, is_admin=False):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.password = password
        self.email = email
        self.is_admin = is_admin
        self.wishlist = []

    def show(self):
        return f"Utilisateur: {self.name} {self.surname}\nID: {self.user_id}\nEmail: {self.email}\n"
