clc, clear
global m I V_e0 t0 tetha_e0

%% Initial Condition
tspan = [0 500];
V0 = 0;
w0 = 0;
x0 = 0;
y0 = 0;
tetha0 = 0;
init = [V0 w0 x0 y0 tetha0];
V_e0 = 0;
t0 = 0;
tetha_e0 = 0;

%% Model parameters
m = 5;
I = 0.32;

%% Controlling variables
V_c = 2;
tetha_c = 1.2;

%% Solver
[t, dxdt] = ode45(@(t, dxdt) odefcn(t, dxdt, V_c, tetha_c), tspan, init);

%% Plot
subplot(5,1,1)
plot(t, dxdt(:,1), 'r')
title('V')
grid on
subplot(5,1,2)
plot(t, dxdt(:,2), 'r')
title('w')
grid on
subplot(5,1,3)
plot(t, dxdt(:,3), 'r')
title('x')
grid on
subplot(5,1,4)
plot(t, dxdt(:,4), 'r')
title('y')
grid on
subplot(5,1,5)
plot(t, dxdt(:,5), 'r')
title('tetha')
grid on
