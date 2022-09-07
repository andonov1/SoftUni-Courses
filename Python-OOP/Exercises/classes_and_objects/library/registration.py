from Exercises.classes_and_objects.library.library import Library
from Exercises.classes_and_objects.library.user import User


class Registration:
    def add_user(self, user: User, library: Library):
        for user_record in library.user_records:
            if user_record.user_id == user.user_id:
                return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)
        library.rented_books[user.username] = {}

    def remove_user(self, user: User, library: Library):
        if user not in library.user_records:
            return "We could not find such user to remove!"
        library.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str, library: Library):
        for user in library.user_records:
            if user.user_id == user_id and new_username != user.username:
                if user.username in library.rented_books:
                    current_user_books = library.rented_books[user.username]
                    library.rented_books.pop(user.username)
                    user.username = new_username
                    library.rented_books[user.username] = current_user_books
                return f"Username successfully changed to: {new_username} for user id: {user_id}"
            if user.user_id == user_id and new_username == user.username:
                return "Please check again the provided username - it should be different than the username used so far!"
        return f"There is no user with id = {user_id}!"