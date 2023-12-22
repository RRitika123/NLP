# LangChain Application

Langchain is a framework that allows us to build applications using Large Language Models.
In this project we are using llm called OpenAI using Langchain framework.

A brief description of what this project does:\n 
We have built an application which will help our user to suggest their Youtube channel name given the name of the niche they are interested in. Also it will suggest some trending topics to make content on.

## Installation of modules

Install necessary modules by running following command

```bash
  pip install -r requirements.txt
```
otherwise

```bash
  pip install langchain
  pip install openai
  pip install streamlit
```

## Environment Variables

To run this project, you will need to add your openai_api_key into secret_key.py file.

`openapi_key`

## Concepts used

OpenAI: 
The OpenAI module is used to initialize an instance of the OpenAI language model. This involves passing an API key (openapi_key) to authenticate and access the OpenAI language model for natural language processing tasks.

PromptTemplate:
This module is used for creating templates for prompts that can be used with language models.
The PromptTemplate module allows us to define templates for prompts with placeholders. In the provided code, a prompt template is created which includes the input variable {channel_name}, allowing us to customize the prompt for different channels dynamically.

LLM Chain: 
The LLMChain module is used to create a chain involving a language model. In the provided code, an instance of LLMChain is created with the OpenAI language model. This chain can be part of a larger sequence of operations.

Sequential Chain: 
complex chains that involve multiple inputs, and where there also multiple final outputs.

## Screenshots

![Alt text](image.png)

