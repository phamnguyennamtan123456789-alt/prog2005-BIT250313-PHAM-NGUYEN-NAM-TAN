import matplotlib.pyplot as plt
import numpy as np

# Tạo dữ liệu
x = np.linspace(-5, 5, 100)

y1 = x**2
y2 = x**3

# Vẽ 2 đồ thị
plt.plot(x, y1, label='y = x^2')
plt.plot(x, y2, label='y = x^3')

# Thêm tiêu đề và legend
plt.title('Đồ thị hàm số')
plt.legend()

# Hiển thị
plt.show()