import json
from classes.class_user import User


class UserDatabase:
    def __init__(self):
        self.users = self.load_users_from_file()

    def load_users_from_file(self):
        """Function for loading user from the JSON file

        Returns:
            Enable users loaded in the file to be returned, or enable other parts of the program to have access to this file.
        """
        try:
            with open("./db/user.json", "r") as file:
                self.users = json.load(file)
                return self.users
        except FileNotFoundError:
            return []

    def save_users_to_file(self):
        """Function for saving users in the JSON file"""
        with open("./db/user.json", "w") as file:
            json.dump(self.users, file, indent=4)

    def create_account(self, name, surname, email, password):
        """Fuction enabling the user to create an account in the library

        Args:
            nom (char): name chosen and entered by the user
            prenom (char): first name chosen and entered by the user
            email (char): email address chosen and entered by the user
            password (char): password chosen and entered by the user
        """

        # Create a single id for the new user
        user_id = len(self.users) + 1

        # Adding a new user to the database
        dude = {
            "id": user_id,
            "name": name,
            "surname": surname,
            "password": password,
            "email": email,
            "admin": False,
            "wishlist": [],
        }
        self.users.append(dude)
        self.save_users_to_file()

    def remove_user(self, user_id):
        """Function for deleting a user account from the library

        Args:
            user_id : the user id to be deleted from the list of users
        """

        # Search for the user to be deleted
        index = None
        for i, dude in enumerate(self.users):
            if dude["id"] == user_id:
                index = i
                break

        if index is not None:
            # Delete the book from the list
            del self.users[index]
            # Saving changes to the JSON file
            self.save_users_to_file()
            print(f"user ID {user_id} delete.")
        else:
            print(f"user ID {user_id} nowhere.")

    def authenticate_user(self, email, password):
        """Function used to check the information entered by the user at the time of connection

        Args:
            email (char): the email address register by the user
            password (char): the password register by the user

        Returns:
            _type_: _description_
        """
        for dude in self.users:
            if dude["email"] == email and dude["password"] == password:
                return dude
        return None

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user["id"] == user_id:
                return user
        return None
