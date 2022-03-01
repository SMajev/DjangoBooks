import requests

def get_field(*args):
    try:
        if len(args) == 2:
            field = args[0][args[1]]

        elif len(args) == 3:
            field = args[0][args[1]][args[2]]

        elif len(args) == 4:
            field = args[0][args[1]][args[2]][args[3]]

    except:
        field = None

    return field

class GoogleAPI:
    
    @staticmethod
    def get_book(phrase):
        url = f'https://www.googleapis.com/books/v1/volumes?q={phrase}'
        try:
            result = requests.get(url).json()['items'][0]['volumeInfo']
        except:
            result = None

        if result != None:
            title = get_field(result, 'title')
            author = get_field(result, 'authors') 
            published = get_field(result, 'publishedDate')
            isbn = get_field(result, 'industryIdentifiers', 0, 'identifier')
            print_length = get_field(result, 'pageCount')
            cover = get_field(result, 'imageLinks', 'thumbnail')
            language = get_field(result, 'language')

            book = {
                'title': title,
                'author': author,
                'published': published,
                'isbn': isbn,
                'print_length': print_length,
                'cover': cover,
                'language': language
            }

        else:
            book = 'Not found!'

        return book

 

