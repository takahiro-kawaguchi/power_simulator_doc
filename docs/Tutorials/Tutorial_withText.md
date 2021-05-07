# Tutorial

<div style="text-align: center;">
<img src="/Figures/tuto-withText.jpg" width=60%;>
</div>

このチュートリアルではテキストの内容に沿って電力系統システムを自分で定義し，その制御シミュレーションを行う方法を解説します．  

- テキストの第１章で扱われていた3busシステムを定義する。
- 各コンポーネントに実際に発電機や負荷を設置し、具体的なパラメータを代入する。
- 定義した電力モデルの時間応答を解析したり、コントローラを負荷して解析を行う。  

といった流れで進めていこうと思います。

## __対象となるシステムの設定__

本チュートリアルにおいては以下の図ような単純な電力系統システムを自作します．

![](/Figures/write_3bus.png)

この電力系統システムでは３つのバスと機器が繋がっているシステムです．  
ここで上の３busシステムをシュミレータ上で定義するにあたり、一度情報を表にして以下にまとめてみます。(<span style="font-size: 100%; color: red;">__赤字の各パラメータの値は適当に決めています。__</span>)

#### バスの情報
図からも分かるように、このシステムは３つのバスによって構成されています。

|バス番号|潮流計算のための各バスの設定値|バスの種類|
|:---:|:---:|:---:|
|バス１|<span style="font-size: 100%; color: red;">｜V｜ =1.0 , ∠V＝0.0 </span>|slackバス|
|バス２|<span style="font-size: 100%; color: red;"> P = 1.0 , ｜V｜=1.7 </span>|PVバス|
|バス３|<span style="font-size: 100%; color: red;"> P = -1.25 , Q = -0.5 </span>|PQバス|

表中のP、Q、|V|、∠V はそれぞれ「有効電力」「無効電力」「電圧の大きさ」「電圧の偏角」を指しています。これに関しては[電力ネットワークの解説ページ](intro_net.md)でも触れているので参考にして下さい。

#### ブランチの情報
このシステムではバス間をつなぐブランチは2本あることが分かります。

|ブランチが接続している<br>バス|ブランチ上の抵抗や対地静電容量</br>によるインピーダンス|位相調整変圧機<br>のパラメータ|
|:---:|:---:|:---:|
|バス１ーバス２|<span style="font-size: 100%; color: red;"> x = 0.0576j </span>|<span style="font-size: 100%; color: red;">τ=1.0, θ＝0.0</span>|
|バス３ーバス２|<span style="font-size: 100%; color: red;"> x = 0.0625j </span>|<span style="font-size: 100%; color: red;">τ=1.0, θ＝0.0</span>|

標柱の<span style="font-size: 140%; color: green;">xは〜〜〜を表しています。</span>  
τとθは以下の解説では`tap`と`phase`という表記になっています。

#### 発電機バスに付加されている同期発電機モデルの情報

今回のシステムでバス１とバス２が発電機バス(slackバスとPVバス)であるためパラメータ設定する発電機の個数は２つである。

|発電機を付加する<br>バス番号|q軸/d軸の</br>同期リアクタンス|d軸の</br>回路時定数|慣性定数|制動係数|
|:---:|:---:|:---:|:---:|:---:|
|バス１|<span style="color: red;"> Xq =1.59 ,</br> Xd =1.6 , Xd'=0.32 </span>|<span style="color: red;">τｄ =6.0 </span>|<span style="color: red;">M =100 </span>|<span style="color: red;">D =2 </span>|
|バス２|<span style="color: red;"> Xq =1.59 ,</br> Xd =1.6 , Xd'=0.23 </span>|<span style="color: red;">τｄ =6.0 </span>|<span style="color: red;">M =18 </span>|<span style="color: red;">D =2 </span>|

表の各変数の記号はテキストと同じ様にしましたが、シュミレータ内では  
<div style="text-align: center;">Xd'→ Xdp　、　τｄ→ Tdo　、　D→ d</div>  
という変数名になっています。  
なお、発電機を円筒形にしたい場合は、`Xdp`に`Xq`と同じ値を入れます。

#### 発電機に付加されている制御器の情報(AGC,PSSなど)

一般に世の中で稼働している発電所の発電機はAGC,やAVR,PSSなどの制御機が内蔵されています。<span style="color: green;">(ほんと？？)</span>

