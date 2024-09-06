def insertion_sort(arr):
    # Listemizin uzunluğu kadar döngüye sokuyoruz
    for i in range(1, len(arr)):
        # Şu anki elemanımızı geçici bir değişkene alıyoruz
        temp = arr[i]
        # Bir önceki elemanın indeksini belirliyoruz
        j = i - 1

        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp

arr = [22,27,16,2,18,6]
insertion_sort(arr)
print("Sıralanmış liste:", arr)

# Çıktı 2,6,16,18,22,27 oluyor böylece burada 18 i aramak istediğimiz
#  zaman ortada olduğu için avarage case diyoruz
