import argparse

def main():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("filename")

    args = args_parser.parse_args()

    lines = []
    with open(args.filename, "r", encoding="utf-8") as file:
        lines = file.read().split("\n")
        file.close()

    sendText = ""
    for i in range(len(lines)):
        if lines[i]:
            sendText += 'SendText "' + lines[i] + '"\n'
            
            if i != (len(lines) - 2): sendText += 'Send "{Tab}"\n'

    with open("crn-macro.ahk", "w") as out_file:
        out_file.write('+n::{\n' + sendText + 'Send "{Enter}"\n}')


if __name__ == "__main__":
    main()