本シュミレータでは後にも実行の仕方を触れますが、パラメータを引数としてAGCなどを内蔵した発電機を定義する関数`generator_AGC`という関数があります。その制御器内のゲイン等の値を設定する必要があります。  
制御器のパラメータのデータは１発電機に１つあるため、今回のシステムでは２つ設定する必要があります。

|制御機を付加する発電機が</br>接続してるバス番号|Ka|Te|Kpss|Tpss|TL|
|:---:|:---:|:---:|:---:|:---:|:---|
|バス１|<span style="color: red;">Ka = 2.0</span>|<span style="color: red;">Te = 0.05</span>|<span style="color: red;">Kpss = 200</span>|<span style="color: red;">Tpss = 10</span>|<span style="color: red;">TL1 = 0.015 , TL1'= 0.05</br>TL2 = 0.01 , TL2'= 0.08</span>|
|バス２|<span style="color: red;">Ka = 2.0</span>|<span style="color: red;">Te = 0.05</span>|<span style="color: red;">Kpss = 200</span>|<span style="color: red;">Tpss = 10</span>|<span style="color: red;">TL1 = 0.015 , TL1'= 0.05</br>TL2 = 0.01 , TL2'= 0.08</span>|

<span style="font-size: 140%; color: green;">この表の変数が何を指しているのか分からなかったです。</span>
  
といったように先に紹介した3busシステムでもこれだけの情報が割り当てられています。  
それでは実際に以下にこれらの情報をもとにシュミレータ内で3busシステムを定義していきましょう。

## __電力系統システムの定義__

全ての電力系統システムは`power_network`クラスを用いて実装されます．以下のようにして電力系統クラスを定義します．

```matlab
net = power_network();
```

イメージでいうと、空のテンプレート表のようなものを変数`net`にあてはめており、これからこの表に機器の情報やブランチ・バスの情報を書き込んでいくための準備のようなプロセスです。

### __送電網の定義__

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

### __バス__

#### <u>Slackバス</u>

slackバス(swingバス)とは[潮流計算](https://en.wikipedia.org/wiki/Power-flow_study)のため特別な発電機バスです．

```matlab
net.bus{1} = bus_slack(1.0, 0.0, [0, 0]);
```

引数・各パラメーターについては[bus_slack](path_to_doc_bus_slack)を参照してください．

#### <u>Generatorバス</u>

Generatorバスとは発電機(Generator)を接続するためのバスです．プログラム上では以下のように

```matlab
net.bus{2} = bus_PV(1.0, 1.7, [0, 0]);
```
引数・各パラメーターについては[bus_PV](path_to_doc_bus_PV)を参照してください．

#### <u>Loadバス</u>

Loadバスとは負荷を接続するためのバスです．プログラム上では以下のように

```matlab
net.bus{3} = bus_PQ(-1.25, -0.5, [0, 0]);
```
引数・各パラメーターについては[bus_PQ](path_to_doc_bus_PQ)を参照してください．

### __機器__

機器を定義し，先程の定義したbusに接続します．プログラム上ではi番目のバスに機器を接続するときは

```matlab
net.bus{i}.add_component(machine);
```
のようにします．

#### <u>generator</u>
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

#### <u>load</u>

power_simulator内には以下の4つのloadが用意されています．

- [load_const_impedance](path_to_load_const_impedance)
- [load_const_power](path_to_load_const_power)
- [load_varying_impedance](path_to_load_varying_impedance)
- [load_varying_power](path_to_load_varying_power)

本チュートリアルにおいては，[load_varying_impedance](path_to_load_varying_impedance)を用います．

```
net.bus{3}.add_component(load_varying_impedance())
```

## __電力系統の自作のコードの全体__

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

## __自作した電力系統の応答のシミュレーション__

ここで，自作したシステムに対し地絡を加えたシミュレーションを実行します．以下がそのコード例です．

```matlab
option = struct();
option.fault = {{[0, 0.01], 1}, {[10, 10.01], 2}};

out = net.simulate([0, 100], option);
```
ここでは0秒から0.01秒の間と10秒から10.01秒の間にそれぞれ地絡をくわえます．

例として２つ目のgeneratorのシミュレーション結果は以下のようになります．

![](/Figures/Tuto_text_result1.png)

## __制御シミュレーション__

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

## __docを参照している部分__
```
[hoge](path_to_doc_hoge)
```
というかんじで未完成のdocを参照している部分が多々ありあます．docが完成したあとこの部分を書き換えていただけると有り難いです．