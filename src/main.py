from fastapi import FastAPI
from pydantic import BaseModel
import re
import pandas as pd
from validate_docbr import CPF

app = FastAPI()

#  Endpoint raiz para testar se a API está online
@app.get("/")
async def root(): 
    return {"message": "API RPA está rodando!"}

# Configuração do Swagger UI
@app.get("/openapi.json")
async def get_open_api():
    return get_open_api(title="RPA225", version="1.0.0", routes=app.routes)

#  Classe para receber comandos na API
class InputData(BaseModel):
    command: str

#  Função para validar CPF
def validar_cpf(cpf: str) -> bool:
    return CPF().validate(cpf)

# 🔹 Função que processa comandos enviados à API
def processar_comando(comando: str) -> str:
    if "gerar relatório" in comando.lower():
        df = pd.DataFrame({"Nome": ["João", "Maria"], "CPF": ["123.456.789-09", "987.654.321-00"]})
        df.to_csv("relatorio.csv", index=False)
        return "Relatório gerado com sucesso!"
    return "Comando não reconhecido."

# 🔹 Rota principal para receber comandos
@app.post("/executar")
async def executar_comando(data: InputData):
    resultado = processar_comando(data.command)
    return {"resposta": resultado}
