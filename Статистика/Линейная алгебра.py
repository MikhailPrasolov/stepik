import numpy as np
# 1 Урок. Способы задания матриц
v_hor_np = np.array([1, 2]) # Вектор-строка
print(v_hor_np )

v_vert_np = np.array([[1], [2]]) # Вектор-столбец
print(v_vert_np)

m_sqr_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # В Numpy можно создать квадратную матрицу с помощью метода array().
print(m_sqr_arr)

m_sqr_mx = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # в Numpy есть еще одни способ создания матриц – это построение объекта типа matrix с помощью одноименного метода. Задать матрицу можно в виде списка.
print(m_sqr_mx)

m_sqr_mx = np.matrix('1 2 3; 4 5 6; 7 8 9')# Также доступен стиль Matlab, когда между элементами ставятся пробелы, а строки разделяются точкой с запятой, при этом такое описание должно быть передано в виде строки.
print(m_sqr_mx)

m_diag = [[1, 0, 0], [0, 5, 0], [0, 0, 9]] # Диагональную матрицу можно построить вручную, задав только значения элементам на главной диагонали.
m_diag_np = np.matrix(m_diag)
print(m_diag_np)

m_sqr_mx = np.matrix('1 2 3; 4 5 6; 7 8 9') # Первый вариант подойдет в том случае, если у вас уже есть матрица, и вы хотите сделать из нее диагональную.
print (m_sqr_mx)
diag = np.diag(m_sqr_mx) # Извлечем ее главную диагональ.
print(diag)
m_diag_np = np.diag(np.diag(m_sqr_mx)) # Построим диагональную матрицу на базе полученной диагонали.
print(m_diag_np)

m_e = [[1, 0, 0], [0, 1, 0], [0, 0, 1]] # Создадим единичную матрицу на базе списка, который передадим в качестве аргумента функции matrix().
m_e_np = np.matrix(m_e)
print(m_e_np)

m_eye = np.eye(3) # Такой способ не очень удобен, к счастью для нас, для построения такого типа матриц в библиотеке Numpy есть специальная функция – eye().
print(m_eye)

m_idnt = np.identity(3) # В качестве аргумента функции передается размерность матрицы, в нашем примере – это матрица 3 3. Тот же результат можно получить с помощью функции identity().
print(m_idnt)

m_zeros = np.zeros((3, 3)) # Что касается Numpy, то в составе этой библиотеки есть функция zeros(), которая создает нужную нам матрицу.
print(m_zeros)

m_mx = np.matrix('1 2 3; 4 5 6') # Если у вас уже есть данные о содержимом матрицы, то создать ее можно используя списки Python или функцию matrix() из библиотеки Numpy.
print(m_mx)

m_var = np.zeros((2, 5)) # Если же вы хотите создать матрицу заданного размера с произвольным содержимым, чтобы потом ее заполнить, проще всего для того использовать функцию zeros(), которая создаст матрицу заданного размера, заполненную нулями.
print(m_var)

# 2 Урок

import numpy as np
A1 = np.matrix('1 2 1; -2 3 -3; 3 -4 5')
Y1 = np.matrix('8;-5;10')

A2 = np.matrix('2 1 -1; 0 3 4; 1 0 1')
Y2 = np.matrix('0;-6;1')

A3 = np.matrix('2 -3 -1; 3 4 3; 1 1 1')
Y3 = np.matrix('-6;-5;-2')

A4 = np.matrix('-2 1 0; 1 -2 -1; 3 4 -2')
Y4 = np.matrix('-6; 5; 13')

A5 = np.matrix('3 2 1; 2 3 1; 2 1 3')
Y5 = np.matrix('-8;-3;-1')

A6 = np.matrix('3 2 1; 6 5 4; 9 8 7')
Y6 = np.matrix('1;-2;3')

print(np.linalg.solve(A1,Y1))
print()
print(np.linalg.solve(A2,Y2))
print()
print(np.linalg.solve(A3,Y3))
print()
print(np.linalg.solve(A4,Y4))
print()
print(np.linalg.solve(A5,Y5))


#print (A.transpose(), ' - Транспонирование') # Транспонирование
#print()
#print(np.linalg.det(A), ' - Определитель ') # Определитель
#print()
#print(np.linalg.inv(A), ' - Обратная матрица ') # Обратная матрица
