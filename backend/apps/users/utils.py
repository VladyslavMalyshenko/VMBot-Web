def get_encoded_url(url: str):
    encoded_url = url.replace(
        ':', '%3A'
    ).replace('/', '%2F')
    return encoded_url
