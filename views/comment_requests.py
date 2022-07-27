import json
import sqlite3

from models.comment import Comment


def get_all_comments():
    """Function to get all of the comments"""

    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.post_id,
            c.author_id,
            c.content
        FROM Comments c
        """)

        comments = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            comment = Comment(row['id'], row['post_id'],
                              row['author_id'], row['content'])

            comments.append(comment.__dict__)

        return json.dumps(comments)


def get_single_comment(id):
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.post_id,
            c.author_id,
            c.content
        FROM Comments c
        WHERE c.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        comment = Comment(data['id'], data['post_id'],
                          data['author_id'], data['content'])

        return json.dumps(comment.__dict__)


def get_comments_by_post_id(post_id):
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.post_id,
            c.author_id,
            c.content,
            p.id
        FROM Comments c
        JOIN Posts p
            ON c.post_id = p.id
        """, (post_id, ))

        comments = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            comment = Comment(row['id'], row['post_id'],
                              row['author_id'], row['content'])

            comments.append(comment.__dict__)

        return json.dumps(comments)


def create_comment(new_comment):
    """Summary: Function to create new comment"""
    with sqlite3.connect("./db.sqlite3") as conn:

        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Comments
            (post_id, author_id, content)
            VALUES  
            (?,?,?)
        """, (new_comment['post_id'], new_comment['author_id'], new_comment['content']))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the entry dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_comment['id'] = id

    return json.dumps(new_comment)


def update_comment(id, new_comment):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Comments
            SET
                content = ?
        WHERE id = ?
        """, (new_comment['content'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True


def delete_comment(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Comments
        WHERE id = ?
        """, (id, ))
