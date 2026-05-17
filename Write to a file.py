# Step 1: Open file in write mode ('w')
with open('myfile.txt', 'w') as file:
    file.write("Hello! This is line 1.\n")
    file.write("This is line 2.\n")
    file.write("Python file handling is easy!\n")

print("✅ File created and written successfully!")