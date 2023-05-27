import os

BOOK_PATH = 'book/book.txt'

PAGE_SIZE = 1050

book: dict[int, int] = {}


def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    res = text[start:start + page_size]
    if res[-1] == '.' and text[len(res) + start - 2] == '.' and len(res) and text[-1] != '.':
        if res[-1] == res[-2]:
            res = res[:len(res) - 2]
        else:
            res = res[:len(res) - 1]
        result = (res, len(res))
    else:
        for i in range(len(res) - 1, -1, -1):
            if (res[i] == '.' and res[i - 1] == '?') or (res[i] == '?' and res[i + 1] == '.'):
                continue
            elif res[i] in ['.', ',', ':', ';', '!', '?']:
                b = i
                break

        res = res[:b + 1]

        result = (res, len(res))
    return result


def prepare_book(path: str) -> None:
    with open(path) as f:
        book_read = f.read()
    i = 1
    start_run = 0
    while start_run < len(book_read):
        tuple_text = _get_part_text(book_read, start_run, PAGE_SIZE)
        book[i] = tuple_text[0].strip()
        i += 1
        start_run += tuple_text[1] + 1


prepare_book(os.path.join(os.getcwd(), BOOK_PATH))
