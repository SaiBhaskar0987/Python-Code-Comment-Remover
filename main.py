import sys

def remove_comments(input_path, output_path):
    # Read the input file
    with open(input_path, 'r') as f:
        data = f.read()

    # Remove single-line comments
    l = data.split("\n")
    list = []
    for i in l:
        if '#' not in i:
            list.append(i)
        else:
            if '"' in i:
                b = i.split('"')
                if "#" not in b[-1]:
                    list.append(i)
                elif "#" in b[-1]:
                    c = i.split("#")
                    c.pop()
                    d = '#'.join(c)
                    list.append(d)
            else:
                a = i.split("#")
                list.append(a[0])

    # Write the intermediate result to a temporary file
    with open(output_path, 'w') as g:
        g.write('\n'.join(list))

    # Remove multi-line comments (''' and """)
    with open(output_path, 'r') as atta:
        data1 = atta.read()

    parts = data1.split("'''")
    filtered_parts = parts[0::2]
    cleaned_data = ''.join(filtered_parts)

    with open(output_path, 'w') as wheat:
        wheat.write(cleaned_data)

    with open(output_path, 'r') as sugar:
        data2 = sugar.read()

    parts1 = data2.split('"""')
    filtered_parts1 = parts1[0::2]
    cleaned_data1 = ''.join(filtered_parts1)

    with open(output_path, 'w') as rice:
        rice.write(cleaned_data1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    remove_comments(input_file, output_file)