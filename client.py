
import json
import requests
import socket

server_host = "0.0.0.0"
server_port = "8000"
prompt_file = "input.txt"
output_file = "output.json"

def send_to_server(prompt):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect((server_host,server_port))
        s.sendall(prompt.encode("utf-8"))
        data = s.recv(1024)
        responses = json.loads(data.decode("utf-8"))

def get_prompt():
    with open("input.txt","r") as read:
        return [line.strip() for line in f]

def make_json(responses):
    with open("output.json","w") as file:
        json.dump(responses,file)

def main():
    prompt = get_prompt()
    responses = find_responses(prompt)
    make_json(responses)    
    send_to_server(prompt)

if __name__=="__main__":
    main()