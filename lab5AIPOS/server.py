import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer

class OurHttpHandler(BaseHTTPRequestHandler):
    # Handling of HTTP-request
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello world!')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        # Parse the POST data as needed (e.g., as URL-encoded or JSON data)
        # For example, if it's URL-encoded data:
        post_data_dict = urllib.parse.parse_qs(post_data)

        # Access and process the data from post_data_dict
        if 'key' in post_data_dict:
            value = post_data_dict['key'][0]
            print(f'Received POST data: {value}')

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'POST request is received and processed')

    def do_OPTIONS(self):
        # Handle OPTIONS request
        self.send_response(200)
        self.send_header('Allow', 'GET, POST, OPTIONS')
        self.end_headers()
        self.wfile.write(b'Allowed methods: GET, POST, OPTIONS')

def run_server(port):
    server_address = ('', port)
    httpd = HTTPServer(server_address, OurHttpHandler)
    print(f'Starting server on port {port}')
    httpd.serve_forever()
    if KeyboardInterrupt:
        httpd.server_close()