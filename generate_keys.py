import pickle
from pathlib import Path
import streamlit_authenticator as stauth

names = ["R Singh", "test 1", "test 2"]
usernames = ["rsingh", "test1", "test 2"]

passwords = ["XXX", "XXX", "XXX"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)