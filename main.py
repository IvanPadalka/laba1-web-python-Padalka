from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()

print("Set-cookie: name=value; expires=Wed May 18 03:33:20 2033; path=/cgi-bin/; httponly")

print("Content-type: text/html\n")
print("Cookies!!!")