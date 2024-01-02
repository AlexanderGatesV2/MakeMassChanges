# RenameIt.py

**Purpose:** This script is created to rename a bunch of files from a previous backup. These files all had the same UTC date appended to the end of their names.

**Functionality:**
- Asks for the directory to search in (applies changes recursively).
- Prompts for the text you want to rename.
- Requests the new text to replace the old text.

**Features:**
- If a file with the new name already exists, `_` followed by a number is appended to the new file name.
  - For example, `File001.bin` will become `File001_1.bin` while the original `File001.bin` remains unchanged.

---

# DeleteIt.py

**Usage:**
1. **Choose a Directory**: The script searches the directory recursively.
2. **Text-Based Deletion**: Deletes files based on the file name text entered by the user.

---

# ChangeIt.py

**Overview:**
- A two-in-one tool that combines the functionalities of `RenameIt.py` and `DeleteIt.py`.
- Allows users to choose between renaming and deleting files in a specified directory.
