
def file_stream(path:str):
    with open(path, 'r') as f:
        for line in f:
            yield line