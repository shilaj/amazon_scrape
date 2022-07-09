def dict_method(request_headers):
    request_headers_list = request_headers.strip().split("\n")
    dictionary = {}
    for lis in request_headers_list:
        temp = lis.strip().split(": ")
        dictionary[temp[0]] = temp[1]

    return dictionary