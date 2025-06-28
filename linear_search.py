def linear_search(text_data, target):
    results = []
    lines = text_data.split('\n')
    
    for line_num, line in enumerate(lines, 1):
        if target.lower() in line.lower():  # Case-insensitive search
            results.append({
                'line_number': line_num,
                'content': line.strip(),
                'position': line.lower().find(target.lower())
            })
    
    return results

def read_data_file(filename='data.txt'):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return ""

