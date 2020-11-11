#!/usr/bin/env python3
import http.server as SimpleHTTPServer
import socketserver as SocketServer
from valve.source.a2s import ServerQuerier
from valve.source import NoResponseError
PORT = 8000

class GetHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def retrieveIdkPlayers(self, ip):
        try:
            ipA = str(ip).replace('/','').split(":")
            ip = (str(ipA[0]), int(ipA[1]))        
            server = ServerQuerier(ip, 0.5)
            info = server.info()
            return info['player_count']
        except Exception as e:
            return 0
        return total

    def do_GET(self):
        total = self.retrieveIdkPlayers(self.path)
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(str(total).encode(encoding='utf_8'))

Handler = GetHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
httpd.serve_forever()
