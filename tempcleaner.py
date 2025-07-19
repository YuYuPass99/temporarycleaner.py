import os
import shutil
import tempfile

def clean_temp_dir():
    temp_dir = tempfile.gettempdir()
    print(f"Cleaning temporary directory: {temp_dir}")

    delete = 0
    error = 0

    for i in os.listdir(temp_dir):
        path = os.path.join(temp_dir, i)

        try:
            if os.path.isfile(path) | os.path.islink(path):
                os.remove(path)
                print(f"Deleted: {path}")
                delete += 1
            elif os.path.isdir(path):
                shutil.rmtree(path)
                print(f"Deleted directory: {path}")
                delete += 1
        except Exception:
            print(f"Error deleting {path}: {Exception}")
            error += 1

    print(f"\nDeleted objects: {delete}")
    if error:
        print(f"Errors: {error}")
    else:
        print("No errors.")

if __name__ == "__main__":
    clean_temp_dir()