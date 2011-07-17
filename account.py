from google.appengine.ext import db

# there has to be a better way to deal with userinfo data        
class Account(db.Model):
    access_token = db.StringProperty()
    name = db.StringProperty()
    user_info = db.StringProperty()
    family_name = db.StringProperty()
    locale = db.StringProperty()
    gender = db.StringProperty()
    email = db.StringProperty()
    given_name = db.StringProperty()
    google_account_id = db.StringProperty()
    verified_email = db.BooleanProperty()
    link = db.StringProperty()
    picture = db.StringProperty()
    
    def __str__(self):
        return u'name=%s family_name=%s locale=%s gender=%s email=%s given_name=%s google_account_id=%s verified_email=%s' % (self.name, self.family_name, self.locale, self.gender, self.email, self.given_name, self.google_account_id, self.verified_email)
        