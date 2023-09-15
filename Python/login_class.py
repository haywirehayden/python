# Login Class

# the idea of 'self'

""" Original example

class Login:

    username = "user1"
    password = "pawssord"
    server = "server.com"

    def login(self):
        print("You have logged in to: ", self.server, "as: ", self.username )

    def emailcheck(self):
        print("You got mail in: ", self.server)

gmail = Login()
gmail.username = "leon"
gmail.server = "gmail.com"

hotmail = Login()
hotmail.username = "bowtieguy2023"
yahoo = Login()
yahoo.server = "yahoo.co.uk"

print(yahoo.emailcheck())
print(gmail.emailcheck())
"""


# better attribute assignation example

class Login:

    def _int_(self,passeduser,passedpw,passedserver):
        self.username = passeduser
        self.password = passedpw
        self.server = passedserver

    def login(self):
        print("You have logged in to: ", self.server, "as: ", self.username)

    def emailcheck(self):
        return "You got mail in: ", + self.server

gmail = Login("gmailname","password123","gmail.com")
hotmail = Login("hotmailname","password7593","hotmail.com")
yahoo = Login("yahooname","passwor8554467fhhgfx","yahoo.com")


print(yahoo.emailcheck()) # running the function in the copies from the class
print(gmail.emailcheck())


print(yahoo) # print the'id' of the class, they will be unique
print(gmail)
print(hotmail)

