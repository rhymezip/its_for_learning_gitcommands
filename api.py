from fastapi import FastAPI

app = FastAPI()

notlar = [
        {"id": 1, "baslik" : "alisveris", "icerik": "ekmek al"},
        {"id": 2, "baslik": "toplanti", "icerik": "saat 10 da gel"}
        ]

@app.get("/notlar")
def notlari_getir():
    return {"notlar": notlar}

@app.get("/notlar/{not_id}")
def not_getir(not_id: int):
    for not_item in notlar:
        if not_item["id"] == not_id:
            return not_item
    return {"hata": "not bulunmadi"}

@app.post("/notlar")
def not_ekle(baslik: str, icerik: str):
    yeni_id = max(item["id"] for item in notlar) + 1
    yeni_not = {
            "id": yeni_id,
            "baslik": baslik,
            "icerik": icerik
            }
    notlar.append(yeni_not)
    return {"eklendi": yeni_not}

@app.delete("/notlar/{not_id}")
def not_sil(not_id: int):
    for i, item in enumerate(notlar):
        if item["id"] == not_id:
            notlar.pop(i)
            return {"silindi": not_id}
    return {"hata": "not bulunmadi"}

@app.put("/notlar/{not_id}")
def not_guncelle(not_id: int, baslik: str, icerik: str):
    for item in notlar:
        if item["id"] == not_id:
            item["baslik"] = baslik
            item["icerik"] = icerik
            return{"guncellendi": item}
    return {"hata": "not bulunmadi"}
