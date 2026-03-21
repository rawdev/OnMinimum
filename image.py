import numpy as np
import matplotlib.pyplot as plt

# 1. 데이터 생성 (x, y 범위는 -5 ~ 5)
x = np.linspace(-5, 5, 30)
y = np.linspace(-5, 5, 30)
X, Y = np.meshgrid(x, y)

# 2. 함수 정의: f(x, y) = x^2 + y^2
Z = X**2 + Y**2

# 3. 3D 그래프 생성
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# 4. 표면 그리기 (색상은 'aliceblue'로 더 밝게, 격자선은 검은색)
ax.plot_surface(X, Y, Z, color='aliceblue', edgecolor='black', linewidth=0.8, antialiased=True)

# 5. 축 라벨 설정
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)')

# 6. 축 범위 설정
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([0, 50])

# 7. 이미지와 비슷한 원근감/각도 조정
ax.view_init(elev=25, azim=-45)

# 8. 그래프 저장 및 표시
plt.savefig('generated_image.png')
plt.show()
