import re


regexp = re.compile(r"((\s)(\w)\w*\s\3\w*((\s\3\w*)?)*)", re.IGNORECASE)
