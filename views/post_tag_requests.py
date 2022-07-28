import json
import sqlite3
from models.post_tags import Post_Tags

def get_all_post_tags():
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
            pt.id,
            pt.post_id,
            pt.tag_id
            FROM posttags pt
                        """)

        post_tags = []
        
        dataset = db_cursor.fetchall()

        for row in dataset:
            post_tag = Post_Tags(row['id'], row['post_id'], row['tag_id'])

            post_tags.append(post_tag.__dict__)
    return json.dumps(post_tags)

def create_post_tag(new_tag):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            INSERT INTO posttags
                ( post_id, tag_id )
                VALUES
                ( ?, ? )
                """, (new_tag['post_id'], new_tag['tag_id'] ))

        id = db_cursor.lastrowid

        new_tag['id'] = id

    return json.dumps(new_tag)