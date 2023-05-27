import json
from classes.class_user import User

class UserDatabase:
    def __init__(self):
        self.users = self.load_users_from_file()

    def load_users_from_file(self):
        try:
            with open("./bd/user.json", "r") as file:
                self.users = json.load(file)
                return self.users
        except FileNotFoundError:
            return []

    def save_users_to_file(self):
        with open("./bd/user.json","w") as file:
            json.dump(self.users, file, indent=4)

    def create_account(self, nom, prenom, email, password):
        # Génération d'un identifiant unique pour le nouvel utilisateur
        user_id = len(self.users) + 1

        # Ajout du nouvel utilisateur à la base de données
        dude = {
            'id': user_id,
            'nom': nom,
            'prenom': prenom,
            'mdp': password,
            'email': email,
            'admin': False
        }
        self.users.append(dude)
        self.save_users_to_file()

    
    def remove_user(self, user_id):
        # Recherche du user à supprimer
        index = None
        for i, dude in enumerate(self.users):
            if dude['id'] == user_id:
                index = i
                break

        if index is not None:
            # Suppression du livre de la liste
            del self.users[index]
            # Enregistrement des modifications dans le fichier JSON
            self.save_users_to_file()
            print(f"user avec ID {user_id} supprimé.")
        else:
            print(f"user avec ID {user_id} introuvable.")

    def authenticate_user(self, email, password):
        for user in self.users:
            if user['email'] == email and user['mdp'] == password:
                return user
        return None