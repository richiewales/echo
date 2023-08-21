from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from typing import Optional
from llama_cpp import Llama
from echosite.settings import BASE_DIR
import os

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the posts index.")

def generate_post(request):
    llm = Llama(model_path=os.path.join(BASE_DIR, 'models/Llama-2-7B-Chat-GGML/llama-2-7b-chat.ggmlv3.q4_0.bin'))
    output = llm("Q: Generate a tweet about catgirls and honda civis.  A: ", max_tokens=128, stop=["Q:", "\n"], echo=True)
    output = output['choices'][0]['text'].split('A: ')[1]
    return JsonResponse({'prompt': output})