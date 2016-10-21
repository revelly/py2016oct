import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
print(Handler2.cgi_directories)

httpd = socketserver.TCPServer(("", PORT), Handler)

i=input("Yes")
print("serving at port", PORT)
httpd.serve_forever()
