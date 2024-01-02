import os

def rename_files_in_directory(root_dir, old_text, new_text):
    renamed_count = 0
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if old_text in file:
                old_file_path = os.path.join(root, file)
                new_file_name = file.replace(old_text, new_text)
                new_file_path = os.path.join(root, new_file_name)
                counter = 1
                while os.path.exists(new_file_path):
                    name_part, extension = os.path.splitext(new_file_name)
                    new_file_path = os.path.join(root, f"{name_part}_{counter}{extension}")
                    counter += 1
                os.rename(old_file_path, new_file_path)
                renamed_count += 1
    return renamed_count

def delete_files_with_text(root_dir, text):
    deleted_count = 0
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if text in file:
                file_path = os.path.join(root, file)
                os.remove(file_path)
                deleted_count += 1
    return deleted_count

# User prompt to choose the operation
operation = input("Enter 'r' to rename files, or 'd' to delete files: ").strip().lower()

if operation == 'r':
    root_directory = input("Enter the root directory path for renaming: ")
    old_text = input("Enter the text to be replaced in file names: ")
    new_text = input("Enter the new text for file names: ")
    total_renamed = rename_files_in_directory(root_directory, old_text, new_text)
    print(f"Total files renamed: {total_renamed}")

elif operation == 'd':
    root_directory = input("Enter the root directory path for deletion: ")
    text_to_search = input("Enter the text to search for in file names: ")
    total_deleted = delete_files_with_text(root_directory, text_to_search)
    print(f"Total files deleted: {total_deleted}")

else:
    print("Invalid operation selected.")
