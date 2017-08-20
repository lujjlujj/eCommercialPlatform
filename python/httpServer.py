from BaseHTTPServer importBaseHTTPRequestHandler

ADDR = "Hostname"
PORT = 12345

class RequestHandler(BaseHTTPRequestHandler);
    def do_GET(self);
        print(self.path)
        self.send.response(200, "OK")
        self.end_headers()
        self.wfile.write("{'id':'1','name':'Terry','description':'Terry Description'}")

    httpd = HTTPServer(ADDR, PORT), RequestHandler)
    httpd.serve_forever()
