from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from app.core.config import HUGGINGFACE_API_KEY, config_repo_id, config_max_new_tokens, config_temperatures

from app.prompts.answering import answering_prompt

import logging
logger = logging.getLogger(__name__)


endpoint = HuggingFaceEndpoint(
    repo_id=config_repo_id,
    huggingfacehub_api_token=HUGGINGFACE_API_KEY,
    temperature=config_temperatures,
    max_new_tokens=config_max_new_tokens,
)
llm = ChatHuggingFace(llm=endpoint)


prompt = answering_prompt


def generate_answer(question: str, context: str) -> str:
    chain = prompt | llm
    logger.info("Sent the prompt to LLM")

    response = chain.invoke(
    {
        "question": question,
        "context": context,
    }
    )
    logger.info("got the output from llm")

    return response.content