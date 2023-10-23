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
