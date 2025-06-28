def build_bad_char_table(pattern):
    table = {}
    for i in range(len(pattern)):
        table[pattern[i]] = i
    return table

def boyer_moore_search(text_data, target):
    results = []
    pattern = target.lower()
    lines = text_data.split('\n')
    m = len(pattern)

    for line_num, line in enumerate(lines, 1):
        text = line.lower()
        n = len(text)
        bad_char = build_bad_char_table(pattern)
        s = 0

        while s <= n - m:
            j = m - 1
            while j >= 0 and pattern[j] == text[s + j]:
                j -= 1
            if j < 0:
                results.append({
                    'line_number': line_num,
                    'content': line.strip(),
                    'position': s
                })
                s += m if s + m < n else 1
                break  # Only first match per line
            else:
                shift = max(1, j - bad_char.get(text[s + j], -1))
                s += shift

    return results
def read_data_file(filename='data.txt'):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return ""