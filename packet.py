def parse_packet(payload: bytes) -> dict:
    """Return minimal frame metadata."""
    return {"size": len(payload), "valid": bool(payload)}
