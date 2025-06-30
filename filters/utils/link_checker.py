# filters/utils/link_checker.py

import re

# 🌐 Detect if a message contains a link
def contains_link(text: str) -> bool:
    regex = r"(https?://|www\.)\S+"
    return bool(re.search(regex, text))

