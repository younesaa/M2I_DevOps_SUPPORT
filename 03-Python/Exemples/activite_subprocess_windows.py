import subprocess

def create_file(filename):
    try:
        subprocess.run(f'type nul > {filename}', shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"Failed to create {filename}")

def list_files():
    try:
        result = subprocess.run('dir /B', capture_output=True, text=True, shell=True, check=True)
        return result.stdout.strip().split('\n')
    except subprocess.CalledProcessError:
        print("Failed to list files")
        return []

def delete_file(filename):
    try:
        subprocess.run(f'del {filename}', shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"Failed to delete {filename}")

def append_to_file(filename, text):
    try:
        with open(filename, 'a') as file:
            file.write(text + '\n')
    except IOError:
        print(f"Failed to append to {filename}")

if __name__ == "__main__":
    create_file('testfile.txt')
    files = list_files()
    print("Files in the current directory:", files)
    append_to_file('testfile.txt', 'Hello, world!')
    print('\n')
    try:
        with open('testfile.txt', 'r') as file:
            print("Contents of the file:", file.read())
    except IOError:
        print("Failed to read 'testfile.txt'")

    delete_file('testfile.txt')
    files = list_files() 
    print("Files in the current directory after deletion:", files)
