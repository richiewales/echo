from itertools import combinations
from llama_cpp import Llama
from sys import platform
import os

model_dir = 'Llama-2-7B-Chat-GGML'
model_file = 'llama-2-7b-chat.ggmlv3.q4_0.bin'
n_gpu_layers = 0

if platform == 'darwin':
    n_gpu_layers = 1

def generate_post(topic):
    llm = Llama(model_path=os.path.join('/Users/richiew/Documents/echo/echosite', 'models', model_dir, model_file), n_gpu_layers=n_gpu_layers)
    output = llm("Q: Generate a tweet about {}.  A: ".format(topic), max_tokens=128, stop=["Q:", "\n"], echo=True)
    output = output['choices'][0]['text'].split('A: ')[1]
    return output
    
prompts = ['anime', 'soccer', 'music', 'elon musk', 'travel', 'video games', 'ai', 'cats', 'dogs', 'fashion']
with open('output_tweets.txt', 'w') as out_file:
    for topic_set in set(list(combinations(prompts, 2))):
        topics = ' and '.join(list(topic_set))
        output = generate_post(topics)
        print(output)
        out_file.write(output)
        out_file.write('\n\n')