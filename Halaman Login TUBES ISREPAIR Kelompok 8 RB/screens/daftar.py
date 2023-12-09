 
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import sqlite3
import bcrypt

class Daftar(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file("kv/daftar.kv")
        super().__init__(**kwargs)
    def submit(self):
        nama = self.ids.nama.text
        email = self.ids.email.text
        nohp = self.ids.nohp.text
        alamat = self.ids.alamat.text
        password = self.ids.password.text
        password = password.encode('utf-8')
    
        #koneksi ke database dan insert
        conn = sqlite3.connect('../tubes.db')
        c = conn.cursor()
        
        c.execute("INSERT INTO member (nama, email, nohp, alamat, password)VALUES(:nama, :email, :nohp, :alamat, :password)",
        {
            'nama' : nama,
            'email' : email,
            'nohp' : nohp,
            'alamat' : alamat,
            'password' : password
        })
        conn.commit()
        conn.close()