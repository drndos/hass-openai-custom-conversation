"""Constants for the OpenAI Conversation integration."""

import logging

DOMAIN = "custom_openai_conversation"
LOGGER = logging.getLogger(__package__)

CONF_RECOMMENDED = "recommended"
CONF_PROMPT = "prompt"
CONF_CHAT_MODEL = "chat_model"
RECOMMENDED_CHAT_MODEL = "gpt-4o"
CONF_MAX_TOKENS = "max_tokens"
RECOMMENDED_MAX_TOKENS = 150
CONF_TOP_P = "top_p"
RECOMMENDED_TOP_P = 1.0
CONF_TEMPERATURE = "temperature"
RECOMMENDED_TEMPERATURE = 1.0
CONF_BASE_URL = "base_url"
DEFAULT_BASE_URL = "https://api.openai.com/v1"
DEFAULT_API_KEY = "sk-0000000000000000000"
