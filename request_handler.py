
import json

from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer
from views.post_requests import get_posts_by_user_id

import json
from views.user import create_user, login_user
# POSTS

from views import get_all_posts
from views import get_single_post
from views import delete_post
from views import create_post


from views import (
    get_all_posts,
    get_single_post,
    delete_post)


# USERS
from views import create_user
from views import login_user

class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""

    def parse_url(self, path):
        """Parse the url into the resource and id"""
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split('/')
        resource = path_params[1]
        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)
        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass
        return (resource, pk)

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the OPTIONS headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        """Handle Get requests to the server"""
        # Set the response code to "Ok"
        self._set_headers(200)

        response = {}

        parsed = self.parse_url(self.path)
        if '?' not in self.path:
            (resource, id) = parsed

            if resource == "posts":
                if id is not None:
                    response = f"{get_single_post(id)}"
                else:
                    response = f"{get_all_posts()}"
        else:  # THere is a ? in the path, run the query param functions
            (resource, query) = parsed

            if query.get('user_id') and resource == "posts":
                response = get_posts_by_user_id(query['user_id'][0])

        self.wfile.write(f"{response}".encode())

    def do_POST(self):
        """Make a post request to the server"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))

        (resource, id) = self.parse_url(self.path)

        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        post_body = json.loads(self.rfile.read(content_len))

        (resource, id) = self.parse_url(self.path)


        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize the new post
        new_post = None
        user = None
        if resource == 'login':
            user = login_user(post_body)
            self.wfile.write(f"{user}".encode())
        if resource == 'register':
            user = create_user(post_body)
            self.wfile.write(f"{user}".encode())
        if resource == "posts":
            new_post = create_post(post_body)
            self.wfile.write(f"{new_post(id)}".encode())

    # def do_PUT(self):
    #     """Handles PUT requests to the server"""
    #     pass

    def do_DELETE(self):
        """Handle DELETE Requests"""
        self._set_headers(204)
        (resource, id) = self.parse_url(self.path)
        if resource == "posts":
            delete_post(id)



def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
