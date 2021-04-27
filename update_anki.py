from anki import update_note
from anki import find_notes
from anki import notes_info
from anki import embed_url


def main():
    for id in find_notes():
        note = notes_info(id)[0]
        front = note['fields']['Front']['value']
        back = note['fields']['Back']['value']
        update_note(id, front, new_value(back))


def new_value(value):
    return value if value.find("<a href=") == -1 else transform_value(value)


def transform_value(value):
    first = value.find('<a href="')+len('<a href="')
    last = value.find('"', first)
    url = value[first:last]
    return embed_url(url)


if __name__ == '__main__':
    main()