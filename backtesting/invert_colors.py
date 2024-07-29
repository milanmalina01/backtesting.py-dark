def invert_background(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Find the end of the <style> tag in the head section
    insert_pos = content.find('</style>')

    if insert_pos == -1:
        # If there's no <style> tag, insert one after the <head> tag
        insert_pos = content.find('</head>')
        if insert_pos != -1:
            insert_pos += len('</head>')
            style_content = '<style>html, body { background-color: black; color: white; }</style>'
        else:
            # If there's no <head> tag, we can't properly insert the style, so just append it at the end
            style_content = '<style>html, body { background-color: black; color: white; }</style>'
            content += style_content
            insert_pos = content.find('</style>') + len('</style>')
    else:
        # Insert the background and text color styles within the existing style tag
        style_content = 'html, body { background-color: black; color: white; }'

    # Insert the style content at the found position
    modified_content = content[:insert_pos] + style_content + content[insert_pos:]

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(modified_content)

if __name__ == '__main__':
    # Example usage
    input_file_path = 'result.html'
    output_file_path = 'result_inv.html'
    invert_background(input_file_path, output_file_path)