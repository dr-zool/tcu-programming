def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            print(f"Opening file: {file_path}")
            content = file.read()
            if not content:
                raise ValueError("File is empty")
            lines = content.splitlines()
            print("File content processed successfully.")
            return lines
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Finished processing the file.")
