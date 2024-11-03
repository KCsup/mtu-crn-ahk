import argparse
import os.path as path
import os

def main():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("filename")
    args_parser.add_argument("output_name")
    args_parser.add_argument("macro_key")

    args = args_parser.parse_args()

    INVALID_CHARS = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for c in INVALID_CHARS:
        if c in args.filename:
            print("Invalid input file name.")
            return
        elif c in args.output_name:
            print("Invalid output file name.")
            return

    if not path.isfile(args.filename):
        print("Input file does not exist.")
        return

    if len(args.macro_key) != 1:
        print("Please provide a single key character for the macro.")
        return

    lines = []
    with open(args.filename, "r", encoding="utf-8") as file:
        lines = file.read().split("\n")
        file.close()

    sendText = ""
    for i in range(len(lines)):
        if lines[i]:
            sendText += 'SendText "' + lines[i] + '"\n'
            
            if i != (len(lines) - 2): sendText += 'Send "{Tab}"\n'

    if not path.isdir("out"):
        os.mkdir("out")

    with open(f"out/{args.output_name}.ahk", "w") as out_file:
        out_file.write('+' + args.macro_key + '::{\n' + sendText + 'Send "{Enter}"\n}')
        print(f"Macro written to out/{args.output_name}.ahk")


if __name__ == "__main__":
    main()
