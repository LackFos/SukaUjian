# import mysql.connector
# from Database.Connect import Connect

# class Kelas:
#     def __init__(self, nomor, capacity, occupied):
#         self.__nomor = nomor
#         self.__capacity = capacity
#         self.__occupied = occupied == 'True'

#     def pinjamKelas(self, banyakMahasiswa):
#         if self.__occupied:
#             print(f"Kelas {self.__nomor} ini sudah dipakai")
#             return
#         if banyakMahasiswa > self.__capacity:
#             print(f"Kelas {self.__nomor} ini tidak muat")
#         else:
#             print(f"Kelas {self.__nomor} ini berhasil dipinjam")
#             self.__occupied = False

#     def kembalikanKelas(self):
#         self.__occupied = False

# db = Connect()
# result= db.select("kelas")

# result = db.insert("kelas", {"id": "Null", "NomerKelas": "330","Capacity": 50, "Occupied": "True"})
# result = db.update("kelas", {"id":"18" },{"NomerKelas": "340","Capacity": 40, "Occupied": "True"})
# result = db.delete("kelas", {"id": "18"})
# print(result)

#///////////////////////////////////////////////////////////////////////////////////////////////

# import mysql.connector
# from Database.Connect import Connect

# class Kelas:
#     def __init__(self):
#         self.__nomor = input("Enter classroom number: ")
#         self.__capacity = int(input("Enter classroom capacity: "))
#         self.__occupied = input("Is the classroom occupied? (True/False): ")

#     def insert_to_database(self):
#         db = Connect()
#         data = {
#             "NomerKelas": self.__nomor,
#             "Capacity": self.__capacity,
#             "Occupied": self.__occupied
#         }
#         db.insert("kelas", data)
#         print("Data inserted into the database.")

#     def update_in_database(self, new_nomor, new_capacity, new_occupied):
#         db = Connect()
#         criteria = {"NomerKelas": self.__nomor}
#         new_data = {
#             "NomerKelas": new_nomor,
#             "Capacity": new_capacity,
#             "Occupied": new_occupied
#     }
#     db.update("kelas", criteria, new_data)
#     print("Data updated in the database.")



#     def delete_from_database(self):
#         db = Connect()
#         criteria = {"NomerKelas": self.__nomor}
#         db.delete("kelas", criteria)
#         print("Data deleted from the database.")

#     @staticmethod
#     def select_from_database():
#         db = Connect()
#         result = db.select("kelas")
#         return result

# # Create a Kelas object and interactively input data
# kelas = Kelas()
# print("Choose an operation:")
# print("1. Insert")
# print("2. Update")
# print("3. Delete")
# print("4. Select")
# operation = int(input("Enter the operation number: "))

# if operation == 1:
#     kelas.insert_to_database()
# elif operation == 2:
#     new_nomor = input("Enter new classroom number: ")
#     new_capacity = int(input("Enter new classroom capacity: "))
#     new_occupied = input("Is the classroom newly occupied? (True/False): ")
#     kelas.update_in_database(new_nomor, new_capacity, new_occupied)
# elif operation == 3:
#     kelas.delete_from_database()
# elif operation == 4:
#     result = Kelas.select_from_database()
#     print(result)
# else:
#     print("Invalid operation number.")

from Database.Connect import Connect

class Kelas:
    def __init__(self):
        self.__nomor = ""
        self.__capacity = 0
        self.__occupied = ""

    def insert_to_database(self):
        self.__nomor = input("Enter classroom number: ")
        self.__capacity = int(input("Enter classroom capacity: "))
        self.__occupied = input("Is the classroom occupied? (True/False): ")

        db = Connect()
        data = {
            "NomerKelas": self.__nomor,
            "Capacity": self.__capacity,
            "Occupied": self.__occupied
        }
        db.insert("kelas", data)

    def update_in_database(self):
        self.__nomor = input("Enter classroom number to update: ")
        
        # Check if the classroom exists in the database
        if not self.classroom_exists():
            print(f"There is no classroom with number '{self.__nomor}' in the database.")
            return

        new_nomor = input("Enter new classroom number: ")
        new_capacity = int(input("Enter new classroom capacity: "))
        new_occupied = input("Is the classroom newly occupied? (True/False): ")

        db = Connect()
        criteria = {"NomerKelas": self.__nomor}
        new_data = {
            "NomerKelas": new_nomor,
            "Capacity": new_capacity,
            "Occupied": new_occupied
        }
        db.update("kelas", criteria, new_data)

    def delete_from_database(self):
        self.__nomor = input("Enter classroom number to delete: ")

        # Check if the classroom exists in the database
        if not self.classroom_exists():
            print(f"There is no classroom with number '{self.__nomor}' in the database.")
            return

        db = Connect()
        criteria = {"NomerKelas": self.__nomor}
        db.delete("kelas", criteria)

    def classroom_exists(self):
        db = Connect()
        criteria = {"NomerKelas": self.__nomor}
        result = db.select("kelas", criteria)
        return bool(result)  # Returns True if the classroom exists, False otherwise

    @staticmethod
    def select_from_database():
        db = Connect()
        result = db.select("kelas")
        return result

# Create a Kelas object
kelas = Kelas()

print("Choose an operation:")
print("1. Insert")
print("2. Update")
print("3. Delete")
print("4. Select")
operation = int(input("Enter the operation number: "))

if operation == 1:
    kelas.insert_to_database()
elif operation == 2:
    kelas.update_in_database()
elif operation == 3:
    kelas.delete_from_database()
elif operation == 4:
    result = Kelas.select_from_database()
    print(result)
else:
    print("Invalid operation number.")

# test