# 使い方
## 実装されたネットワークを利用

power_networkを継承した子クラスとして，netowrk_9bus, network_68busが実装されている．

これらは，busの子クラスbus_non_unit, bus_PV, bus_PQ, bus_slackと，component の子クラスgenerator, load_const_impedance, component_emptyを用いて実装されている．

### コントローラ無しのシミュレーション

たとえば，0～0.01秒にバス1が地絡，10～10.01秒にバス3とバス5が地絡する場合

```matlab
net= network_68bus();
option = struct();
option.fault = {{[0, 0.01], 1}, {[10, 10.01], [3,5]}};
out = net.simulate([0, 100], option);
out_linear = net.simulate_linear([0, 100], option);

% 特定の時刻の出力が必要な場合
out_t = net.sol2signals(out.sol, 0:1:100);

names = {'\delta', '\Delta\omega', 'E', 'V_{fd}', '\xi_1', '\xi_2', '\xi_3'};
for i = 1:16
	figure
	for j = 1:7
		subplot(3, 3, j), plot(out.t, out.X{i}(:, j), out_linear.t, out_linear.X{i}(:, j), out_t.t, out_t.X{i}(:, j), 'o'), title(names{j}, 'Interpreter', 'tex');
	end
	subplot(3, 3, 8), plot(out.t, out.V{i}(:, 1), out_linear.t, out_linear.V{i}(:,1)), title('Real(V)');
	subplot(3, 3, 9), plot(out.t, out.V{i}(:, 2), out_linear.t, out_linear.V{i}(:,2)), title('Imag(V)');
end
```



### 線形システムの活用

get_sysで得られるシステムは平衡点からの偏差を状態ととっていることに注意．

```matlab
net= network_68bus();
option_fault = struct();
option_fault.fault = {{[0, 0.01], 1}};
out_fault = net.simulate_linear([0, 0.01], option_fault);
option = struct();
option.x_init = out_fault.X;
out_linear = net.simulate_linear([0 100], option);
sys = net.get_sys();
x0 = horzcat(out_fault.X{:});
x0 = x0(end, :)' - net.x_ss;
[z, t, x] = initial(sys, x0);
x = x+net.x_ss';
names = {'\delta', '\Delta\omega', 'E', 'V_{fd}', '\xi_1', '\xi_2', '\xi_3'};
for i = 1:16
	figure
	for j = 1:7
		subplot(3, 3, j), plot(out_linear.t, out_linear.X{i}(:, j), '.-', t, x(:, (i-1)*7+j), '.-'), title(names{j}, 'Interpreter', 'tex');
	end
end
```



### レトロフィットコントローラを付加

```matlab
net= network_68bus();

% モデルを用いないレトロフィットコントローラ
c_retro = controller_retrofit_type1(net, 1, 1e-3);
net.add_controller(c_retro);

option_fault = struct();
option_fault.fault = {{[0, 0.01], 1}};
out_fault = net.simulate_linear([0, 0.01], option_fault);

% コントローラのリセット無しのシミュレーション
option1 = struct();
option1.x_init = out_fault.X;
option1.xk_init = out_fault.Xk;
out1 = net.simulate_linear([0.01, 100], option1);
% これでも同じ
out1p = net.simulate_linear([0, 100], option_fault);

% 地絡終了後にリセットをかけた場合 
option2 = struct();
option2.x_init = out_fault.X;
out2 = net.simulate_linear([0.01, 100], option2);

% バス1,8をローカルとし，6次の環境モデルを使ったコントローラ
c_retro2 = controller_retrofit_type1(net, [1, 8], 1e-3, 6);
net.add_controller(c_retro2); % バス1を含んでいるので，1つ目のコントローラは除去される
out3 = net.simulate_linear([0.01, 100], option2);

% 複数のレトロフィットコントローラも可
c_retro3 = controller_retrofit_type1(net, [3,4], 1e-3, 6);
net.add_controller(c_retro3);
out4 = net.simulate_linear([0.01, 100], option2);

figure, subplot(2, 1, 1), plot(out1p.t, out1p.X{1}(:,2), out1.t, out1.X{1}(:,2), out2.t, out2.X{1}(:,2),out3.t, out3.X{1}(:,2), out4.t, out4.X{1}(:,2));
subplot(2, 1, 2), plot(out1p.t, out1p.U{1}, out1.t, out1.U{1}, out2.t, out2.U{1}, out3.t, out3.U{1}, out4.t, out4.U{1})

% hat{z}とcheck{z}
z = out4.X{1}(:,2);
z_check = out4.Xk{1}(:, 2);
z_hat = z - z_check;
figure,subplot(3, 1, 1), plot(out4.t, z);
subplot(3, 1, 2), plot(out4.t, z_hat);
subplot(3, 1, 3), plot(out4.t, z_check);

```



### グローバルコントローラ

```matlab
net= network_68bus();

option_fault = struct();
option_fault.fault = {{[0, 0.01], 1}};
out_fault = net.simulate_linear([0, 0.01], option_fault);
option = struct();
option.x_init = out_fault.X;

out_org = net.simulate_linear([0.01 100], option);

% ブロードキャストコントローラ
c_broadcast = controller_broadcast_PI(net, 1:9, 1:9, -5, -6.5);
c_broadcast = controller_broadcast_PI(net, 10:16, 10:16, -5, -6.5); % 複数も可
net.add_controller_global(c_broadcast);

out1 = net.simulate_linear([0.01 100], option);

% レトロフィットコントローラ
c_retro = controller_retrofit_type1(net, [1, 8], 1e-3, 6);
net.add_controller(c_retro);

out2 = net.simulate_linear([0.01 100], option);

% ブロードキャストコントローラを外してレトロフィットコントローラのみ
net.controllers_global = {};
out3 = net.simulate_linear([0.01 100], option);
plot(out_org.t, out_org.X{1}(:,2), out1.t, out1.X{1}(:,2), out2.t, out2.X{1}(:,2), out3.t, out3.X{1}(:,2))
legend('without', 'broadcast', 'retrofit\_broadcast', 'retrofit');

```


### AGC入力から周波数の受動性

```matlab
% AGC入力をもつ発電機をもつネットワーク
net = network_68bus_AGC_const_power1();

% 受動性の確認
sys_ = net.get_sys(); % 線形化したシステム
% 発電機の入出力を取り出す（他は負荷を変動させるのための入力）
uname = arrayfun(@(i) ['u', num2str(i)], 1:16, 'UniformOutput', false);
sys_ = sys_('z', uname);

% 発電機の入力はAVR, AGCで並んでいるので，AGCだけ取り出す
sys_ = sys_(:, 2:2:end);

sys = ones(1, size(sys_, 1)) * sys_ * ones(size(sys_, 2), 1);
nyquist(sys)
```
