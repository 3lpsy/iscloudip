
def confirm(question, default="NOT_SET"):
    question = question + " "
    if default != 'NOT_SET':
        question = "{} [{}]".format(question, default)
    response = input(question)
    if not response:
        if default != 'NOT_SET':
            return default
        return confirm(question, default)
    elif response.lower() == 'yes' or response.lower() == 'y':
        return True
    elif response.lower() == 'no' or response.lower() == 'n':
        return False
    else:
        return confirm(question, default)
