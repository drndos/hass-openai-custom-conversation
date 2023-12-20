# Home Assistant Custom LLM Conversation

This will add a converstaion option to Home Assistant with any local running LLM through text-gen-webui. There are some workarounds needed, but once setup you can choose various LLMs and test/tweak them using a UI.

# Requirements
- Server for Text-Gen-WebUI with a compatible NVIDIA GPU. Preferably with 6GB VRAM or more.
- Home Assistant Server
- HACS installed on Home Assistant Server
- Wyoming Protocal Integration (*Optional, but required for voice interaction*)
- Piper (*Optional, but required for voice interaction*)
- Whisper (*Optional, but required for voice interaction*)

# Installation

This is going to be a two part installation and is going to look very different depending on how you want to install everything. 

**Part 1 | Install Oobabooga's Text-Gen-WebUI**
- I was able to get this running with Windows 11, but I wanted this on my Unraid server, so I opted for a dockerized version of text-gen-webui. I will be updating this guide once I get some more time.

**Part 2 | Install a Custom Component to Home Assisant**

Step 1: HACS
- Open HACS and click "Integrations" from the menu.
- Select the three dots in the top right.
- Click on Custom Repositories.
- Copy the url from this repo and paste into the first field.
- Select Integration from the second field.

Step 2: Devices & Services
- Open the devices & services menu from the settings menu
- Click on "Add Integration"
- Search/Add Custom LLM Conversation

Step 3: Fill Out Fields
- First Field: Enter any random string.
- Second Field: The Local IP address of your Oobabooga Text-Gen-WebUI installation.

Step 4: Adjust Conversation Settings
- Navigate to settings menu and click on Voice Assistants.
- Add or modify a voice assistant.
- Choose Custom LLM Conversation under the Conversation drop down menu.
- Click on the settings cog icon next to the conversation
- Leave Alone/Modify the context parameters. (NOTE: This counts against the token limit, so you may want to remove the part to list all the devices. I was unable to keep this in due to the hundreds of devices on my Home Assistant network)
- Modify additional settings depending on the requirements of each LLM. If you are familiar with LLMs then this should be easy.

# Community Discussion
- This is source of all the information that came together with some additional insight on the Discord. I am simply sharing the connection between text-gen-webui and this coverstaion component over openai's api.

Discussion here https://community.home-assistant.io/t/integration-with-localai/575238/13
