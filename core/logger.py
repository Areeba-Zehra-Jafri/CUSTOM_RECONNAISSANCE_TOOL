# core/logger.py

VERBOSE = False

def set_verbose(value: bool):
    global VERBOSE
    VERBOSE = value

def info(message: str):
    print(f"[+] {message}")

def warning(message: str):
    print(f"[!] {message}")

def debug(message: str):
    if VERBOSE:
        print(f"[DEBUG] {message}")
