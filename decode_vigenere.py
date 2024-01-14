import time 


def decode_message(message_to_decode, keyword):
   time.sleep(1)
   print("\nDecoding...")

   reference = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

   #create a string to decode the message
   def find_keyword_string(keyword):
         keyword_string = ''
         keyword_index = 0
         for char in message_to_decode:
            if char.isalpha():
               keyword_string += keyword[keyword_index]
               keyword_index = (keyword_index + 1) % len(keyword)   
            else:
               keyword_string += char
         return keyword_string
   
   #find a new index to decode the message
   keyword_message = find_keyword_string(keyword)  
   decoded_message = ''
   for i, char in enumerate(message_to_decode):
      if char.isalpha():
         message_index = reference.index(char)
         keyword_message_index = reference.index(keyword_message[i]) 
         result_index = (message_index - keyword_message_index) % 26
         decoded_message += reference[result_index]
      else:
         decoded_message += char

   print('\n', decoded_message)
   repeat()


def repeat():
    time.sleep(1)
    print('\nWould you like to decode another message?\nEnter yes or no: ', end="")
    answer = input().lower()
    valid_answers = ['yes', 'y']
    if answer in valid_answers:
        decoding()
    else:
        print('\nEnd of session.')


def get_message():

    print('\nPlease enter message to decode: ', end='')
    message_to_decode = input().lower()

    return message_to_decode


def get_keyword():

    print('\nPlease enter keyword for decoding: ', end='')
    keyword = input().lower()

    return keyword


def decoding():
    message_to_decode = get_message()
    keyword = get_keyword()
    decode_message(message_to_decode, keyword)


def main():
    print("\nHello!")
    decoding()  

if __name__ == "__main__":
  while True:
    main()

    break
