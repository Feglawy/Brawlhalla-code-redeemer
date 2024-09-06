

def read_codes(file_path:str) -> list[str]:
    with open(file_path, 'r') as file:
        codes = [line.strip() for line in file if line.strip()]
    return codes

def write_code(file_path:str, code:str) -> None:
    with open(file_path, 'a') as file:
        file.write(code)
