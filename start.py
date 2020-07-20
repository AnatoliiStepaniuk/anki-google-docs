from __future__ import print_function

from gdocs import gdocs
from gdocs import document_id
from anki import add_note
from anki import html_link

def main():

    with open('urls.txt') as f:
        for url in f.readlines():
            document = gdocs().get(documentId=document_id(url)).execute()
            add_note(document.get('title'), html_link(url))

if __name__ == '__main__':
    main()