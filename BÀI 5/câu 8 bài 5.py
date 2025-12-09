import numpy as np

kieu_du_lieu = [
    ('ten', 'U20'),       
    ('chieucao', 'f4'),   
    ('lop', 'U10')        
]
sinh_vien = np.array([
    ('An', 165.2, '10A1'),
    ('Bình', 170.5, '10A2'),
    ('Chi', 160.3, '10A1'),
    ('Duy', 172.1, '10A3'),
    ('Hà', 158.7, '10A2'),
], dtype=kieu_du_lieu)

sinh_vien_sapxep = np.sort(sinh_vien, order=['lop', 'chieucao'])
print(sinh_vien_sapxep)
