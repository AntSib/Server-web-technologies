from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs


class Simple_HTTP_Requst_Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(403, "NOt OK")
        self.send_header("Content-Type", "text/html; charset=UTF-8")
        self.end_headers()

        with open('index.html', encoding='utf-8') as f:
            result = list(map(lambda s: s.strip(), f.readlines()))
        
        result = ''.join(result)

        self.wfile.write(bytes(result, 'utf-8'))


httpd = HTTPServer(('localhost', 8080), Simple_HTTP_Requst_Handler)
httpd.serve_forever()

