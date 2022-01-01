from fastapi import FastAPI
from animeflv import AnimeFLV


api = AnimeFLV()  
app = FastAPI()

@app.get("/search")
def search(name: str):
  print(name)
  return api.search(name)

@app.get("/animeInfo")
def animeInfo(info: str):
  return api.getAnimeInfo(info)

@app.get("/getVideoServers")
def getVideoServers(video: str):
  return api.getVideoServers(video)
