# hass-vicuna-conversation
Conversation support for home assistant using vicuna or llama local llm

Uses similar to openAI APIs:
https://github.com/ggerganov/llama.cpp
https://github.com/keldenl/gpt-llama.cpp
https://huggingface.co/eachadea/ggml-vicuna-13b-1.1
https://www.home-assistant.io/integrations/openai_conversation/
https://github.com/home-assistant/core/tree/dev/homeassistant/components/openai_conversation

You can improve speed using GPU:
This works only on linux or WSL as far as I can tell, use new cuda branch
https://huggingface.co/TheBloke/vicuna-13B-1.1-GPTQ-4bit-128g
https://github.com/qwopqwop200/GPTQ-for-LLaMa
https://rentry.org/llama-tard-v2
https://github.com/matatonic/text-generation-webui

`python3 server.py --model vicuna-13B-1.1-GPTQ-4bit-128g --wbits 4 --groupsize 128 --model_type Llama --extensions openai --listen`


TBD:
https://github.com/ggerganov/whisper.cpp
