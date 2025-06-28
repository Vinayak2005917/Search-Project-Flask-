def build_shift_table(pattern):
    m = len(pattern)
    table = {char: m for char in set(pattern)}
    for i in range(m - 1):
        table[pattern[i]] = m - 1 - i
    return table

def horspool_search(text_data, target):
    results = []
    pattern = target.lower()
    shift_table = build_shift_table(pattern)
    lines = text_data.split('\n')

    for line_num, line in enumerate(lines, 1):
        text = line.lower()
        n = len(text)
        m = len(pattern)
        i = m - 1

        while i < n:
            k = 0
            while k < m and pattern[m - 1 - k] == text[i - k]:
                k += 1
            if k == m:
                results.append({
                    'line_number': line_num,
                    'content': line.strip(),
                    'position': i - m + 1
                })
                break  # Only first match per line
            else:
                i += shift_table.get(text[i], m)
    
    return results
def read_data_file(filename='data.txt'):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return ""