"""
URL-encode characters—In URLs, we often replace special and nonprintable
characters with a % followed by the character’s ASCII value in hexadecimal. For
example, if a URL is to include a space character (ASCII 32, aka 0x20), we
replace it with %20. Given a string, URL-encode any character that isn’t a letter
or number. For the purposes of this exercise, we’ll assume that all characters
are indeed in ASCII (i.e., one byte long), and not multibyte UTF-8 characters. It
might help to know about the ord (http://mng.bz/EdnJ) and hex (http://mng
.bz/nPxg) functions. 
"""


def url_encode_characters(url):
    encoded_url = ""
    for letra in url:
        if letra.isalnum():
            encoded_url += letra
        else:
            encoded_url += f'%{ord(letra):02X}'
    return encoded_url


print(url_encode_characters("www.protp.com"))
