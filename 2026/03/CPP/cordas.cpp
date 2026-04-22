#include <iostream>
#include <string>
using namespace std;

int main() {
	string mensagem = "Bem-vindo e Adeus \n";
	// Descobri que string são  objetos em cpp também!! E que eu posso usar funções delas, como por exemplo append
	
	string outramsg = mensagem.append("Mais coisa");
	cout << outramsg;
	return 0;
}
