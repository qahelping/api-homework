import csv
import json

import pandas as pd
CSV_FILE_PATH = ''
JSON_FILE_PATH = ''

# get number of books
with open(CSV_FILE_PATH, newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    result = pd.read_csv(CSV_FILE_PATH)
    for row in reader:
        dict1 = dict(zip(header, row))
        del dict1['Publisher']
    book_len = len(result)

# get nuber of users
with open(JSON_FILE_PATH, "r") as f3:
    users = json.load(f3)
    user_len = len(users)

#  calculation of book amount per user
books_amount = list()
a = book_len // user_len
b = book_len % user_len
c = user_len - b + 1
for i in range(b):
    books_amount.append(a + 1)
for k in range(user_len - b):
    books_amount.append(a)

# remove the last column in books
with open(JSON_FILE_PATH, "r") as f0:
    with open(CSV_FILE_PATH, newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        new_books = []
        for row in reader:
            dict1 = dict(zip(header, row))
            del dict1['Publisher']
            new_books.append(dict1)

# write into result file
with open("result.json", "w") as f1:
    with open(JSON_FILE_PATH, "r") as f0:
        users = json.load(f0)
        users_small = {}
        new_users = [0] * user_len
        position = 0
        # go through users

        for j in range(user_len):
            user_books = []
            # leave only required fields from users
            for k, v in users[j].items():
                if k in ('name', 'gender', 'address', 'age'):
                    users_small[k] = v

            # adding books for each user, amount of books for each is taken from books_amount

            for i in range(position, books_amount[j] + position):
                user_books.append(new_books[i])
            position = position + books_amount[j]
            users_small['books:'] = user_books
            # adding a new edited user to new_users list
            new_users[j] = users_small
            users_small = {}

        s = json.dumps(new_users, indent=4)
    f1.write(s)