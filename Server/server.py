import socket, pickle
HOST = '127.0.0.1'
PORT = 5500
BUFF_SIZE = 4048
def input():
    name = raw_input("Username:")
    password = raw_input("Password:")
    usbid = usb2.main()
    return (name, hashlib.pbkdf2_hmac('sha256', password, b'abcd', 1000), usbid)

class user(object):
    def __init__(self, (name, password, usbid)):
        self.name = name
        self.password = password
        self.usbid = usbid
    def printUser(self):
        print self.name
        # print "USB: ", self.usbid
        # print "Password: ", self.password[0:len(self.password)/2]+"*"*(len(self.password)/2)
    def authen(self, password, usbid):
        if password != self.password:
            print "Wrong password!"
            # return False
            return "Wrong password!"
        else:
            if usbid != self.usbid:
                print "Wrong usb!"
                # return False
                return "Wrong usb!"
            else:
                print "Login success!"
                # return True
                return "Login success!"
class listUser(object):
    def __init__(self, name):
        self.name = name
    accountList = []
    def register(self):
        self.accountList.append(user(input()))
    def printList(self):
        for i in self.accountList:
            print '%d.' %(self.accountList.index(i)+1) ,
            i.printUser()
    def saveList(self, filename):
        try:
            f = open(filename,"w")
            for i in self.accountList:
                pickle.dump(i, f)
            f.close()
            print "Save list %s completed!" % filename
        except:
            print "Save list %s error!" % filename

    def loadList(self, filename):
        f = open(filename, "r")
        while 1:
            try:
                a = pickle.load(f)
                self.accountList.append(a)
            except:
                break
        f.close()
    def authen(self, inp):
        
        temp = None
        for i in self.accountList:
            if inp[0] == i.name:
                temp = i
                return i.authen(inp[1], inp[2])
        if temp == None:
            print "Not found user!"
            return "Not found user!"
class Server():
    def main(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))

        s.listen(10)
        ls = listUser("ls")
        ls.loadList("user.obj")
        ls.printList()
    
        # while 1:
            # conn, addr = s.accept()
            # print "Connection Address:", addr
            # while 1:
            #     data = conn.recv(BUFF_SIZE)
                
            #     if not data:
            #         break
            #     mess = pickle.loads(data)
            #     if mess.opcode == 1:
            #         answer = ls.authen(mess.data)
            #     mess.reply(answer)
            #     conn.send(pickle.dumps(mess))#
            # conn.close()
        conn, addr = s.accept()
        print "Connection Address:", addr
        while 1:
            data = conn.recv(BUFF_SIZE)
                
            if not data:
                break
            mess = pickle.loads(data)
            if mess.opcode == 1:
                answer = ls.authen(mess.data)
            mess.reply(answer)
            conn.send(pickle.dumps(mess))#
        conn.close()
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
server = Server()
server.main()