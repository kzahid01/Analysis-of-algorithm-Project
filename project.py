# Simple implementation of Diffie-Hellman Key Exchange

# Publicly shared variables
p = 23      # A prime number
g = 5       # A primitive root modulo p

# Alice selects a private key
a = 6
# Bob selects a private key
b = 15

# Calculate public keys
A = (g ** a) % p
B = (g ** b) % p

# Exchange public keys and compute the shared secret
shared_secret_alice = (B ** a) % p
shared_secret_bob = (A ** b) % p

# Print results
print("Publicly shared values:")
print(f"Prime number (p): {p}")
print(f"Primitive root (g): {g}\n")

print("Private keys:")
print(f"Alice's private key (a): {a}")
print(f"Bob's private key (b): {b}\n")

print("Public keys exchanged:")
print(f"Alice sends: {A}")
print(f"Bob sends: {B}\n")

print("Shared secrets computed independently:")
print(f"Alice's shared secret: {shared_secret_alice}")
print(f"Bob's shared secret: {shared_secret_bob}")
