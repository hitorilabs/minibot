from fastapi import FastAPI, Request, Response

app = FastAPI()

@app.post("/")
async def target(request: Request) -> Response:
  data = await request.json()
  return data