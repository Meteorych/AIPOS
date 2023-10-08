import argparse
from http.server import BaseHTTPRequestHandler, HTTPServer

class OurHttpHandler(BaseHTTPRequestHandler):
    # Handling of HTTP-request
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Get request!')

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Post request')
        pass

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Options request')
        pass

def run_server(port):
    server_address = ('', port)
    httpd = HTTPServer(server_address, OurHttpHandler)
    print(f'Starting server on port {port}')
    httpd.serve_forever()
    if KeyboardInterrupt:
        httpd.server_close()