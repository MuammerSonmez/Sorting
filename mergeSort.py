def merge_sort(liste):
    if len(liste) > 1:
        orta = len(liste) // 2
        
        sol_yarim = liste[:orta]
        sag_yarim = liste[orta:]
        

        merge_sort(sol_yarim)
        merge_sort(sag_yarim)

        i = j = k = 0
        

        while i < len(sol_yarim) and j < len(sag_yarim):
            if sol_yarim[i] < sag_yarim[j]:
                liste[k] = sol_yarim[i]
                i += 1
            else:
                liste[k] = sag_yarim[j]
                j += 1
            k += 1
        

        while i < len(sol_yarim):
            liste[k] = sol_yarim[i]
            i += 1
            k += 1
        
        while j < len(sag_yarim):
            liste[k] = sag_yarim[j]
            j += 1
            k += 1

liste = [38, 27, 43, 3, 9, 82, 10]
print("Sırasız liste:", liste)
merge_sort(liste)
print("Sıralı liste:", liste)
