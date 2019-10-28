import numpy as np
key = np.array([
    [3, 10, 20],
    [20, 9, 17],
    [9, 4, 17]
])

key_rows = key.shape[0]
key_columns = key.shape[1]

if key_rows != key_columns:
   raise Exception('key must be square matrix!')
def letterToNumber(letter):
   return string.ascii_lowercase.index(letter)

raw_message = "attack is to night"
print("raw message: ",raw_message)

message = []

for i in range(0, len(raw_message)):
   current_letter = raw_message[i:i+1].lower()
   if current_letter != ' ': #discard blank characters
      letter_index = letterToNumber(current_letter)
      message.append(letter_index)
if len(message) % key_rows != 0:
   for i in range(0, len(message)):
      message.append(message[i])
      if len(message) % key_rows == 0:
         break
message = np.array(message)
message_length = message.shape[0]
message.resize(int(message_length/key_rows), key_rows)
encryption = np.matmul(message, key)
encryption = np.remainder(encryption, 26)
