from langchain_ollama import ChatOllama

from tools import (
    search_client_info,
    retrieve_meeting_notes,
    retrieve_memory
)

from memory import (
    add_to_history,
    get_chat_history
)


# --------------------------------
# LOCAL LLM
# --------------------------------

llm = ChatOllama(
    model="llama3"
)


# --------------------------------
# AGENT REASONING
# --------------------------------

def identify_client(user_query):

    if "acme" in user_query.lower():
        return "Acme Corp"

    return None


# --------------------------------
# AGENT WORKFLOW
# --------------------------------

def prepare_meeting_brief(client_name):

    print("\n[Agent] Searching Client Info...")

    client_info = search_client_info(
        client_name
    )

    print("[Agent] Retrieving Meeting Notes...")

    meeting_notes = retrieve_meeting_notes(
        client_name
    )

    print("[Agent] Retrieving Long-Term Memory...")

    memory = retrieve_memory(
        client_name
    )

    prompt = f"""
You are an AI Meeting Preparation Assistant.

Client Information:
{client_info}

Meeting Notes:
{meeting_notes}

Long-Term Memory:
{memory}

Generate a concise meeting brief.

Include:

1. Client Overview
2. Previous Discussions
3. Open Concerns
4. Action Items
5. Recommended Talking Points
"""

    response = llm.invoke(
        prompt
    )

    return response.content


# --------------------------------
# FOLLOW UP QUESTIONS
# --------------------------------

def answer_followup(question):

    history = get_chat_history()

    history_text = ""

    for msg in history[-6:]:

        history_text += (
            f"{msg['role']}: "
            f"{msg['content']}\n"
        )

    prompt = f"""
Conversation History:

{history_text}

User Question:
{question}

Answer using the conversation context.
"""

    response = llm.invoke(
        prompt
    )

    return response.content


# --------------------------------
# MAIN LOOP
# --------------------------------

print("\n========================")
print("Meeting Preparation Agent")
print("========================\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    add_to_history(
        "user",
        user_input
    )

    if (
        "prepare me" in user_input.lower()
        and "meeting" in user_input.lower()
    ):

        client = identify_client(
            user_input
        )

        if client:

            response = prepare_meeting_brief(
                client
            )

        else:

            response = (
                "Client not found."
            )

    else:

        response = answer_followup(
            user_input
        )

    print("\nAssistant:\n")
    print(response)

    add_to_history(
        "assistant",
        response
    )

    print(
        "\n-------------------------\n"
    )