import sqlite3
import json
from models import Post

# def get_all_posts():
#     """function to respond to client side for ./posts
#     """
#     with sqlite3.connect("./db.sqlite3") as conn:
#         conn.row_factory = sqlite3.Row
#         db_cursor = conn.cursor

#         db_cursor.execute("""
#         SELECT
#             p.id
#             p.user_id
#             p.category_id
#             p.title
#             p.publication_date
#             p.image_url
#             p.content
#             p.approved
#         FROM Post p
#         """)

#         posts = []

#         dataset = db_cursor.fetchall()

#         for row in dataset:

#             post = Post(row['id'],)