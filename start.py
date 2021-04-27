from __future__ import print_function

from gdocs import gdocs
from gdocs import document_id
from anki import add_note
from anki import embed_url

def main():

    with open('urls.txt') as f:
        for url in f.readlines():
            document = gdocs().get(documentId=document_id(url)).execute()
            add_note(document.get('title'), embed_url(url))
            print('Added ' + document.get('title'))

if __name__ == '__main__':
    main()