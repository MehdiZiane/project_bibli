class User:
    """Class use to manage users registered in the database"""

    def __init__(self, user_id, nom, prenom, mdp, email, is_admin=False):
        self.user_id = user_id
        self.nom = nom
        self.prenom = prenom
        self.mdp = mdp
        self.email = email
        self.is_admin = is_admin
        self.wishlist = []

    def show(self):
        return f"Utilisateur: {self.nom} {self.prenom}\nID: {self.user_id}\nEmail: {self.email}\n"
