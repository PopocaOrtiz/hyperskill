def create_text(text: str):
    return text


def create_bold(text: str) -> str:
    return f'**{text}**'


def create_italic(text: str) -> str:
    return f'*{text}*'


def create_link(label: str, url: str) -> str:
    return f'[{label}]({url})'


def create_inline_code(text: str) -> str:
    return f'`{text}`'


def create_header(level: int, text: str):
    return f"{'#'*level} {text}\n"


def create_new_line() -> str:
    return '\n'


def create_list(ordered: bool, number_of_rows: int):
    texts = []
    for i in range(number_of_rows):
        text = input(f"row #{i + 1}:")
        character = f'{i + 1}. ' if ordered else '* '
        texts.append(character + text)

    return '\n'.join(texts) + '\n'


def main():
    final_text = ''
    while True:

        command = input('Choose a formatter:')

        if command == '!help':
            print('Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line')
            print('Special commands: !help !done')
            continue

        if command == '!done':
            quit()
        elif command == 'header':

            while True:

                level = int(input('Level'))
                if 1 < level < 6:
                    break

                print('The level should be within the range of 1 to 6')

            text = input('Text:')
            final_text += create_header(level, text)
        elif command == 'plain':
            text = input('Text:')
            final_text += create_text(text)
        elif command == 'bold':
            text = input('Text:')
            final_text += create_bold(text)
        elif command == 'italic':
            text = input('Text:')
            final_text += create_italic(text)
        elif command == 'link':
            label = input('Label:')
            url = input('URL:')
            final_text += create_link(label, url)
        elif command == 'inline-code':
            text = input('Text:')
            final_text += create_inline_code(text)
        elif command == 'new-line':
            final_text += create_new_line()
        elif command == 'ordered-list' or command == 'unordered-list':

            while True:

                number_of_rows = int(input('Number of rows:'))

                if number_of_rows > 0:
                    break

                print('The number of rows should be greater than zero')

            ordered = command == 'ordered-list'

            final_text += create_list(ordered, number_of_rows)

        else:
            print('Unknown formatting type or command')

        print(final_text)


if __name__ == '__main__':
    main()
