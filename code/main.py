

# Then import DES3 for Encryption and md5 for key
from Crypto.Cipher import DES3
from hashlib import md5

# For selecting operation from given choice
while True:
    print('Choose operation to be done:\n\t1- Encryption\n\t2- Decryption')
    operation = input('Enter Your Choice: ')
    if operation not in ['1', '2']:
        break

    # Image / File Path for operation
    file_path = input('Enter File path of image: ')

    # Key for performing Triple DES algorithm
    key = input('Enter your Triple DES key: ')

    # Encode given key to 16 byte ascii key with md5 operation
    key_hash = md5(key.encode('ascii')).digest()


    tdes_key = DES3.adjust_key_parity(key_hash)


    cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')

    # Open & read file from given path
    with open(file_path, 'rb') as input_file:

        file_bytes = input_file.read()

        if operation == '1':
            # Perform Encryption operation
            new_file_bytes = cipher.encrypt(file_bytes)
        else:
            # Perform Decryption operation
            new_file_bytes = cipher.decrypt(file_bytes)

    # Write updated values in file from given path
    with open(file_path, 'wb') as output_file:
        output_file.write(new_file_bytes)
        print('Operation Done!')
        break