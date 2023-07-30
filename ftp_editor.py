import ftplib
import sys
import os


class FTP:
    def __init__(self, hostname: str, username: str, password: str):
        # Fill Required Information
        self.hostname = hostname
        self.username = username
        self.password = password

        # Connect FTP Server
        self.ftp = ftplib.FTP(self.hostname, self.username, self.password)
        
        # force UTF-8 encoding
        self.ftp.encoding = "utf-8"
    
    def get_command(self, command: str):
        if (len(command.split()) > 1):
            command_arg = command.split()[1].strip().replace("\"", "").replace("'", "")
        if (command.startswith("cd")):
            self.change_dir(command_arg)
        elif (command.startswith("download")):
            self.download(command_arg)
        elif (command.startswith("upload")):
            self.upload(command_arg)
        elif (command.startswith("dir")):
            self.dir()
        elif (command.startswith("cls")):
            os.system("cls")
    
    def change_dir(self, directory: str):
        self.ftp.cwd(directory)
        
    def download(self, filename: str):
        with open(filename, "wb") as file:
            # Command for Downloading the file "RETR filename"
            self.ftp.retrbinary(f"RETR {filename}", file.write)
        print("Downloaded to " + filename)
    
    def upload(self, filename: str):
        with open(filename, "rb") as file:
            # Command for Uploading the file "STOR filename"
            self.ftp.storbinary(f"STOR {filename}", file)
    
    def dir(self):
        self.ftp.dir()
    
    def quit(self):
        self.ftp.quit()
        
if __name__ == "__main__":
    try:
        ftp = FTP(input("Enter the host name: "), input("Enter the username: "), input("Enter the password: "))
        print("[INFO] Loggined successfuly!")
    except Exception as e:
        print("[ERROR] Something went wrong!\n" + e)
        sys.exit(0)
    while True:
        command = input("> ")
        if command == "quit" or command == "quit":
            break
        ftp.get_command(command=command)
    ftp.quit()
    