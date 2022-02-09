import requests

with open('creds', 'r') as f:
    uname, pswd = f.read().split()


class Quizlet:
    pswd: str
    uname: str
    session: requests.Session
    url = 'https://www.quizlet.com'

    def __init__(self, uname, pswd):
        self.uname = uname
        self.pswd = pswd
        self.session = requests.Session()
        self.login()
    
    def login_payload(self):
        return {"username":self.uname, "password":self.pswd}

    def login(self):
        self.session.post(url+'/login', self.login_payload())
    
    def test(self):
        r = self.session.get('https://quizlet.com/latest')
        print(r.text)
