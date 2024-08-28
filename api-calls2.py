import google.generativeai as genai
import uuid 
import json
import requests
import time
prompt = input("what is the prompt ")
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
with open("output.json","w") as file:
    json.dump(responses,file)









