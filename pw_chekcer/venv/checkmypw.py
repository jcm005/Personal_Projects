import requests
import hashlib
import sys


def requests_api_data(query_char):

    url = 'https://api.pwnedpasswords.com/range/' + query_char  # enter the has version of the passworf but onmly the first five in the hash password to keep secreecy
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error Feching: {res.status_code}, check the api and try again')
    return res


def pwned_api_check(password):

   sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
   first_char, tail = sha1password[:5], sha1password[5:]
   #print(first_char,tail)
   response = requests_api_data(first_char)
   #print(response)
   return get_password_leak_count(response,tail)


def read_response(response):
    print(response.text)

def get_password_leak_count(hashes,hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0
        #print(h,count)

    print(hashes)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... you should probably change your password')
        else:
            print(f'You are all good!  {password} was not found')
        return 'done'

main(sys.argv[1:])

