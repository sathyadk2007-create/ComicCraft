 from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8001

server = HTTPServer(("127.0.0.1", PORT), SimpleHTTPRequestHandler)

print(f"ComicCraft running at http://127.0.0.1:{PORT}")

server.serve_forever()