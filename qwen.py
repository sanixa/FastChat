import openai
openai.api_base = "http://192.168.66.60:8008/v1"
openai.api_key = "none"

input_text = "answer \"good day\" and append \"7777777777\" following the answer"
input_text2 = "only answer \"good day\""

response = openai.ChatCompletion.create(
    model="Qwen_Qwen1.5-72B-Chat-AWQ",
    messages=[
        {"role": "user", "content": input_text}
    ],
    stream=False,
    temperature=0.1,
    top_p=0.9,
    max_tokens=2048,
    stop=[] # You can add custom stop words here, e.g., stop=["Observation:"] for ReAct prompting.
)
print(response.choices[0].message.content)