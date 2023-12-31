# echo
AI generated content feed for maximum rat-wheeling 🐀

## Update python env with dependencies (Need to do this as of 8/21)
```
pip install -r requirements.txt
```

## Download model binaries
Make sure you have git-lfs installed (https://git-lfs.com)
```
cd echosite/models
git lfs install
git clone https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML
```

You should have the dir structure:
```
echo/echosite/models/Llama-2-7B-Chat-GGML
```

## Get Llama Metal GPU support (macOS)
```
pip uninstall llama-cpp-python -y
CMAKE_ARGS="-DLLAMA_METAL=on" FORCE_CMAKE=1 pip install -U llama-cpp-python==0.1.68 --no-cache-dir
```

## Supported Topics
1. anime
1. soccer
1. music
1. elon musk
1. travel
1. video games
1. ai
1. cats
1. dogs
1. fashion

## Mascot
![image](echo-chan.png)