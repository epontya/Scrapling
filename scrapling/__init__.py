"""Scrapling - A powerful, flexible web scraping library.

Scrapling is a high-performance web scraping library that provides
automatic browser fingerprinting, smart element detection, and
robust parsing capabilities.

Personal fork notes:
- Forked for learning/personal use
- Added StealthyFetcher to top-level exports for easier access
- Added AsyncStealthyFetcher to top-level exports as well
- Grouped availability flags into a single dict for cleaner checks
- Added helper function `get_available_backends()` for easy inspection
- See https://github.com/D4Vinci/Scrapling for the upstream project
"""

from scrapling.core.fetchers import Fetcher, AsyncFetcher
from scrapling.core.page import Adaptor
from scrapling.core.custom_types import SelectorList

__version__ = "0.2.9"
__author__ = "D4Vinci"
__license__ = "MIT"

# Track which optional fetcher backends are available
_available_backends = {}

# Expose PlaywrightFetcher and AsyncPlaywrightFetcher at the top level for convenience
try:
    from scrapling.core.fetchers import PlaywrightFetcher, AsyncPlaywrightFetcher
    _available_backends["playwright"] = True
except ImportError:
    _available_backends["playwright"] = False

# Also expose StealthyFetcher and AsyncStealthyFetcher at the top level -- I use these most often
try:
    from scrapling.core.fetchers import StealthyFetcher, AsyncStealthyFetcher
    _available_backends["stealthy"] = True
except ImportError:
    _available_backends["stealthy"] = False


def get_available_backends() -> dict:
    """Return a copy of the available backends dict.

    Useful for quickly checking which optional dependencies are installed
    without having to catch ImportErrors yourself.

    Example::

        import scrapling
        print(scrapling.get_available_backends())
        # {'playwright': True, 'stealthy': False}
    """
    return dict(_available_backends)


__all__ = [
    "Fetcher",
    "AsyncFetcher",
    "Adaptor",
    "SelectorList",
    "get_available_backends",
]

if _available_backends.get("playwright"):
    __all__ += ["PlaywrightFetcher", "AsyncPlaywrightFetcher"]

if _available_backends.get("stealthy"):
    __all__ += ["StealthyFetcher", "AsyncStealthyFetcher"]
