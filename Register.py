import hashlib, binascii
class user(object):
    def __init__(self, name, password):
        self.name = name
        self.password = password
    def printUser(self):
        print "Username: ", self.name
        print "Password: ", self.password[0:len(self.password)/2]+"*"*(len(self.password)/2)
    def logIn(self, name, password):
        if name == self.name:
            if password == self.password:
                return True
        else:
            return False
class listUser(object):
    def __init__(self, name):
        self.name = name
    userList = []
    def register(self, name, password):
        self.userList.append(user(name, hashlib.pbkdf2_hmac('sha256', password, b'abcd', 1000)))
    def printAll(self):
        for i in self.userList:
            i.printUser()
    def logIn(self):
        username = raw_input("Username: ")
        password = raw_input("Password: ")
        Check = False
        for i in self.userList:
            Check = i.logIn(username, hashlib.pbkdf2_hmac('sha256', password, b'abcd', 1000))
            if Check == True:
                i.printUser
                print "loged in"
                return i
        print "Not found user!"
        return False

DS = listUser("DS")
DS.register("Khanh", "123456")
DS.register("Khoa", "123456")
DS.register("Tung", "123456")
DS.register("Hai", "123456")
DS.printAll()
DS.logIn()
