import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A1oUG-YVynhzj35VzwX5CcbYobxKaI5VjKMG7_A1g71CFiD24mcGRv3-9CvfhkDPfEUHz1m9fKibUFMICITZjuC1Xi8a-hnhDpYDs4-iFIwvcrqoEopDJQdK6RXR0_6LFFdJBu3JtpnW'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  
    
    #This is the the full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("Files have been uploaded")


main()