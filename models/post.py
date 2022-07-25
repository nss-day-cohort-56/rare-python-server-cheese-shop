class Post():
    """class initializer
    """
    def __init__(self, id, user_id, category_id, title, publication_date, image_url, content, approved):
        """function to create model of Post

        Args:
            id (_type_): _primary key/int_
            user_id (_type_): _foreign key/int_
            category_id (_type_): _foreign key/int_
            title (_type_): _text string_
            publication_date (_type_): _date_
            image_url (_type_): _text string_
            content (_type_): _text string_
            approved (_type_): _boolean_
        """
        self.id = id
        self.user_id = user_id
        self.category_id = category_id
        self.title = title
        self.publication_date = publication_date
        self.image_url = image_url
        self.content = content
        self.approved = approved
