import uvicorn

if __name__ == "__main__":
    uvicorn.run("server.runapp:app", host="localhost", port=8000, reload=True)