"""Shared utilities for all agent files."""


def content_to_dicts(content) -> list:
    """Convert Anthropic SDK response content blocks to serializable dicts."""
    return [{"type": b.type, **b.model_dump(exclude={"type"})} for b in content]
