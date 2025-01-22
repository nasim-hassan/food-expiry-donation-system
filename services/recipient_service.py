from models.recipients import add_recipient, get_all_recipients

def add_new_recipient(name, contact_info, address):
    add_recipient(name, contact_info, address)

def list_recipients():
    return get_all_recipients()
