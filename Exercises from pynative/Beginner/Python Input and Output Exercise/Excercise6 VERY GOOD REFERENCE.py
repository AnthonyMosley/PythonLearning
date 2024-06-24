#import
import logging
#Exercise 6: Write all content of a given file into a new file by skipping line number 5




#define functions before main
def createtest(fileString:str)->None:
    with open(fileString,'w') as fp:
        fp.write('line1')
        fp.write('\nline2')
        fp.write('\nline3')
        fp.write('\nline4')
        fp.write('\nline5')
        fp.write('\nline6')
        fp.write('\nline7')
def readfile(fileString: str) -> list:
    with open(fileString, 'r') as fp:
        content = fp.readlines()
        logging.debug(f"This is whats in this file: {content}")
    return [line.strip() for line in content]

def skipLines(readFileFunc: list, newFileName: str) -> None:
    with open(newFileName, 'w') as fp:
        for i, line in enumerate(readFileFunc):
            if i != 4:  # Skip line 5
                fp.write(line)


def main()->None:
#body of code here
    #BASIC LOGGING VVV
    level = logging.DEBUG
    fmt= '[%(levelname)s] %(asctime)s- %(message)s'
    logging.basicConfig(level=level,format=fmt)
    #BASIC LOGGING ^^^

    createtest("test.txt")
    new_file_content = skipLines(readfile("test.txt"), "new_file.txt")
    readfile("new_file.txt")  # Print the contents of the new file
if __name__ == '__main__':
    main()