import re
import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    text = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)

    text = re.sub(r'<[^>]+>', '', text)

    lines = [line.strip() for line in text.splitlines()]
    cleaned_lines = [line for line in lines if line]

    with codecs.open(result_file, 'w', 'utf-8') as file:
        for line in cleaned_lines:
            file.write(line + '\n')