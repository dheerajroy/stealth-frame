# Stealth Frame - Simple Steganography Program

Stealth Frame is a simple steganography program written in Python. It allows you to hide a message within media files, such as images and retrieve the hidden message media files containing the message.

## Requirements

1. To run this program, you need to have Python version 3.10 or greater installed on your system.
2. Media file(s) to perform steganography

## Installation

1. Clone or download the Stealth Frame repository from [GitHub](https://github.com/dheerajroy/stealth-frame).

2. Open a terminal or command prompt and navigate to the program's directory.

## Usage

1. Run the program by executing the `main.py` file using the following command:
```
python main.py
```

2. You will be prompted with an option menu as shown below:
```
Stealth Frame - Embed and retrieve information within media files (simple steganography)
(1). Embed message
(2). Retrieve message
(0). Exit
>>> 
```

3. Choose the appropriate option:
   - Option 1: Embedding a message:
     - Enter the media file path (e.g., image file path) where you want to embed the message.
     - Enter the message you want to hide within the media file.
     - Enter the destination path for the modified media file (make sure the file extension is the same as the original file).
     - The program will embed the message within the media file and save the modified media file at the specified destination path.

   - Option 2: Retrieving a message:
     - Enter the media file path (e.g., image file path) that contains the hidden message.
     - The program will extract and display the hidden message from the media file.

   - Option 0: Exiting the program.