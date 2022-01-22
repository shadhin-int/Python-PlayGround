# import requests
from genericpath import exists
import psycopg2
import json
conn = psycopg2.connect(database='json_postgre', user='post_admin',
                        password='postgre', host='localhost', port='5432')

req ={
        "orderId": 2968276270,
        "symbol": "BTCUSDT",
        "status": "NEW",
        "clientOrderId": "tgitcJ0Io0B3Sja94bPvkb",
        "price": "625",
        "avgPrice": "0.00000",
        "origQty": "10",
        "executedQty": "0",
        "cumQty": "0",
        "cumQuote": "0",
        "timeInForce": "GTC",
        "type": "LIMIT",
        "reduceOnly": False,
        "closePosition": False,
        "side": "BUY",
        "positionSide": "BOTH",
        "stopPrice": "0",
        "workingType": "CONTRACT_PRICE",
        "priceProtect": False,
        "origType": "LIMIT",
        "updateTime": 1642528379744
    }
# data here is a list of dicts
data = req
print(data, "<----------")

def validation_data(val):
    if val != None:
        if type(val) is int:
            return str(val).encode('utf-8')
        else:
            return val
cur = conn.cursor()
# create a table with one column of type JSON
cur.execute("CREATE TABLE IF NOT EXIST placed_order (data json);")

# if conn:
#     for i, item in enumerate(data):
#         orderId = validation_data(item.get("orderId", None))
#         symbol= validation_data(item.get("symbol", None))
#         status= validation_data(item.get("symbol", None))
#         clientOrderId= validation_data(item.get("clientOrderId", None))
#         price= validation_data(item.get("price", None))
#         avgPrice= validation_data(item.get("avgPrice", None))
#         origQty= validation_data(item.get("origQty", None))
#         executedQty= validation_data(item.get("executedQty", None))
#         cumQty= validation_data(item.get("cumQty", None))
#         cumQuote= validation_data(item.get("cumQuote", None))
#         timeInForce= validation_data(item.get("timeInForce", None))
#         type= validation_data(item.get("type", None))
#         reduceOnly= validation_data(item.get("reduceOnly", None))
#         closePosition= validation_data(item.get("closePosition", None))
#         side= validation_data(item.get("side", None))
#         positionSide= validation_data(item.get("positionSide", None))
#         stopPrice= validation_data(item.get("stopPrice", None))
#         workingType= validation_data(item.get("workingType", None))
#         priceProtect= validation_data(item.get("priceProtect", None))
#         origType= validation_data(item.get("origType", None))
#         updateTime= validation_data(item.get("updateTime", None))
    
#     cur.execute("CREATE TABLE placed_order (data json);")

#     cur.execute(
#         'INSERT INTO json_to_mysql.dankrik(kode_booking, nik, nama_pemohon, tgl_datang, waktu_datang,\
#         kantor_imigrasi, alamat) VALUES(%s, %s , %s, %s, %s, %s, %s)', (kode_booking, nik, nama_pemohon, 
#         tgl_datang, waktu_datang, kantor_imigrasi, alamat)
#     )


cur.execute("INSERT INTO placed_order VALUES (%s)", (json.dumps(data),))


# commit changes
conn.commit()
# Close the connection
conn.close()
