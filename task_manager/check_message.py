from django.contrib.messages import get_messages


def get_message_txt(response):
    messages = list(get_messages(response.wsgi_request))
    return str(messages[0])
