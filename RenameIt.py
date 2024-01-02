import os

def rename_files_in_directory(root_dir, old_text, new_text):
    renamed_count = 0

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if old_text in file:
                old_file_path = os.path.join(root, file)
                new_file_name = file.replace(old_text, new_text)
                new_file_path = os.path.join(root, new_file_name)

                # Append a number if a file with the new name already exists
                counter = 1
                while os.path.exists(new_file_path):
                    name_part, extension = os.path.splitext(new_file_name)
                    new_file_path = os.path.join(root, f"{name_part}_{counter}{extension}")
                    counter += 1

                os.rename(old_file_path, new_file_path)
                renamed_count += 1

    return renamed_count

# User input for directory and text
root_directory = input("Enter the root directory path: ")
old_text = input("Enter the text to be replaced: ")
new_text = input("Enter the new text: ")

total_renamed = rename_files_in_directory(root_directory, old_text, new_text)
print(f"Total files renamed: {total_renamed}")

# TestDir Path
# /Users/alexandergates/PycharmProjects/RenameIt/TestDir

