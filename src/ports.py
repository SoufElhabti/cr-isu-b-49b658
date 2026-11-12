"""Public port parser."""


def parse_port(value: str) -> int:
    """Parse a numeric port string."""
    port = int(value)
    if not 0 < port < 65536:
        raise ValueError("port out of range")
    return port
