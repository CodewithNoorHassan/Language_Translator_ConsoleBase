from agents import Agent,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,RunConfig
from dotenv import load_dotenv
import os
import asyncio



load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI API KEY is not set make sure it is defined in your .env file")

# -----------GEMINI API CLIENT SETUP-------------
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


# -----------MODEL SETUP-------------

model= OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)


# -----------RUN CONFIGURATION-------------

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)


# -----------MAIN FUNCTION-------------

async def main():
    print("Tranlstaor Agent"),
    source_lang = input("Enter the source language you want to translate: ")
    target_lang = input("Enter the target language you want: ")
    text = input(f"Enter the text you want to convert from {source_lang} to {target_lang}: ")



    # -----------CREATING AGENT-------------

    agent = Agent(
        name="Translator AI Agent",
        instructions="You are a transltor agent your task is to translate user source language to target language. if unclear, ask for clarification",

    )


    # -----------RUNNING TRANSLATION-------------

    response = await Runner.run(
        agent,
        input=f"Translate this from {source_lang} to {target_lang}: {text}",
        run_config=config
    )

    print("\n ---------------Translation Result--------------")
    print(response)


if __name__== "__main__":
    asyncio.run(main())