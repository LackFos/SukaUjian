from Database.Connect import Connect

db=Connect()
result=db.get('ujian', {"Matakuliah": "Matematika"})
y=result.get("MataKuliah")
print(y)