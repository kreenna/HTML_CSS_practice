from http.server import HTTPServer, BaseHTTPRequestHandler

# определяем настройки запуска
hostName = "localhost"  # адрес для доступа по сети
serverPort = 8080  # порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """ Метод для обработки GET-запросов """
        self.send_response(200)  # отправляем код ответа
        self.send_header("Content-type", "text/html")  # отправляем тип данных
        self.end_headers()  # завершаем формирование заголовков ответа
        with open("contacts.html", "r", encoding="utf-8") as file:
            data = file.read()
        self.wfile.write(bytes(data, "utf-8"))

    def do_POST(self):
        """Метод для обработки POST-запросов."""
        # получаем длину данных
        content_length = int(self.headers['Content-Length'])
        # читаем данные из запроса
        post_data = self.rfile.read(content_length).decode('utf-8')
        # выводим данные в консоль
        print("Получены данные POST-запроса:")
        print(post_data)


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # запускаем веб-сервер в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
