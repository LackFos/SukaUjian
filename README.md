# Dokumetansi Database 🤙

## Koneksi ke database

- Masukkan credential database di file .env
- Buat instance baru dari class /Database/Connect

## Methods

### select

`Connect.select(table, column="*")`

- table (string) : nama table yang digunakan
- column (array) : column yang ingin diselect (default value \*, jadi parameter ini dibiarkan kosong method ini akan return seluruh column yang ada)

```
Connect.select("user", ["id", "name", "password"])
```

> Ini Akan return semua rows column `id, name, dan password` dari table `user`

### get

`Connect.get(table, where, column="*")`

- table (string) : nama table yang digunakan
- where (dictionary) : row dengan value yang cocok akan terdampak
- column (array) : column yang ingin diselect (default value \*, jadi parameter ini dibiarkan kosong method ini akan return seluruh column yang ada)

```
Connect.get("user", {"id": "1"}, ["id", "nama", "password"])
```

> Ini Akan return semua rows column `id, name, dan password` dari table `user` yang cocok dengan kondisi `where`

### first

`Connect.first(table, where, column="*")`

- table (string) : nama table yang digunakan
- where (dictionary) : row dengan value yang cocok akan terdampak
- column (array) : column yang ingin diselect (default value \*, jadi parameter ini dibiarkan kosong method ini akan return seluruh column yang ada)

```
Connect.get("user", {"id": "1"}, ["id", "nama", "password"])
```

> Ini Akan return satu rows column `id, name, dan password` dari table `user` yang cocok dengan kondisi `where`

### insert

`Connect.insert(table, data)`

- table (string) : nama table yang digunakan
- data (dictionary) : data yang ingin dimasukkan

```
Connect.insert("user", {"nama": "Elvis", "password": "12345", "role": "mahasiswa"})
```

> Ini menambahkan data berikut ke dalam table `user` :

| nama  | password |   role    |
| :---: | :------: | :-------: |
| Elvis |  12345   | mahasiswa |

### update

`Connect.update(table, where, data)`

- table (string) : nama table yang digunakan
- where (dictionary) : row dengan value yang cocok akan terdampak
- data (dictionary) : data yang ingin diperbarui

```
Connect.update("user", {"id": "1"}, {"nama": "FarizKece"})
```

> Ini akan mengubah value column nama dari table `user` dengan `id = 1` menjadi FarizKece

### delete

`Connect.delete(table, where)`

- table (string) : nama table yang digunakan
- where (dictionary) : row dengan value yang cocok akan terdampak

```
Connect.delete("user", {"id": "5"})
```

> Ini akan menghapus rows dengan id `5` didalam table `user`

### close

`Connect.close()`

> Method ini digunakkan untuk menutup koneksi database
