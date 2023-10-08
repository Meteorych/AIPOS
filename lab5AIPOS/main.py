import argparse
import json
import server
from client import send_request

payload = {'key1': 'value1', 'key2': 'value2'}
def main():
    parser = argparse.ArgumentParser(description='HTTP Server and Client')
    parser.add_argument('--port', type=int, default=8000, help='Port to listen on for the server')
    parser.add_argument('--start-server', action='store_true', help='Start the HTTP server')
    parser.add_argument('--url', type=str, help='URL to send the request to')
    parser.add_argument('--method', type=str, default='GET', help='HTTP method (GET by default), also there is support for POST and OPTIONS')
    parser.add_argument('--headers', type=str, help='Headers as a JSON string')
    parser.add_argument('--data', type=str, help='Request data', default=payload)
    args = parser.parse_args()

    if args.start_server:
        server.run_server(args.port)
    elif args.url:
        headers = None
        if args.headers:
            headers = json.loads(args.headers)

        response = send_request(args.url, args.method, headers, args.data)
        print(f'Status Code: {response[0]}')
        print('Response Content:')
        print(response[1])


if __name__ == '__main__':
    main()