import os
import subprocess
import sys

print("""
Hi there! This is a tool which you can use for active/passive reconnaissance.
You can use it to gather information about a target domain.

Which of the following would you like to do?
1. Run active reconnaissance
2. Run passive reconnaissance
3. Run record lookup
4. Exit
""")



def main_loop():
    answer = input("Enter your choice (1-4): ").strip()
    if answer == '1':
        run_active_recon()
    elif answer == '2':
        pass
    elif answer == '3':
        run_record_lookup()
    elif answer == '4':
        print("Exiting the program. Goodbye!")
        sys.exit(0)
    else:
        print("Invalid input. Please enter a number between 1 and 4.")

def run_record_lookup():
    print("Running record lookup...\n\n\n")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(base_dir, 'active-recon', 'record-lookup.py')

    subprocess.run([sys.executable, script_path])
    
def run_active_recon():
    pass

if __name__ == "__main__":
    main_loop()