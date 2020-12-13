# Step3（制御器の導入）

- 対象者：レトロフィット制御の論文を読み，実際にシミュレーションを行いたい技術者．
- 機能：  
    既存のシステムに対して既存のコントローラを付加して，シミュレーションを実行する．  
    既存のコントローラを付加されたシステムの状態空間表現（線形化システム）を取得する．


## 解説
### コントローラの作成

コントローラの作成について説明する．  


#### グローバルコントローラの作成

グローバルコントローラの作成は次のように行う．
```
cg = controller_broadcast_PI_AGC_normal(net, y_idx, u_idx, Kp, Ki);
```
- 入力引数`net`  
    作成したネットワークを設定．`net`は*power_network*クラスのインスタンス．
    詳細は[Step1](/Tutorials/step1/)・[Power Network](/Docs/power_network/)を参照のこと．
- 入力引数`y_idx`  
    出力を観測するバスを設定．
- 入力引数`u_idx`  
    入力を印加するバスを設定．
- 入力引数`Kp` `Ki`  
    コントローラのPIゲイン．
- 出力引数`cg`  
    コントローラの状態空間モデルなどの情報が含まれる．
    - idx：入力を引火するバス（入力引数の`u_idx`と同じ）
    - net：コントローラを付加するネットワーク（入力引数の`net`と同じ）
    - A：コントローラのA行列
    - BeX：コントローラのB行列（観測するバスの状態をスタックしたベクトルに関する）
    - BeV：コントローラのB行列（全てのバスの電圧をスタックしたベクトルに関する）
    - Bu：コントローラのB行列（グローバルコントローラが生成する全てのバスへの入力信号をスタックしたベクトルに関する）
    - C：コントローラのC行列
    - DeX：コントローラのD行列（観測するバスの状態ベクトルに関する）
    - DeV：コントローラのD行列（全てのバスの電圧をスタックしたベクトルに関する）
    - Du：コントローラのD行列（グローバルコントローラが生成する全てのバスへの入力信号をスタックしたベクトルに関する）

power_simulatorではグローバルコントローラがすでにいくつか定義されている．  
詳細は[Controller](/Docs/controller/)を参照のこと．  
本チュートリアルでは，[controller_broadcast_PI_AGC_normal](/Docs/controller/#controller_broadcast_pi_agc_normal)を使用する．  
[controller_broadcast_PI_AGC_normal](/Docs/controller/#controller_broadcast_pi_agc_normal)はブロードキャストAGCの実装で，ゲインを電力に比例させているもの．

#### コントローラの作成

コントローラの作成は次のように行う．
```
c = controller_retrofit_generator_nonlinear_AGC_LQR(net, idx, Q, R, model_uv, vbar, ubar, out, varargin);
```
- 入力引数`net`  
    作成したネットワークを設定．`net`は*power_network*クラスのインスタンス．
    詳細は[Step1](/Tutorials/step1/)・[Power Network](/Docs/power_network/)を参照のこと．
- 入力引数`idx`  
    出力を観測するバスを設定．
- 第3入力引数以降は今回は使用しないので省略．[Controller](/Docs/controller/)を参照のこと．
- 出力引数`c`  
    - K_inter
    - sys_design
    - sys_fb
    - Q
    - R

power_simulator ではコントローラがすでにいくつか定義されている．  
詳細は[Controller](/Docs/controller/)を参照のこと．  
本チュートリアルでは，[controller_retrofit_generator_nonlinear_AGC_LQR](/Docs/controller/#controller_retrofit_generator_nonlinear_agc_lqr)を使用した．  
[controller_retrofit_generator_nonlinear_AGC_LQR](/Docs/controller/#controller_retrofit_generator_nonlinear_agc_lqr)は


### 電力系統モデルに対するコントローラの付加

システムに対するコントローラの付加について説明する．

#### グローバルコントローラの付加

グローバルコントローラの付加は次のように行う
```
net.add_controller_global(controller);
```
- 入力引数`controller`  
    作成したグローバルコントローラを設定．`controller`は*controller*クラスのインスタンス．  
    一つのバスに複数のグローバルコントローラを付加することができる．

#### コントローラの追加

コントローラの付加は次のように行う．
```
net.add_controller(controller);
```
- 入力引数`controller`  
    作成したコントローラを設定．`controller`は*controller*クラスのインスタンス．  
    一つのバスに複数のコントローラを付加した際には，最後に付加したコントローラが使用される．


### システムの状態空間モデル（線形化システム）の取得

システムの状態空間モデルの取得は次のように行う．
```
sys = net.get_sys(with_controller);
```
- 入力引数`with_controller`  
    取得するシステムに制御器を含めるかどうかの設定．  
    *false*：コントローラなし，*true*：コントローラあり（省略した場合は*false*）
- 出力引数`sys`
    詳細は[Step2](/Tutorials/step2/)・[Power Network](/Docs/power_network/)を参照のこと．


## 例1：コントローラを付加したシミュレーション

コントローラを付加したシステムに対して，外乱を印加した時の応答．
```
% 電力系統モデルの作成
net = network_68bus_AGC_varying_impedance();

% システムへのコントローラの付加
cg = controller_broadcast_PI_AGC_normal(net, 1:16, 1:16, -10, -500); % グローバルコントローラの作成
net.add_controller_global(cg); % グローバルコントローラの付加
c = controller_retrofit_generator_nonlinear_AGC_LQR(net, 1); % コントローラの作成
net.add_controller(c); % コントローラの付加

% シミュレーションのためのオプションを定義・決定
option = struct();
option.fault = {{[0 0.07], 1}, {[10 10.05], 10}}; % 地絡の設定

% シミュレーションの実行
out = net.simulate([0 20], option); % 0~20s
```

## 例2：線形化システムの取得

コントローラを付加した電力系統モデル`net`を定義した後に以下を追記すると，状態空間表現（線形化システム）`sys`が得られる．
```
% 線形化システムの取得
with_controller = true; % 制御器あり
sys = net.get_sys(with_controller);
```
