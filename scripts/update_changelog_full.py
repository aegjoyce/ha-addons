#!/usr/bin/env python

import os
import sys
from datetime import date

from python_keepachangelog.changelog import Changelog, ChangelogEntry

MY_DIRECTORY = os.path.dirname(__file__)
print(MY_DIRECTORY)
CHANGELOG_PATH = os.path.abspath(os.path.join(MY_DIRECTORY, "../scrypted/CHANGELOG.md"))

def main(new_version: str):
    cl = Changelog(source=CHANGELOG_PATH)
    cl.parse_original_content()
    cl.add_entry(ChangelogEntry(new_version, date.today(), {"Changed": [f"Update base image to {new_version}"]}))
    with open(CHANGELOG_PATH, "w") as f:
        f.write(cl.to_string())
    
if __name__ == "__main__":
    new_version = sys.argv[1].lstrip("v")
    main(new_version)
    
