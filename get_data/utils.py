import os


def save(response, folder):
    filename = os.path.basename(response.url)
    filepath = os.path.join(folder, filename)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    if 'text' in response.headers.get('content-type'):
        with open(filepath, 'w') as file:
            file.write(response.content)
    else:
        with open(filepath, 'wb') as file:
            file.write(response.content)
