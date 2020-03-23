import web
db = web.database(dbn='mysql', user='root', pw='bc8ab63dc88a70d8', db='TESTDB')

urls = (
    '/register', 'index',
    '/add', 'post'
)


class index:
    def GET(self):
        return open(r'register.html').read()


class post:
    def POST(self):
        data = web.input()
        db.insert('EMPLOYEE', FIRST_NAME=data.title,LAST_NAME='ddq', AGE=29, SEX='passwd', INCOME=666666)
        
        
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
