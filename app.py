from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import os

class ConectaPetHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Rota para simular uma API de cuidadores de Pets
        if self.path == '/api/cuidadores':
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.end_headers()
            
            # Seus dados atualizados com as fotos locais
            cuidadores = [
                {
                    "id": 1,
                    "nome": "Nikolas Ferreira",
                    "servico": "Pet Sitter (Hospedagem)",
                    "bairro": "Copacabana",
                    "preco": "R$ 60/dia",
                    "avaliacao": "⭐️ 4.9",
                    "foto": "nikolas.png"
                },
                {
                    "id": 2,
                    "nome": "Giselle Tonha",
                    "servico": "Dog Walker (Passeadora)",
                    "bairro": "Botafogo",
                    "preco": "R$ 35/passeio",
                    "avaliacao": "⭐️ 4.8",
                    "foto": "giselle.png"
                },
                {
                    "id": 3,
                    "nome": "Ian Gostoso",
                    "servico": "Pet Sitter & Passeador",
                    "bairro": "Flamengo",
                    "preco": "R$ 50/dia",
                    "avaliacao": "⭐️ 5.0",
                    "foto": "ian.png"
                }
            ]
            self.wfile.write(json.dumps(cuidadores).encode('utf-8'))
        else:
            # Serve os arquivos estáticos (index.html, etc) normalmente
            super().do_GET()

if __name__ == '__main__':
    # Configuração correta e única para o Railway funcionar online
    porta = int(os.environ.get("PORT", 8000))
    server_address = ('0.0.0.0', porta)
    
    httpd = HTTPServer(server_address, ConectaPetHandler)
    print(f"🚀 Servidor online na porta {porta}")
    httpd.serve_forever()
