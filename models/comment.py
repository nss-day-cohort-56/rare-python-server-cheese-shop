class Comment():
    """Class initializer"""

    def __init__(self, id, post_id, author_id, content, publication_date):
        """function to create model of Comments"""
        self.id = id
        self.post_id = post_id
        self.author_id = author_id
        self.content = content
        self.publication_date = publication_date
