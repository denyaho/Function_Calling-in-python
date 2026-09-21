def fn_greet(name: str) -> str:
    return f"Hello, {name}-san!"

def fn_reverse_string(s: str) -> str:
    return s[::-1]

def fn_substitute_string_with_regex(source: str, regex: str, replacement: str) -> str:
    import re
    return re.sub(regex, replacement, source)