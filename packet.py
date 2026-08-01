def parse_packet(payload: bytes) -> dict:
    return {'size': len(payload), 'valid': bool(payload)}
