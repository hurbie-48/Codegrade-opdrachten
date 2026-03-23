import re

pattern = r"^[A-Z]{2}-\d{2}-\d{2}$"


if (re.match(pattern, "TT-33-33")) == None:
    print("Not a match")
else:
    print("Match")