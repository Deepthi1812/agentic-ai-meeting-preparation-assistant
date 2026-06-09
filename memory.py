import json


# -----------------------------
# SHORT TERM MEMORY
# -----------------------------

chat_history = []


def add_to_history(role, content):

    chat_history.append(
        {
            "role": role,
            "content": content
        }
    )


def get_chat_history():

    return chat_history


# -----------------------------
# LONG TERM MEMORY
# -----------------------------

MEMORY_FILE = "memory/long_term_memory.json"


def get_client_memory(client_name):

    with open(
        MEMORY_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        memory = json.load(f)

    return memory.get(
        client_name,
        {}
    )
