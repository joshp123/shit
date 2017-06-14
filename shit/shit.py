# shouty git
import sys
import subprocess

def main():
    shouty_args = sys.argv[1:]
    chill_args = [a.lower() for a in shouty_args]
    result = subprocess.run(['git'] + chill_args, stdout=subprocess.PIPE)
    return result.returncode

if __name__ == '__main__':
    main()
