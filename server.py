import google.generativeai as genai
import uuid 
import json
import requests
import time
import threading

server_host = "0.0.0.0"
server_port = "8000"
prompt_file = "input.txt"
output_file = "output.json"

def get_response(client):
    prompt = client.recv(1024).decode('utf-8')
    genai.configure(api_key = "AIzaSyAsxpuioHx9n-ToX9_Sp8ixuzpfMVd1xAU")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    responses = []
    time = int(time.time())
    responses.append({
        "prompt":f"{prompt}",
        "response":response.text,
        "source":"gemma",
        "time":f"{time}"
    })
    for t in responses:
        t_id = uuid.uuid5()
        ids[t_id] = t
    for i , t in enumerate(responses):
        t["ClientID"] = list(ids.keys())[i] 
    with connections_lock :
        for c in Connections:
            c.sendall(responses.encode("utf-8"))
            c.close()
            connections.remove(c)

    client.close()
    connections.remove(client)
    
def start():
    global Connections
    Connections = []
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind((server_host,server_port))
        s.listen(15)
        while True:
            client , _ = s.accept()
            with connections_lock:
                Connections.append(client)
            client = threading.Thread(target=get_response,args=(client),)   
            client.start()

if __name__ == "__main__":
    start()