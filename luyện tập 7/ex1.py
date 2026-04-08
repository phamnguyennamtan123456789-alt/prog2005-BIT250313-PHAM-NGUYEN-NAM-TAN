import matplotlib.pyplot as plt
x = ["Xuất sắc", "Giỏi", "Trung bình", "Yếu", "Kém"]
y = [6, 10, 12, 4, 1]

plt.bar(x, y)

plt.title("Kết quả học tập")
plt.xlabel("Mức độ")
plt.ylabel("Số lượng")
plt.show()