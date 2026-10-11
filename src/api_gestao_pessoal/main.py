from fastapi import FastAPI, status

from api_gestao_pessoal.schemas.message import Message

app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK, response_model=Message)
def main():
    return {"Message": "Olá, Mundo!"}
