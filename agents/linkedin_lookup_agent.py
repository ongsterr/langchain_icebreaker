from tools.tools import get_profile_url_tavily

from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub  # to download premade prompts
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
import os

load_dotenv()


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """
    given the full name {name_of_person}, I want you to get me a link to their Linkedin profile page. your answer should contain only a url.
    """

    prompt_template = PromptTemplate(template=template, input_variables=["name_of_person"])
    tools_for_agent = [
        Tool(
            name="Crawl Google for Linkedin profile page",
            func=get_profile_url_tavily,
            description="useful for when you need to get the Linkedin page url",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")  # chain of thought
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(input={"input": prompt_template.format_prompt(name_of_person=name)})
    linkedin_profile_url = result["output"]
    return linkedin_profile_url


if __name__ == "__main__":
    linkedin_url = lookup(name="Eden Marco")
    print(linkedin_url)
