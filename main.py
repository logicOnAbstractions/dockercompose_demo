import sys
import os
print("Hello world!")
print(f"Printing current os.environ values - including any set in DOckefile/compose file etc.")
envars = os.environ
for var, value in envars.items():
    print(f"{var}: {value}")
print(f"Current working directory: {os.getcwd()}")

print(f"Listing all files & folder in working directory:")
for file_folder in os.listdir():
    print(f"{file_folder}")
