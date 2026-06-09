from vector_store import create_vector_store
from memory import get_client_memory


# Create FAISS once
vector_db = create_vector_store()


# ----------------------------------
# TOOL 1
# CLIENT INFO SEARCH
# ----------------------------------

def search_client_info(client_name):

    results = vector_db.similarity_search(
        f"{client_name} client profile",
        k=2
    )

    return "\n".join(
        [doc.page_content for doc in results]
    )


# ----------------------------------
# TOOL 2
# MEETING NOTES SEARCH
# ----------------------------------

def retrieve_meeting_notes(client_name):

    results = vector_db.similarity_search(
        f"{client_name} meeting notes",
        k=2
    )

    return "\n".join(
        [doc.page_content for doc in results]
    )


# ----------------------------------
# TOOL 3
# LONG TERM MEMORY
# ----------------------------------

def retrieve_memory(client_name):

    memory = get_client_memory(
        client_name
    )

    return str(memory)