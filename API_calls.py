import google.generativeai as genai 
import json
import requests
prompt = input("what is the prompt ")
genai.configure(api_key = "AIzaSyAsxpuioHx9n-ToX9_Sp8ixuzpfMVd1xAU")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(prompt)
responses = []
responses.append({
    "prompt":f"{prompt}",
    "response":response.text,
    "source":"gemini"
})
with open("output.json","w") as file:
    json.dump(responses,file)


