from fastapi import FastAPI
from sentence_transformers import SentenceTransformer, util
from fastapi.responses import JSONResponse



app = FastAPI()


model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')


@app.post('/get_embeddings')
async def get_embeddings(text: str):
    try:
        # Вычислить эмбеддинг текста
        embedding = model.encode(text, convert_to_tensor=True)
        print(embedding)

        # Создать словарь для возврата в формате JSON
        response_data = {"embedding": embedding.tolist()}  # Преобразовать Tensor в список для сериализации JSON

        # Вернуть JSONResponse с кодом состояния 200 (ОК)
        return JSONResponse(content=response_data, status_code=200)

    except Exception as e:
        # В случае ошибки возвращать JSON с кодом состояния 500 (Внутренняя ошибка сервера)
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post('/count_cos_similarity')
async def count_cos_similarity(vector_1, vector_2):
    return util.pytorch_cos_sim(vector_1, vector_2)


@app.get("/health")
def health_check():
    return {"status": "ok"}
