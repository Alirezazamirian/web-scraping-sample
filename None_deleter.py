
def main():
    file_path = 'product_data2.txt'

    none_deleter(file_path)

    with open(file_path, 'r') as file:
        lines = file.readlines()
    non_empty_lines = [line for line in lines if line.strip()]
    with open(file_path, 'w') as file:
        file.writelines(non_empty_lines)

    print('Task was done!')


if __name__ == '__main__':
    main()

def none_deleter(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    print('file was read successfully.')
    modified_content = content.replace('None', '')
    with open(file_path, 'w') as file:
        file.write(modified_content)
    print("All occurrences of 'None' have been deleted from the file.")