import json

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

CONFIG_FILE = "config.json"
SCHEMA_FILE = "schema.json"

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # 画面表示時に現在の設定とスキーマを読み込む
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        config_data = json.load(f)
    with open(SCHEMA_FILE, "r", encoding="utf-8") as f:
        schema_data = json.load(f)

    # 修正ポイント: 第2引数を context={"request": request, ...} にする
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "config": config_data,
            "schema": schema_data
        }
    )

@app.post("/save")
async def save_config(data: dict):
    # 編集されたデータを保存
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # ここでPythonプログラムを呼び出す例
    # os.system("python my_bot_script.py")

    return {"message": "保存してプログラムを実行しました"}
