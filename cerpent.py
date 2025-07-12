import os

# Define the block size as a constant
BLOCK_SIZE = 16

def generate_key() -> str:
    """Generate a random 256-bit (32-byte) key and return it as a hex string."""
    key_bytes = os.urandom(32)
    return key_bytes.hex()

def pad(data: bytes, block_size: int = BLOCK_SIZE) -> bytes:
    """Apply PKCS#7 padding."""
    padding_len = block_size - (len(data) % block_size)
    return data + bytes([padding_len] * padding_len)

# Modified unpad to accept block_size
def unpad(data: bytes, block_size: int = BLOCK_SIZE) -> bytes:
    """Remove PKCS#7 padding."""
    # Ensure data is not empty before accessing data[-1]
    if not data:
        raise ValueError("Cannot unpad empty data.")
    padding_len = data[-1]
    # Basic sanity check for padding length and data length
    if padding_len < 1 or padding_len > block_size or len(data) < padding_len:
         raise ValueError("Invalid padding bytes length or data length.")
    # Check if all padding bytes are correct
    if data[-padding_len:] != bytes([padding_len] * padding_len):
         raise ValueError("Invalid padding bytes content.")
    return data[:-padding_len]


def left_rotate(val: int, n: int) -> int:
    """Perform left rotation on an 8-bit value."""
    # Ensure val is treated as an 8-bit integer
    val = val & 0xff
    return ((val << n) & 0xff) | (val >> (8 - n))

def right_rotate(val: int, n: int) -> int:
    """Perform right rotation on an 8-bit value."""
    # Ensure val is treated as an 8-bit integer
    val = val & 0xff
    return ((val >> n) | (val << (8 - n))) & 0xff

def transform_block(block: bytes, key: bytes) -> bytes:
    """
    Transform each byte of the block using the corresponding key byte.
    For each byte B and key byte K:
        - Compute T = B XOR K.
        - Compute T2 = (T + 7) mod 256.
        - Left rotate T2 by 2 bits.
    """
    out = bytearray()
    # Ensure key is long enough for the block, or handle shorter keys
    # For this cipher (block size 16, key 32), this is okay.
    if len(key) < len(block):
         # This check might be too strict if a mode like ECB were used with a short key
         # but for this simple implementation, assume key >= block size
         # A real cipher uses key scheduling to derive round keys from the master key
         raise ValueError("Key length is insufficient for the block size.")

    for i in range(len(block)):
        b = block[i]
        # Use key bytes cyclically if key < block (though not needed with key 32, block 16)
        k = key[i % len(key)]
        t = b ^ k
        t2 = (t + 7) % 256
        y = left_rotate(t2, 2)
        out.append(y)
    return bytes(out)

def inv_transform_block(block: bytes, key: bytes) -> bytes:
    """
    Reverse the transformation:
        - Right rotate each byte by 2 bits.
        - Compute T = (result - 7) mod 256.
        - Compute original byte = T XOR key_byte.
    """
    out = bytearray()
    if len(key) < len(block):
         raise ValueError("Key length is insufficient for the block size.")


    for i in range(len(block)):
        b = block[i]
        k = key[i % len(key)]
        t2 = right_rotate(b, 2)
        # Handle negative result from subtraction using modulo
        t = (t2 - 7) % 256
        original = t ^ k
        out.append(original)
    return bytes(out)


def encrypt(plaintext: str, key_hex: str) -> str:
    """
    Encrypt plaintext using the Cerpent Cipher.
    The plaintext is UTF-8 encoded, padded to BLOCK_SIZE bytes per block,
    and each block is transformed. The ciphertext is returned as a
    comma-separated hex string.
    """
    try:
        key_bytes = bytes.fromhex(key_hex)
        if len(key_bytes) != 32: # Enforce 256-bit key length
            raise ValueError("Key must be exactly 64 hexadecimal characters (256 bits).")
    except ValueError as e:
        # Re-raise with a more user-friendly message if it was a hex issue
        if "non-hexadecimal number" in str(e) or "Odd-length string" in str(e):
             raise ValueError("Invalid hex key format. Key must be a hex string.")
        raise # Re-raise other ValueError

    plaintext_bytes = plaintext.encode('utf-8')
    padded = pad(plaintext_bytes, BLOCK_SIZE) # Use constant BLOCK_SIZE
    ciphertext_blocks = []
    for i in range(0, len(padded), BLOCK_SIZE): # Use constant BLOCK_SIZE
        block = padded[i:i+BLOCK_SIZE] # Use constant BLOCK_SIZE
        transformed = transform_block(block, key_bytes)
        ciphertext_blocks.append(transformed.hex())
    return ",".join(ciphertext_blocks)

def decrypt(ciphertext: str, key_hex: str) -> str:
    """
    Decrypt the ciphertext (a comma-separated hex string) and return the plaintext.
    """
    try:
        key_bytes = bytes.fromhex(key_hex)
        if len(key_bytes) != 32: # Enforce 256-bit key length
            raise ValueError("Key must be exactly 64 hexadecimal characters (256 bits).")
    except ValueError as e:
         if "non-hexadecimal number" in str(e) or "Odd-length string" in str(e):
             raise ValueError("Invalid hex key format. Key must be a hex string.")
         raise # Re-raise other ValueError


    blocks = ciphertext.split(",")
    decrypted_bytes = bytearray()
    for block_hex in blocks:
        if not block_hex:
            continue # Skip empty strings from split
        try:
            block = bytes.fromhex(block_hex)
            if len(block) != BLOCK_SIZE: # Use constant BLOCK_SIZE
                 raise ValueError(f"Invalid hex block size encountered during decryption: {len(block)} bytes, expected {BLOCK_SIZE}.") # Use constant BLOCK_SIZE
        except ValueError:
            raise ValueError(f"Invalid hexadecimal characters found in ciphertext block: {block_hex}")

        inv_transformed = inv_transform_block(block, key_bytes)
        decrypted_bytes.extend(inv_transformed)

    unpadded = unpad(decrypted_bytes, BLOCK_SIZE) # Pass BLOCK_SIZE to unpad
    return unpadded.decode('utf-8')