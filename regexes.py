import re

re.finditer(r"(?m)^\s+(?!noreply|postmaster)(\w+)",
"""
    sales@bla.com
    postmaster@gmail.com
    eng@bla.com
    noreply@peng.com
    admn@giga.com
""")
