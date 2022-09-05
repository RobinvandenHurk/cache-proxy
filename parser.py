def get_headers(request: str):
    lines = request.split('\r')[1:]
    headers = {}

    for line in lines:
        if line == '\n':
            break

        split = line.split(":", 1)
        headers[split[0].strip()] = split[1].strip()

    return headers


def get_url(request: str):
    return request.split(" ")[1][1:]


def get_method(request: str):
    return request.split(" ")[0]
