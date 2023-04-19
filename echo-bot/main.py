import os, json
from fastapi import FastAPI, Request, Response
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError

PUBLIC_KEY = os.getenv("MINIAPP_PUBLIC_KEY")

app = FastAPI()

@app.post("/")
async def target(req: Request, res: Response):

  # Your public key can be found on your application in the Developer Portal
  verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))

  signature = req.headers["X-Signature-Ed25519"]
  timestamp = req.headers["X-Signature-Timestamp"]
  body = (await req.body()).decode("utf-8")

  try:
    verify_key.verify(f'{timestamp}{body}'.encode(), bytes.fromhex(signature))
  except BadSignatureError:
    res.status_code = 401
    return {"error": "Invalid request signature"}

  data = json.loads(body)
  if data.get("type") == 1: return {"type": 1}

  return { "type": 4, "data": { "content": "echo" } }