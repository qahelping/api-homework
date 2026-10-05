import csv
import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
BOOKS_FILE = BASE_DIR / 'books.csv'
USERS_FILE = BASE_DIR / 'users.json'
RESULT_FILE = BASE_DIR / 'result.json'

def reading_books(file_path: Path):
    books = []
    csv_file = open(file_path, encoding='utf-8')
    reader = csv.DictReader(csv_file)
    for row in reader:
        book = {
            'title': row['Title'],
            'author': row['Author'],
            'pages': int(row['Pages']),
            'genre': row['Genre'],
        }
        books.append(book)
    csv_file.close()
    return books


def reading_users(file_path: Path):
    result_users = []
    json_file = open(file_path, encoding='utf-8')
    users = json.load(json_file)
    for user in users:
        new_user = {
            'name': user['name'],
            'gender': user['gender'],
            'address': user['address'],
            'age': user['age'],
            'books': [],
        }
        result_users.append(new_user)
    json_file.close()
    return result_users


def books_distribution(users, books):
    for index, book in enumerate(books):
        user_index = index % len(users)
        users[user_index]['books'].append(book)
    return users


def save_result(file_path, data):
    json_file = open(file_path, 'w', encoding='utf-8')
    json.dump(data, json_file, ensure_ascii=False, indent=4)
    json_file.close()


def main():
    books = reading_books(BOOKS_FILE)
    users = reading_users(USERS_FILE)
    result = books_distribution(users, books)
    save_result(RESULT_FILE, result)


if __name__ == '__main__':
    main()