from http.server import HTTPServer, BaseHTTPRequestHandler

import requests

hostname = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """Класс, который отвечает за обработку входящих запросов от клиентов."""

    def do_GET(self):
        try:
            # URL к файлу contacts.html в репозитории
            url = "https://raw.githubusercontent.com/username/repository/main/contacts.html"
            response = requests.get(url)
            content = response.text

            # отправляем ответ
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f"Ошибка: {str(e)}".encode('utf-8'))

    # обрабатываем POST-запрос
    def do_POST(self):
        # получаем длину данных
        content_length = int(self.headers['Content-Length'])
        # читаем данные из запроса
        post_data = self.rfile.read(content_length).decode('utf-8')
        # выводим данных в консоль
        print("Получены данные POST-запроса:")
        print(post_data)

        # URL к файлу contacts.html в репозитории
        url = "https://raw.githubusercontent.com/username/repository/main/contacts.html"
        response = requests.get(url)
        content = response.text

        # отправляем ответ
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))


# запускаем сервер
def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Сервер запущен на порту {port}")
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()
