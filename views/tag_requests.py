import sqlite3
import json
from models.tag import Tag

def get_all_tags():
    """retrieves all tags so client side can implement them in the DOM
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
            SELECT
                t.id,
                t.label
            FROM tags t
            ORDER BY t.label ASC    """)

        tags = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            tag = Tag(row['id'], row['label'])
            
            tags.append(tag.__dict__)
    return json.dumps(tags)