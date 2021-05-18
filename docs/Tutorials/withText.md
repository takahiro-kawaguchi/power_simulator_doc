# Tutorial

このチュートリアルではテキストの内容に沿ってpower_simulatorを使ってテキスト内でも触れていた電力系統システムを自作し，その制御シミュレーションを行う方法を解説します．  
具体的には、

- テキストの題１章で扱われていた3busシステムを定義する。
- 各コンポーネントに実際に発電機や負荷を設置し、具体的なパラメータを代入する。
- 定義した電力モデルの時間応答を解析したり、コントローラを負荷して解析を行う。  

といった流れで進めていこうと思います。

## 対象となるシステムの自作

本チュートリアルにおいては以下の図ような単純な電力系統システムを自作します．

![](/Figures/write_3bus.png)

この電力系統システムでは３つのバスと機器が繋がっているシステムです．

### 電力系統システムの定義

全ての電力系統システムは`power_network`クラスを用いて実装されます．以下のようにして電力系統クラスを定義します．

```matlab
net = power_network();
```

イメージでいうと、空のテンプレート表のようなものを変数`net`にあてはめ、これからこの表に機器の情報やブランチ・バスの情報を書き込んでいくための準備のようなプロセスです。

### 送電網の定義

まずは各ブランチ間をつなぐ送電網を定義します．`power_network`クラスには`branch`というメンバー変数があり，そこに送電網に関するパラメーターを定義します．
以下，その定義例です．

```matlab
branch =

  2×7 table

    bus_from    bus_to    x_real    x_imag    y    tap    phase
    ________    ______    ______    ______    _    ___    _____

       1          2         0       0.0576    0     1       0  
       3          2         0       0.0625    0     1       0  
```

```matlab
net.branch = branch;
```
各送電網のパラメーターについては詳しくは[power_network branchについて](path_to_doc_powernetwork_branch)を参照してください

### バス

#### Slackバス

