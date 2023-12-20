from typing import List, Dict, Any, Optional, Tuple
import re
import logging

import voluptuous as vol
import homeassistant.components.conversation
from homeassistant.components import conversation
from homeassistant.core import Context
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers import intent

from .const import (
    ATTR_RESPONSE_PARSER_START,
    ATTR_RESPONSE_PARSER_END,
    ATTR_FIRE_INTENT_NAME,
    DEFAULT_PARSER_TOKEN,
    DEFAULT_INTENT_NAME,
    DOMAIN
)

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Required(ATTR_RESPONSE_PARSER_START, default=DEFAULT_PARSER_TOKEN): cv.string,
        vol.Required(ATTR_RESPONSE_PARSER_END, default=DEFAULT_PARSER_TOKEN): cv.string,
        vol.Required(ATTR_FIRE_INTENT_NAME, default=DEFAULT_INTENT_NAME): cv.slugify
    })
}, extra=vol.ALLOW_EXTRA)

async def async_setup(hass, config):
    """Set up the openai_override component."""

    from custom_components.custom_llm_conversation import OpenAIAgent

    original = OpenAIAgent.async_process

    async def async_process(self, user_input: conversation.ConversationInput) -> conversation.ConversationResult:
        """Handle OpenAI intent."""
        result = await original(self, user_input)
        _LOGGER.info("Error code: {}".format(result.response.error_code))
        if result.response.error_code is not None:
            return result

        import json
        _LOGGER.info(json.dumps(result.response.speech))

        content = ""
        segments = result.response.speech["plain"]["speech"].splitlines()
        for segment in segments:
            _LOGGER.info("Segment: {}".format(segment))
            if segment.startswith("{"):
                service_call = json.loads(segment)
                service = service_call.pop("service")
                if not service or not service_call:
                    _LOGGER.info('Missing information')
                    continue
                await hass.services.async_call(
                        service.split(".")[0],
                        service.split(".")[1],
                        service_call,
                        blocking=True)
            else:
                content = "{} {}".format(content, segment)

        intent_response = intent.IntentResponse(language=user_input.language)
        intent_response.async_set_speech(content)
        return conversation.ConversationResult(
            response=intent_response, conversation_id=result.conversation_id
        )


    OpenAIAgent.async_process = async_process

    return True
