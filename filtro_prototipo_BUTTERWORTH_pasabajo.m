N = [1 6 15 20 15 6 1];
D = [1 -0.985088 1.140387 -0.529826 0.214099 -0.039112 0.003894];

figure(1)
freqz(N,D)
grid on;

figure(2)
[h,w] = freqz(N,D);
plot(w*200/pi, abs(h)/max(abs(h)));
grid on;

figure(3)
zplane(N, D);
grid on;

