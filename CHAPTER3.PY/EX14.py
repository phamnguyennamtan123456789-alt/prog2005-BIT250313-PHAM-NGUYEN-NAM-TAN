def count_vowels(s):
    # Chuyển chuỗi về chữ thường
    s = s.lower()

    nguyen_am = "aeiou"
    dem = 0

    for ky_tu in s:
        if ky_tu in nguyen_am:
            dem += 1

    return dem


# Thử hàm
chuoi = input("Nhập một chuỗi: ")
print("Số nguyên âm trong chuỗi là:", count_vowels(chuoi))