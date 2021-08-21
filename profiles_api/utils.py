import uuid


def generate_id_code():
    """Generates a unique id for the user"""
    return uuid.uuid4().hex
