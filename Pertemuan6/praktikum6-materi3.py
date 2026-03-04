# =============================================
# Nama : Rifqi Tazakka Putra
# NIM  : J0403251158
# =============================================

# =============================================
# Merge Sort (Ascending)
# =============================================


def mergeSort(data, depth=0):
    
    indent = " " * depth # Indentasi berdasarkan level rekursif
    print(f"{indent}mergeSort({data})")
    
    if len(data) <= 1:
        return data
    
    # Divide : Membagi data menjadi 2 bagian
    mid = len(data) // 2
    left = data[:mid] # Slicing bagian kiri
    right = data[mid:] # Slicing bagian kanan
    
    print(f"{indent}divede -> left = {left} | right = {right}")
    
    # Kalau ada 8 data ==> left 4 right 4
    # Left 4 ==> mergesort ==>
    # Dan right 2 ==> mergesort
    
    # Recursive Call
    left_sorted = mergeSort(left)
    right_sorted = mergeSort(right)
    
    merged = merge(left_sorted, right_sorted)
    print(f"{indent}merge -> {left_sorted} + {right_sorted} = {merged}")
    
    return merged

def merge(left,right):
    
    result = []
    i = 0
    j = 0
    
    # Membandingkan elemen kiri dan kanan
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    # Membandingkan sisa elemen jika ada
    result.extend(left[i:])
    result.extend(right[j:])

    return result

angka = [13,7,28,5,19,36,4]
print("Hasil Sort : ", mergeSort(angka))



