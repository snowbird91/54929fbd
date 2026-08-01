DEBUG = True

def parse_packet(payload: bytes) -> dict:
    """Return minimal frame metadata."""
    if DEBUG:
        print(f'packet bytes={len(payload)}')
    return {'size': len(payload), 'valid': bool(payload)}
