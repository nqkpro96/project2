import hashlib, binascii, usb2
import pickle
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
            return False
        else:
            if usbid != self.usbid:
                print "Wrong usb!"
                return False
            else:
                print "Login success!"
                return True
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
    def authen(self):
        inp = input()
        temp = None
        for i in self.accountList:
            if inp[0] == i.name:
                temp = i
                return i.authen(inp[1], inp[2])
        if temp == None:
            print "Not found user!"


def main():
    ls = listUser("ls")
    ls.loadList("user.obj")
    ls.printList()
    print ls.authen()

main()