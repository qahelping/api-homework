import json
from csv import DictReader


def distribute_books():
    """Distributes books to users and writes the result to file in JSON format"""
    users_with_books = []

    with open("users.json", "r", encoding="utf-8") as users_file:
        users = json.loads(users_file.read())
        users_with_books = list(
            map(
                lambda user: {
                    "name": user["name"],
                    "gender": user["gender"],
                    "address": user["address"],
                    "age": user["age"],
                    "books": [],
                },
                users,
            )
        )

    with open("books.csv", "r", encoding="utf-8") as books_file:
        reader = DictReader(books_file)

        i = 0
        total = len(users_with_books)
        for row in reader:
            users_with_books[i]["books"].append(
                {
                    "title": row["Title"],
                    "author": row["Author"],
                    "pages": row["Pages"],
                    "genre": row["Genre"],
                }
            )
            i = i + 1
            if i == total:
                i = 0

    with open("result.json", "w", encoding="utf-8") as result_file:
        json_result = json.dumps(users_with_books, indent=4)
        result_file.write(json_result)


distribute_books()
