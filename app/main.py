from fastapi import FastAPI, status

app = FastAPI(title="Dock Control", version="0.1.0")


@app.get("/health", status_code=status.HTTP_200_OK)
def health_check() -> dict[str, str]:
    return {"status": "ok"}
