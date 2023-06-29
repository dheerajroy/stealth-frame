import sys
from stealth_frame import StealthFrame

stframe = StealthFrame()


def main():
    """CLI to embed and retrieve information within media files (simple steganography)"""
    while True:
        inp = int(input('Stealth Frame - Embed and retrieve information within media files (simple steganography)\n(1). Embed message\n(2). Retrive message\n(0). Exit\n>>> '))

        match inp:
            case 1:
                path = input('Enter media file path > ')
                message = input('Enter message > ')
                stframe.embed_message(path, message)
                stframe.download_image(input(
                    'Enter destination path (make sure the file extension is same as original file) > '))
                print('Completed! Check the destination file.')
            case 2:
                print(stframe.retrieve_message(
                    input('Enter media file path which contains the message > ')))
            case 0:
                print('Thank you!')
                sys.exit(0)
            case _:
                print('Invalid option!')


if __name__ == '__main__':
    main()
