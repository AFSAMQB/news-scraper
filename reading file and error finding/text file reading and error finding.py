def read_text_file(filename):
    """
    Reads a text file and displays its contents with full error handling.
    """
    try:
        # Check if file exists
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        # Display file info and content
        print(f"✅ File '{filename}' opened successfully!")
        print(f"📊 File size: {len(content)} characters")
        print("-" * 50)
        print("📄 CONTENT:")
        print("-" * 50)
        print(content)
        print("-" * 50)
        print("✅ Reading completed!")

    except FileNotFoundError:
        print(f"❌ ERROR: File '{filename}' not found!")
        print("💡 Tip: Make sure the file exists in the same folder")

    except PermissionError:
        print(f"❌ ERROR: Permission denied for '{filename}'")
        print("💡 Tip: Check file permissions or run as administrator")

    except UnicodeDecodeError:
        print(f"❌ ERROR: Cannot read '{filename}' - encoding issue")
        print("💡 Tip: File might have special characters")

    except Exception as e:
        print(f"❌ UNEXPECTED ERROR: {str(e)}")
        print("💡 Tip: Check file path and format")


# Interactive version - asks user for filename
def main():
    print("🔍 TEXT FILE READER")
    print("=" * 40)

    filename = input("📁 Enter filename (e.g., 'sample.txt'): ").strip()

    if not filename:
        print("❌ No filename entered!")
        return

    read_text_file(filename)


# Example usage with sample file creation
def create_sample_file():
    """Creates a sample text file for testing"""
    sample_content = """Hello, World!
This is a sample text file.
Line 2: Python file reading example.
Line 3: Error handling works great!
Line 4: UTF-8 encoding supported ✅"""

    try:
        with open('sample.txt', 'w', encoding='utf-8') as file:
            file.write(sample_content)
        print("📄 Created 'sample.txt' for testing!")
    except Exception as e:
        print(f"⚠️ Could not create sample: {e}")


# RUN PROGRAM
if __name__ == "__main__":
    print("Choose option:")
    print("1. Read any file (interactive)")
    print("2. Read sample.txt (demo)")

    choice = input("Enter 1 or 2: ").strip()

    if choice == "2":
        create_sample_file()
        read_text_file("sample.txt")
    else:
        main()