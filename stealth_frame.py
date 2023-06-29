
class StealthFrame:
    """Embed and retrieve information within media files (simple steganography)."""

    def __init__(self):
        self.content = ''

    def embed_message(self, srcpath, message):
        """Embeds the message within the media file.
        Takes in 2 parameters, srcpath: path to the original file
        message: the message you want to embed."""

        with open(srcpath, 'rb') as f:
            self.content = bytearray(f.read()) + message.encode()

    def download_image(self, destpath):
        """After embedding the message you can download a new media file by providing
        destpath: which takes in the path where you want to store the modified file.
        Make sure the file extension is same as original file."""

        with open(destpath, 'wb') as f:
            f.write(self.content)

    @staticmethod
    def retrieve_message(path):
        """Extracts the message from the media file and returns it. Takes no parameters."""

        with open(path, 'rb') as f:
            message_data = str(bytearray(f.read())).rpartition('\\')[-1][3: -2]
            return message_data


if __name__ == '__main__':
    stframe = StealthFrame()
    stframe.embed_message('img.png', 'Hello world')
    stframe.download_image('secretimg.png')
    print(stframe.retrieve_message('secretimg.png'))
