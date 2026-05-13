"""Scrapling - A powerful, flexible web scraping library.

Scrapling is a high-performance web scraping library that provides
automatic browser fingerprinting, smart element detection, and
robust parsing capabilities.

Personal fork notes:
- Forked for learning/personal use
- Added StealthyFetcher to top-level exports for easier access
- See https://github.com/D4Vinci/Scrapling for the upstream project
"""

from scrapling.core.fetchers import Fetcher, AsyncFetcher
from scrapling.core.page import Adaptor
from scrapling.core.custom_types import SelectorList

__version__ = "0.2.9"
__author__ = "D4Vinci"
__license__ = "MIT"

# Expose PlaywrightFetcher and AsyncPlaywrightFetcher at the top level for convenience
try:
    from scrapling.core.fetchers import PlaywrightFetcher, AsyncPlaywrightFetcher
    _playwright_available = True
except ImportError:
    _playwright_available = False

# Also expose StealthyFetcher at the top level -- I use this one most often
try:
    from scrapling.core.fetchers import StealthyFetcher
    _stealthy_available = True
except ImportError:
    _stealthy_available = False

__all__ = [
    "Fetcher",
    "AsyncFetcher",
    "Adaptor",
    "SelectorList",
]

if _playwright_available:
    __all__ += ["PlaywrightFetcher", "AsyncPlaywrightFetcher"]

if _stealthy_available:
    __all__ += ["StealthyFetcher"]
