#include <iostream>
#include <cstring>
#include <unistd.h>
#include <netinet/in.h>

int main() {
	//Создаем TCP сокет (IPv4, TCP, протокол автоматом)
	int server_fd = socket(AF_INET, SOCK_STREAM, 0);

	//Структура адреса сервера
	sockaddr_in address{};

	address.sin_family = AF_INET; //Все еще IPv4
	address.sin_addr.s_addr = INADDR_ANY; //любой айпишник канает
	address.sin_port = htons(3000); //Порт - 3000

	bind(server_fd, (sockaddr*)&address, sizeof(address)); //Теперь мы забиндились к 0.0.0.0:8080 чтобы это не значило

	listen(server_fd, 1);//мы теперь ждун (привет из... БОГ ТЫ МОЙ, 2016 БЫЛ 10 ЛЕТ НАЗАД!?)

	int addrlen = sizeof(address);

	while (true){
		int client = accept(server_fd, (sockaddr*)&address, (socklen_t*)&addrlen);

		char buffer[1024] = {0};
		read(client, buffer, 1024);

		const char* response =
			"HTTP/1.1 418 I'm a teapot\r\n"
			"Content-Type: text/plain\r\n"
			"Content-Length: 12\r\n"
			"\r\n";

		send(client, response, strlen(response), 0);
		close(client);
	}


	return 0;
}