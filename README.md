# python-cryptography-fernet-wrapper
[Github Repository](https://github.com/KrazyKirby99999/python-cryptography-fernet-wrapper)
# usage
* Importing
    ```python
    pip install python-cryptography-fernet-wrapper
    ```
    ```python
    from fernet_wrapper import Wrapper as fernet_wrapper
    ```

* Encrypt
    ```python
    encrypted_data = fernet_wrapper.encrypt(data, key)
    ```

* Decrypt
    ```python
    decrypted_data = fernet_wrapper.decrypt(encrypted_data, key)
    ```

* Generate random key
    ```python
    key = fernet_wrapper.gen_key()
    ```

* Generate key from password
    ```python
    key = fernet_wrapper.key_from_pass(password)
    ```