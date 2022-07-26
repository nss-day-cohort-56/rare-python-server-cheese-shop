import sqlite3
import json
from models import Post
from models.user import User


def get_all_posts():
    """function to respond to client side for ./posts
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
                SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.profile_image_url,
            u.created_on,
            u.active
        FROM Posts p
        JOIN users u
            ON u.id = p.user_id
        """)

        posts = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            post = Post(row['id'], row['user_id'], row['category_id'], row['title'],
                        row['publication_date'], row['image_url'], row['content'],
                        row['approved'])

            user = User(row['id'], row['first_name'], row['last_name'], row['email'],
                        row['bio'], row['username'], row['password'],
                        row['profile_image_url'], row['created_on'], row['active'])

            post.user = user.__dict__
            posts.append(post.__dict__)
    return json.dumps(posts)


def get_single_post(id):
    """function to return single post from list"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.profile_image_url,
            u.created_on,
            u.active
        FROM Posts p
        JOIN users u
            ON u.id = p.user_id
        WHERE p.id = ?
        """, (id, ))
        data = db_cursor.fetchone()

        post = Post(data['id'], data['user_id'], data['category_id'],
                    data['title'], data['publication_date'], data['image_url'],
                    data['content'], data['approved'])

        user = User(data['id'], data['first_name'], data['last_name'], data['email'],
                        data['bio'], data['username'], data['password'],
                        data['profile_image_url'], data['created_on'], data['active'])

        post.user = user.__dict__
        return json.dumps(post.__dict__)

def delete_post(id):
    """Delete Single Post
    Args:
        id (_type_): _Primary Key_
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Posts
        WHERE id = ?
        """, (id, ))


def get_posts_by_user_id(user_id):
    """This function will get all posts by the user_Id"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved
        FROM Posts p
        WHERE p.user_id = ?
        """, (user_id, ))

        user_posts = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            post = Post(row['id'], row['user_id'], row['category_id'], row['title'],
                        row['publication_date'], row['image_url'], row['content'], row['approved'])

            user_posts.append(post.__dict__)

        return json.dumps(user_posts)


def create_post(new_post):
    """
    Summary: function to create a new post

    Args:
        new_post
    """
    with sqlite3.connect("db.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        INSERT INTO Posts
            ( user_id, category_id, title, publication_date, image_url, content, approved)
            VALUES
            (?, ?, ?, ?, ?, ?, ?);
        """, (new_post['user_id'], new_post['category_id'], new_post['title'],
              new_post['publication_date'], new_post['image_url'],
            new_post['content'], new_post['approved']))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id= db_cursor.lastrowid

        # Add the `id` property to the entry dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_post['id'] = id

    return json.dumps(new_post)

