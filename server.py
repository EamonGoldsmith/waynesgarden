# Import the required module
import http.server

# Set the port number
PORT = 8000

# Create an HTTP server object
server = http.server.HTTPServer(("[website url]", PORT), http.server.SimpleHTTPRequestHandler)

# Run the server
server.serve_forever()

