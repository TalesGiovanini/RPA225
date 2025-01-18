# 🏆 Documentação do Projeto RPA225

🚀 **RPA225** é uma API desenvolvida com **FastAPI** para automação de tarefas e validação de CPF.

## 📌 Funcionalidades

✅ Validação de CPF  
✅ Processamento de comandos  
✅ Geração de relatórios em CSV  
✅ API com documentação automática via Swagger  

## 🚀 Como Executar o Projeto

### **1️⃣ Clonar o Repositório**
```bash
git clone https://github.com/TalesGiovanini/RPA225.git
cd RPA225

2️⃣ Criar e Ativar o Ambiente Virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3️⃣ Instalar as Dependências
pip install -r requirements.txt

4️⃣ Rodar a API
uvicorn src.main:app --host 0.0.0.0 --port 8080 --reload

Após isso, a API estará rodando em:
👉 http://127.0.0.1:8080/

📖 Documentação da API
A API gera automaticamente uma documentação interativa com Swagger. Para acessar, abra no navegador:

👉 Swagger UI: http://127.0.0.1:8080/docs
👉 Redoc: http://127.0.0.1:8080/redoc

📡 Endpoints

🔹 Testar se a API está online
GET /

📌 Retorno esperado

{
  "message": "API RPA está rodando!"
}

🔹 Validar CPF
POST /executar

📌 Exemplo de Requisição

{
  "command": "Validar CPF 123.456.789-09"
}

📌 Retorno esperado

{
  "resposta": "CPF válido: True"
}

🔹 Gerar Relatório CSV
POST /executar

📌 Exemplo de Requisição

{
  "command": "gerar relatório"
}

📌 Retorno esperado

{
  "resposta": "Relatório gerado com sucesso!"
}

🛠 Testes Automatizados
O projeto contém testes automatizados para garantir a qualidade do código.

📌 Para rodar os testes, execute:
pytest tests/test_main.py

📜 Licença
Este projeto está licenciado sob a MIT License. Sinta-se livre para contribuir e aprimorá-lo! 🚀

📩 Contato
📧 Email: talesgiovanini@gmail.com
🐙 GitHub: TalesGiovanini
