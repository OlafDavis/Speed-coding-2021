from file_handling import *

if __name__ == '__main__':
    print("json:")
    data = read_json('files/test_data.json')
    for i in data['emp_details']:
        print(i)

    print("text:")
    text = read_text('files/test_data.json')
    print(text)

    print("lines:")
    lines = read_lines('files/test_data.json')
    print(lines)
