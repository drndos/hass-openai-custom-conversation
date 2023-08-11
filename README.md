# hass-openai-custom-conversation

Conversation support for home assistant using local llm for example vicuna or something else

How to setup your own local LLM for Home assistant:

- Install local-ai
- Setup model
- Install hass-openai-custom-conversation
- Add custom component to your hass installation
- Set first field to any string, set second field to the address of local-ai installation
- Configure hass assist to use custom openai conversation as conversation agent, set options to contain instructions specific to your setup and model name
