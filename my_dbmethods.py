import sqlite3 as sqlite
import os
import pickle
class MyDBCon():

    def __init__(self):
        self.settings_file='settings.pkl'
        self.load_appSettings()
        self.connect_db()
        
    def connect_db(self):
        if os.path.exists(self.appSettings['basename']):
            if 'con' in dir(self):
                self.con.close()
            self.con = sqlite.connect(self.appSettings['basename'])
        else:
            if os.path.exists(os.path.abspath(os.curdir) + '/myBase.db'):
                createIt = False
            else:
                createIt = True
            self.appSettings['basename'] = 'myBase.db'
            self.con = sqlite.connect(self.appSettings['basename'])
            if createIt:
                with self.con:
                    cur = self.con.cursor()
                    #cur.execute("DROP TABLE IF EXISTS Items")
                    cur.execute("CREATE TABLE shabl ( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, keyword TEXT, code TEXT, datechange DATE)")
                    #cur.execute("CREATE TABLE Items(Id INTEGER PRIMARY KEY, Name TEXT, Price INT)")

    def load_appSettings(self):
        if os.path.exists(self.settings_file):
            serialize_obj = pickle.load(open(self.settings_file,'rb'))
            self.appSettings = serialize_obj
        else:
            self.appSettings = {'basename': 'myBase.db'}

    def save_appSettings(self):
        output = open(self.settings_file,'wb')
        pickle.dump(self.appSettings,output,2)
        output.close()

    def set_baseFile(self,newBasename):
        self.appSettings['basename'] = newBasename
        self.connect_db()
        self.save_appSettings()
        
    def baseFile(self):
        return self.appSettings['basename']