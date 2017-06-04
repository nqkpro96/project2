import socket
import hashlib, binascii, usb2
import pickle
IP = "127.0.0.1"
PORT = 5500
BUFF_SIZE = 2048
def input():
    name = raw_input("Username:")
    password = raw_input("Password:")
    usbid = usb2.main()
    return (name, hashlib.pbkdf2_hmac('sha256', password, b'abcd', 1000), usbid)
class Client():
    def main(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((IP,PORT))
        except:
            print "Error connect to server!"
            exit(1)
        
        mess = Mess()
        mess.authenRequest()

        s.send(pickle.dumps(mess))
        # mess.printInfo()
        recv_buff = s.recv(BUFF_SIZE)
        mess = pickle.loads(recv_buff)
        if mess.opcode == 2:
            print "Server return:",mess.data
        # print mess.data
        s.close()
class Mess(object):
    def __init__(self):
        self.opcode = 0
        self.data = None
        
    def authenRequest(self):
        self.opcode = 1
        self.data = input()
    def reply(self, reply):
        self.opcode = 2
        self.data = reply   
    def printInfo(self):
        print self.opcode, self.data
client = Client()
client.main()