from langchain_community.chat_models.gigachat import GigaChat
from langchain.schema import HumanMessage, SystemMessage
from hack_med.config import settings

import json

chat = GigaChat(credentials=settings.AUTORIZATION_KEY,
                verify_ssl_certs=False)

