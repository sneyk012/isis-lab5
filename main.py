import random
from http.server import HTTPServer, BaseHTTPRequestHandler


class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        if random.random() > 0.67:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("<h1>500</h1>", encoding='utf-8'))
        else:
            status = 200
            if self.path == '/':
                response_body = bytes("<h1>HELLO WORLD</h1>", encoding='utf-8')
            else:
                response_body = bytes("<h1>404 Not Found</h1>", encoding='utf-8')
                status = 404

            self.send_response(status)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(response_body)


def runserver(server_class=HTTPServer, handler_class=HttpProcessor):
    server_address = ('0.0.0.0', 1414)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.shutdown()


if __name__ == '__main__':
    runserver()