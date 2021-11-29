import os
import json
import pymysql
from pymysql.cursors import Cursor

json_data = 'dekrip.json'
read_data = open(file=json_data).read()
load_data = json.loads(read_data)
# print(load_data)


def validation_data(val):
    if val != None:
        if type(val) is int:
            return str(val).encode('utf-8')
        else:
            return val

con = pymysql.connect(host='127.0.0.1', user='db_admin', passwd='password', db='json_to_mysql', port=3306)
cursor = con.cursor()

if con:
    for i ,item in enumerate(load_data):
        kode_booking = validation_data(item.get("kode_booking", None))
        nik = validation_data(item.get("nik", None))
        nama_pemohon = validation_data(item.get("nama_pemohon", None))
        tgl_datang = validation_data(item.get("tgl_datang", None))
        waktu_datang = validation_data(item.get("waktu_datang", None))
        kantor_imigrasi = validation_data(item.get("kantor_imigrasi",None))
        alamat = validation_data(item.get("alamat", None))

    cursor.execute(
        'INSERT INTO json_to_mysql.dankrik(kode_booking, nik, nama_pemohon, tgl_datang, waktu_datang,\
        kantor_imigrasi, alamat) VALUES(%s, %s , %s, %s, %s, %s, %s)', (kode_booking, nik, nama_pemohon, 
        tgl_datang, waktu_datang, kantor_imigrasi, alamat)
    )
    con.commit()
    con.close()
    print("Successfull.....!")

# print(load_data, "<-------------------data")