slackバス(swingバス)とは[潮流計算](https://en.wikipedia.org/wiki/Power-flow_study)のため特別な発電機バスです．

```matlab
net.bus{1} = bus_slack(1.0, 0.0, [0, 0]);
```

引数・各パラメーターについては[bus_slack](path_to_doc_bus_slack)を参照してください．

#### Generatorバス

Generatorバスとは発電機(Generator)を接続するためのバスです．プログラム上では以下のように

```matlab
net.bus{2} = bus_PV(1.0, 1.7, [0, 0]);
```
引数・各パラメーターについては[bus_PV](path_to_doc_bus_PV)を参照してください．

#### Loadバス

Loadバスとは負荷を接続するためのバスです．プログラム上では以下のように

```matlab
net.bus{3} = bus_PQ(-1.25, -0.5, [0, 0]);
```
引数・各パラメーターについては[bus_PQ](path_to_doc_bus_PQ)を参照してください．

### 機器

機器を定義し，先程の定義したbusに接続します．プログラム上ではi番目のバスに機器を接続するときは

```matlab
net.bus{i}.add_component(machine);
```
のようにします．

### generator
slackバスとgeneratorには機器としてgeneratorを接続します．
generatorを自作するためには以下のような関数を用います．

```matlab
generator_AGC(mac, exc, pss)
```

各引数,mac,exc,pssはgeneratorのパラメーターに関する[table](https://jp.mathworks.com/help/matlab/tables.html)オブジェクトです．詳しくは，[generator](path_to_doc_generator)を参照してください．

以下，generatorを生成しslackバスに接続するまでのコード例を示します．
```matlab
% mac
Xd = 1.6;
Xdp = 0.32;
Xq = 1.59;
Tdo = 6.0;
M = 100;
d = 2;
mac = table(Xd, Xdp, Xq, Tdo, M, d);

% exc
Ka = 2.0;
Te = 0.05;
exc = table(Ka, Te);

% pss
Kpss = 200;
Tpss = 10;
TL1p = 0.05;
TL1 = 0.015;
TL2p = 0.08;
TL2 = 0.01;
pss = table(Kpss, Tpss, TL1p, TL1, TL2p, TL2);

net.bus{1}.add_component(generator_AGC(mac, exc, pss));
```

### load

power_simulator内には以下の4つのloadが用意されています．

- [load_const_impedance](path_to_load_const_impedance)
- [load_const_power](path_to_load_const_power)
- [load_varying_impedance](path_to_load_varying_impedance)
- [load_varying_power](path_to_load_varying_power)

本チュートリアルにおいては，[load_varying_impedance](path_to_load_varying_impedance)を用います．

```
net.bus{3}.add_component(load_varying_impedance())
```

### 電力系統の自作のコードの全体

```matlab
net = power_network();
net.bus = cell(3, 1);

branch_array = [
    1 2	0	0.0576	0	1	0;
    3 2 0	0.0625	0	1	0;
    ];

branch = array2table(branch_array, 'VariableNames', ...
    {'bus_from', 'bus_to', 'x_real', 'x_imag', 'y', 'tap', 'phase'}...
    );

net.branch = branch;
%% slack
net.bus{1} = bus_slack(1.0, 0.0, [0, 0]);

% mac
Xd = 1.6;
Xdp = 0.32;
Xq = 1.59;
Tdo = 6.0;
M = 100;
d = 2;
mac = table(Xd, Xdp, Xq, Tdo, M, d);

% exc
Ka = 2.0;
Te = 0.05;
exc = table(Ka, Te);

% pss
Kpss = 200;
Tpss = 10;
TL1p = 0.05;
TL1 = 0.015;
TL2p = 0.08;
TL2 = 0.01;
pss = table(Kpss, Tpss, TL1p, TL1, TL2p, TL2);

net.bus{1}.add_component(generator_AGC(mac, exc, pss));

%% generator
net.bus{2} = bus_PV(1.0, 1.7, [0, 0]);

% mac
Xd = 1.6;
Xdp = 0.23;
Xq = 1.59;
Tdo = 6.0;
M = 18;
d = 2;
mac = table(Xd, Xdp, Xq, Tdo, M, d);

% exc
Ka = 2.0;
Te = 0.05;
exc = table(Ka, Te);

% pss
Kpss = 200;
Tpss = 10;
TL1p = 0.05;
TL1 = 0.015;
TL2p = 0.08;
TL2 = 0.01;
pss = table(Kpss, Tpss, TL1p, TL1, TL2p, TL2);

net.bus{2}.add_component(generator_AGC(mac, exc, pss));
%% load
net.bus{3} = bus_PQ(-1.25, -0.5, [0, 0]);
net.bus{3}.add_component(load_varying_impedance())
```

## 自作した電力系統の応答のシミュレーション

ここで，自作したシステムに対し地絡を加えたシミュレーションを実行します．以下がそのコード例です．

```matlab
option = struct();
option.fault = {{[0, 0.01], 1}, {[10, 10.01], 2}};

out = net.simulate([0, 100], option);
```
ここでは0秒から0.01秒の間と10秒から10.01秒の間にそれぞれ地絡をくわえます．

例として２つ目のgeneratorのシミュレーション結果は以下のようになります．

![](/Figures/Tuto_text_result1.png)

## 制御シミュレーション

power_simulatorで用意している制御器は以下のような様々なものがあります．

- [controller_broadcast_PI_AGC](path_to_doc_controller_broadcast_PI_AGC)
- [controller_broadcast_PI_AGC_normal](path_to_doc_controller_broadcast_PI_AGC_normal)
- [controller_LQR](path_to_doc_controller_LQR)
- [controller_retrofit_generator_UKF](path_to_doc_controller_retrofit_generator_UKF)
- [controller_retrofit_generator_UKF_LQR](path_to_doc_controller_retrofit_generator_UKF_LQR)
- [controller_retrofit_LQR](path_to_doc_controller_retrofit_LQR)

本チュートリアルにおいては[controller_broadcast_PI_AGC_normal](path_to_doc_controller_broadcast_PI_AGC_normal)を用いて制御シミュレーションを行います．地絡などは先程と同じ条件で以下のように制御器をくみこみます．

```matlab
cg = controller_broadcast_PI_AGC_normal(net, [2], [2], -10, -5000);
net.add_controller_global(cg)
```

このプログラムの２つ目のgeneratorのシミュレーション結果は以下のようになります．

![](/Figures/Tuto_text_result2.png)

## docを参照している部分
```
[hoge](path_to_doc_hoge)
```
というかんじで未完成のdocを参照している部分が多々ありあます．docが完成したあとこの部分を書き換えていただけると有り難いです．