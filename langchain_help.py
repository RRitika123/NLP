from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openapi_key

import os

os.environ['OPENAI_API_KEY'] = openapi_key
llm = OpenAI(temperature = 0.7)


def generate_channel_name_and_topics(niche):
    # Chain 1: channel Name
    prompt_template_name = PromptTemplate(
        input_variables = ['niche'], 
        template = "I want to open a new youtube on {niche}. Can you suggest me one name for my channel"
    )

    name_chain = LLMChain(llm=llm, prompt = prompt_template_name, output_key="channel_name")

    # Chain2: Trending topics
    prompt_template_items = PromptTemplate(
        input_variables = ['channel_name'],
        template = "Suggest some trending topices for {channel_name}. Return it as comma separated list"
    )

    topics_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="topics")

    chain = SequentialChain(
        chains = [name_chain, topics_chain],
        input_variables = ["niche"],
        output_variables = ["channel_name","topics"]
    )

    response = chain({'niche': niche})
    return response

if __name__ == "__main__":
    print(generate_channel_name_and_topics("Cooking"))
