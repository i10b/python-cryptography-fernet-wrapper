# python-cryptography-fernet-wrapper
[Github Repository](https://github.com/KrazyKirby99999/python-cryptography-fernet-wrapper)
# usage
* Importing
    Command Line
        pip install python-cryptography-fernet-wrapper
    Python
        from python-cryptography-fernet-wrapper import wrapper as fernet_wrapper

* Encrypt
    encrypted_data = fernet_wrapper.encrypt(data, key)

* Decrypt
    decrypted_data = fernet_wrapper.decrypt(encrypted_data, key)

* Generate random key
    fernet_wrapper.gen_key()

* Generate key from password
    fernet_wrapper.key_from_pass(password)