def read_file(filename) -> str:
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f'File {filename} not found')
        exit(84)