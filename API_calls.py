import google.generativeai as genai 
import time
import json
import requests
with open("input.txt","r") as r:
    prompt = [line.strip() for line in read]
genai.configure(api_key = "AIzaSyAsxpuioHx9n-ToX9_Sp8ixuzpfMVd1xAU")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(prompt)
responses = []
time = time.time()
responses.append({
    "prompt":f"{prompt}",
    "response":response.text,
    "source":"gemini",
    "time":f"{time}"
})
with open("output.json","w") as file:
    json.dump(responses,file)


