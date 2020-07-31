function dydt = odefcn(t, y, V_c, tetha_c)

global m I V_e0 t0 tetha_e0
% V' w' x' y' tetha'

V_e = V_c - y(1);
V_u = V_e*0.5 + (V_e - V_e0)*(t-t0)*0.1;


tetha_e = tetha_c - y(5);
w_u = tetha_e*0.3 + (tetha_e - tetha_e0) * (t-t0) * 0.4;
t0 = t;
V_e0 = V_e;
tetha_e0 = tetha_e;



dydt = zeros(5,1);
dydt(1) = V_u / m;
dydt(2) = w_u / I;
dydt(3) = cos(y(5)) * y(1);
dydt(4) = sin(y(5)) * y(1);
dydt(5) = y(2);