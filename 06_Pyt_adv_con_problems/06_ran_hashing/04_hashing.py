import hashlib
import re
import os
import hmac

def generate_salt(length:int=16) -> str:
	'''Generate a random salt for password hashing'''
	return os.urandom(length).hex()
	
def hash_password(password: str,salt:str) -> str:  #Hashes The Password
	return hashlib.sha256((password + salt).encode()).hexdigest()
    
def store_password(password:str) ->str:
	'''Store the password securely with a salt and hash'''
	if not is_strong(password):
		raise ValueError("Password too weak. Use 8+ chars, mix of cases, digits, symbols.")
	salt = generate_salt()
	hashed = hash_password(password,salt)
	return f"{salt}${hashed}"

def verify_password(user_input:str,stored_password:str) -> bool:
	salt,hashed = stored_password.split("$")
	input_hash = hash_password(user_input,salt)
	return hmac.compare_digest(input_hash,hashed)
	
def is_strong(password: str) -> bool:
    return bool(re.fullmatch(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}', password))


try:
	user_input = str(input("🔑 Enter Password to Store : "))
	stored_value = store_password(user_input)
	print("Stored Securely :",stored_value)
except ValueError as ve:
    print("❌", ve)
    exit()

# --- Simulate Login ---
login_pass = input("🔑 Enter password to login: ")
if verify_password(login_pass, stored_value):
    print("✅ Login successful!")
else:
    print("❌ Incorrect password.")
