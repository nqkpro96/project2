import hashlib, binascii, usb2
import pickle
def input():
    name = raw_input("Username:")
    password = raw_input("Password:")
    usbid = usb2.main()
    return (name, hashlib.pbkdf2_hmac('sha256', password, b'abcd', 1000), usbid)

class account(object):
    def __init__(self, (name, password, usbid)):
        self.name = name
        self.password = password
        self.usbid = usbid
        self.blockStatus = False
    def getName(self):
        return self.name
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
    def menu(self):
        pass
class user(account):
    pass

class admin(account):
    def __init__(self, (name, password, usbid)):
        self.name = name
        self.password = password
        self.usbid = usbid
        self.listUser = None
    def search(self, name):
        for i in self.listUser:
            if i.getName() == name:
                print i.getName()
                return i
        return None
    def register(self):
        self.listUser.register()
    def delete(self, name):
        self.listUser.delete(name)
    def block(self, name):
        for i in self.listUser:
            if i.getName() == name:
                if i.blockStatus == False:
                    i.blockStatus = True
                else:
                    i.blockStatus = False
        return None
    def menu(self):
        print "1. Register new user"
        print "2. Delete user"
        print "3. Block user"
        print "4. Print all username"
        choose = int(raw_input("Choose :"))
        if choose == 1:
            self.listUser.register()
        elif choose == 2:
            name = raw_input("Name account to be delete:")
            self.listUser.delete(name)
        elif choose == 3:
            name = raw_input("Name account to be block/unblock:")
            self.block(name)
        elif choose == 4:
            # name = raw_input("Name account to be delete:")
            self.listUser.printList()


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
            print "Not found account!"
    def delete(self, name):
        for i in self.accountList:
            if i.getName() == name:
                self.accountList.remove(i)


def main():
    ls = listUser("ls")
    ls.loadList("user.obj")
    root = admin(("root", None, None))
    root.listUser = ls
    root.menu()
    ls.saveList("user.obj")
    # ls.authen()

main()