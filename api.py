from fastapi import FastAPI

app = FastAPI()

liste = [
        {"id": 1, "baslik": "alisveris", "icerik": "ekmek al"},
        {"id": 2, "baslik": "toplanti", "icerik": "yarin saat 10 da"}
        ]

@app.get("/notlar")
def notlari_getir():
    return {"notlar": liste}

@app.get("/notlar/{not_id}")
def not_getir(not_id: int):
    for not_item in liste:
        if not_item["id"] == not_id:
            return not_item
    return {"hata": "not bulunmadi"}
