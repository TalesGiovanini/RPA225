📄 Documentação do Projeto RPA225
RPA225 - Robotic Process Automation (RPA) Simples
Descrição:
O RPA225 é um projeto de automação de processos utilizando Python e FastAPI. Ele fornece endpoints para validar CPF e gerar relatórios automaticamente. 🚀

📌 Tecnologias Utilizadas
Python 3.12+
FastAPI - Framework para criação de APIs rápidas
Uvicorn - Servidor ASGI para execução do FastAPI
Pandas - Manipulação de dados e geração de relatórios
Validate-docbr - Validação de CPF
Git/GitHub - Controle de versão

📂 Estrutura do Projeto
RPA225/
│── src/
│   ├── main.py          # Código principal da API
│── tests/
│   ├── test_main.py     # Arquivos de teste
│── venv/                # Ambiente virtual (não versionado)
│── requirements.txt     # Dependências do projeto
│── README.md            # Documentação do projeto
│── .gitignore           # Arquivos ignorados pelo Git
│── LICENSE              # Licença do projeto

⚡ Instalação
1️⃣ Clone o repositório

git clone https://github.com/SEU_USUARIO/RPA225.git
cd RPA225

2️⃣ Crie e ative um ambiente virtual

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

3️⃣ Instale as dependências

pip install -r requirements.txt

🚀 Como Executar
Rodar o servidor FastAPI com Uvicorn:

uvicorn src.main:app --host 0.0.0.0 --port 8080 --reload

Agora, acesse a API no navegador:

👉 http://127.0.0.1:8080

Para testar os endpoints via interface Swagger:

👉 http://127.0.0.1:8080/docs

🛠️ Endpoints Disponíveis
1️⃣ Verificar se a API está rodando
Método: GET
Endpoint: /
Resposta:

{"message": "API RPA está rodando!"}

2️⃣ Validar CPF
Método: POST
Endpoint: /executar

Exemplo de Requisição:

{
  "command": "Validar CPF 123.456.789-09"
}

Resposta:

{
  "resposta": "CPF válido: True"
}

3️⃣ Gerar Relatório
Método: POST
Endpoint: /executar
Exemplo de Requisição:

{
  "command": "Gerar relatório"
}

Resposta:

{
  "resposta": "Relatório gerado com sucesso!"
}

📌 Testes Automatizados
O projeto conta com testes automatizados para garantir a qualidade do código.

Para rodar os testes:

pytest tests/test_main.py

📜 Licença
Este projeto está licenciado sob a MIT License. Sinta-se livre para contribuir e aprimorá-lo! 😃

📞 Contato
Caso tenha dúvidas ou sugestões, entre em contato: 📧 Email: talesgiovanini@gmail.com
🌎 GitHub: TalesGiovanini


