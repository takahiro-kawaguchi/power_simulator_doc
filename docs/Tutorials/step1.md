# Step1（既存の系統モデルのシミュレーション）

- 対象者：制御工学についての知識はあるが，電力系統については知識がない技術者
- 機能：  
    既存の電力系統モデルに対して，シミュレーションを実行する  
    特に，初期値応答・外乱応答・入力応答

## 初期値応答

```
net = network_68bus_AGC_varying_impedance();  % 既存のネットワークを利用

option = struct();
option.x_init = net.x_ss; % 平衡点
option.x_init(1) = option.x_init(1) + 0.1;

out = net.simulate([0 20], option);  % [0 20]はシミュレーション時間
```

## 外乱応答

```
net = network_68bus_AGC_varying_impedance();  % 既存のネットワークを利用

option = struct();
option.fault = {{[0 0.07], 1}, {[10 10.05], 10}};
% 地絡の設定．0~0.07秒にバス1, 10~10.05秒にバス10の地絡

out = net.simulate([0 20], option);
```

## 入力応答

```
net = network_68bus_AGC_varying_impedance();  % 既存のネットワークを利用

N = 1000; % データ数
Ts = 0.01; % サンプリング周期
t = (0:N-1)*Ts;
u = randn(N, 4); % 今回は2つのバスに入力するので2x2=4
bus_u = [1, 10]; % 入力するバス

out = net.simulate(t, u, bus_u); % 入力を0次ホールド
out_foh = net.simulate_foh(t, u, bus_u); % 入力を1次ホールド
```

## 初期値・外乱・入出力応答（組み合わせ）

```
net = network_68bus_AGC_varying_impedance(); 
% 既存のネットワークを利用

option = struct();
option.x_init = net.x_ss; % 平衡点
option.x_init(1) = option.x_init(1) + 0.1;
option.fault = {{[0 0.07], 1}, {[10 10.05], 10}};
N = 1000; % データ数
Ts = 0.01; % サンプリング周期
t = (0:N-1)*Ts;
u = randn(N, 4);
bus_u = [1, 10];
out = net.simulate(t, u, bus_u, option);
```
