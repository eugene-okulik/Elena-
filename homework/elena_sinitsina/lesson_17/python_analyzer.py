import os
import argparse


def find_text(file_path, search_text, first_only=False):
    found_any = False
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line_num, line in enumerate(lines, 1):
            words = line.split()
            word_indexes = [i for i, word in enumerate(words) if search_text in word]

            if word_indexes:
                for index in word_indexes:
                    start = max(0, index - 5)
                    end = min(len(words), index + 6)
                    context = ' '.join(words[start:end])
                    print(f'File: {os.path.basename(file_path)}, line: {line_num}')
                    print(f'Context: {context}')
                    print('-' * 80)
                    found_any = True
                    if first_only:
                        return
    return found_any


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="Full path to the logs files")
    parser.add_argument("--text", help="Text for search")
    parser.add_argument("--first", help="Show the first match", action="store_true")
    args = parser.parse_args()
    for root, dirs, files in os.walk(args.directory):
        for file in files:
            file_path = os.path.join(root, file)
            found = find_text(file_path, args.text, args.first)
            if found and args.first:
                return


if __name__ == "__main__":
    main()
