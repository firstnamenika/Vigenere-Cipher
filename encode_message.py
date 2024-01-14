import time 

def encode_message(message_to_encode, keyword):
    print('\nEncoding...')
    time.sleep(1)

    reference = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #create an encoding string using keyword

    keyword_string = ''
    keyword_index = 0
    for char in message_to_encode:
        if char.isalpha():
            keyword_string += keyword[keyword_index]
            keyword_index = (keyword_index + 1)%len(keyword)
        else:
            keyword_string += char
    
    # #iterate through message// shift message letter by keyword letter
    encoded_message = ''
    for i, char in enumerate(message_to_encode):
        if char.isalpha():
            char_index = reference.index(char)
            keyword_string_index = reference.index(keyword_string[i])
            encoded_message_index = (char_index - keyword_string_index) % 26
            encoded_message += reference[encoded_message_index]
        else:
            encoded_message += char
    
    
    print('\n', encoded_message)
    repeat()


def repeat():
    time.sleep(1)
    print('\nWould you like to encode another message?\nEnter yes or no: ', end="")
    answer = input().lower()
    valid_answers = ['yes', 'y']
    if answer in valid_answers:
        encoding()
    else:
        print('\nEnd of session.')


def get_message():

    print('\nPlease enter message to encode: ', end='')
    message_to_encode = input().lower()

    return message_to_encode


def get_keyword():

    print('\nPlease enter keyword for encoding: ', end='')
    keyword = input().lower()

    return keyword


def encoding():
    message_to_encode = get_message()
    keyword = get_keyword()
    encode_message(message_to_encode, keyword)


def main():
    print("\nHello!")
    encoding()
    



if __name__ == "__main__":
  while True:
    main()

    break
    