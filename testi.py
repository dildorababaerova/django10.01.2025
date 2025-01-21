from http.server import HTTPServer, BaseHTTPRequestHandler
 
class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Set the content type
        self.send_header('Content-type', 'text/html')
        self.end_headers()
 
        # Define the HTML content
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Simple Web Server</title>
        </head>
        <body>
        <h1>Welcome to my simple web server!</h1>
            <p>This is a response from a Python server running on port 80.</p>
        </body>
        </html>
        """
 
        # Write the HTML content to the response
        self.wfile.write(html_content.encode('utf-8'))
 
# Set up the server to listen on port 80
port = 80
 
def run():
    httpd = HTTPServer(('', port), SimpleRequestHandler)
    print(f"Serving on port {port}... Press Ctrl+C to stop.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down the server...")
        httpd.server_close()
 
if __name__ == "__main__":
    run()