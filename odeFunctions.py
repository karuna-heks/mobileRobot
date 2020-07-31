import numpy as np
from math import cos
from math import sin

class odeFunctions:

    # Характеристики модели
    m = 5. # масса
    I = 0.32 # момент инерции вокруг вертикальной оси
    
    # Задание на управление
    vControl = 2.0 # скорость
    tethaControl = 1.2 # угол поворота
    
    # Начальные приращения
    t0 = 0. # время
    ve0 = 0. # скорость
    tethae0 = 0. # угол поворота
    
    # Массивы решений
    ts = []
    ys = []
    
    # решения правых частей 
    def f(self, t, y):
        # список параметров: V' w' x' y' tetha'
        
        # ПД-регулятор скорости
        ve = self.vControl - y[0]
        vu = ve * 0.5 + (ve - self.ve0) * (t - self.t0) * 0.1
        
        # ПД-регулятор угла
        tethae = self.tethaControl - y[4]
        wu = tethae * 0.3 + (tethae - self.tethae0) * (t - self.t0) * 0.4
        
        # сохранение параметров для последующего шага
        self.t0 = t
        self.ve0 = ve
        self.tethae0 = tethae
        
        # правые части системы ОДУ
        dydt = np.zeros(5, dtype=float)
        dydt[0] = vu / self.m
        dydt[1] = wu / self.I
        dydt[2] = cos(y[4]) * y[0]
        dydt[3] = sin(y[4]) * y[0]
        dydt[4] = y[1]
        return  dydt
    
    
    # обработчик шага
    def fout(self, t, y):
        self.ts.append(t)
        self.ys.append(list(y.copy()))
        return 0
        