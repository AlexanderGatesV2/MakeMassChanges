import os

def delete_files_with_text(root_dir, text):
    deleted_count = 0

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if text in file:
                file_path = os.path.join(root, file)
                os.remove(file_path)
                deleted_count += 1

    return deleted_count

# User input for directory and text
root_directory = input("Enter the root directory path: ")
text_to_search = input("Enter the text to search for in file names: ")

total_deleted = delete_files_with_text(root_directory, text_to_search)
print(f"Total files deleted: {total_deleted}")
