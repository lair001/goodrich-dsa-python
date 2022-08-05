class SubstitutionCipher:
    """Class for doing encryption and decryption using a Substitution cipher."""

    def __init__(self, forward):
        """Construct Substitution cipher using a given encryption string."""

        self._forward = forward  # will store as string
        self._backward = ''.join((chr(forward.index(chr(i + ord('A'))) + ord('A')) for i in range(26)))

    def encrypt(self, message):
        """Return string representing encripted message."""
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        """Return decrypted message given encrypted secret."""
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        """Utility to perform transformation based on given code string."""
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')  # index from 0 to 25
                msg[k] = code[j]  # replace this character
        return ''.join(msg)