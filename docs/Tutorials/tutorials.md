# Tutorials

## **power_simulatorの構成**
チュートリアルに進む前にここでpower_simulatorの全体構成を示しておきます。チュートリアルを進めていく中や作業中に自身の使っている関数が何をするためのコマンドかわからなくなった際に目次代わりに利用してください。

```mermaid
graph LR

net{power_network.m}---インスタンス
net---内蔵関数
net---変数
click net "http://google.com/"

%%電力系統の定義（既存モデル）
インスタンス---network_68bus
インスタンス---network_70bus
インスタンス---network_9bus
subgraph power_simulator内に既存のネットワークモデル
    インスタンス
    network_68bus
    network_70bus
    network_9bus
end


%%シュミレーション
内蔵関数---simulate
click simulate "./step1.md"
%%うまくファイルのリンクが起動しない
内蔵関数---get_sys
subgraph シュミレーション
    simulate
    get_sys
end


%% コントローラの設定関連
内蔵関数---add_controller_global
内蔵関数---remove_controller_global
内蔵関数---add_controller
内蔵関数---remove_controller
subgraph コントローラの追加/削除
    add_controller_global
    add_controller
    remove_controller_global
    remove_controller
end
add_controller_global==設計==>controller
add_controller==設計==>controller{controller.m}
controller---conイン[インスタンス]
conイン---削除予定controller_broadcast_PI
conイン---controller_broadcast_PI_AGC
conイン---controller_broadcast_PI_AGC_normal
conイン---controller_LQR
conイン---controller_retrofit_generator
conイン---controller_retrofit_generator_nonlinear
controller_retrofit_generator_nonlinear---controller_retofit_type1
conイン---controller_retrofit_generator_nonlinear_AGC_LQR
conイン---controller_retrofit_generator_nonlinear_UKF
controller_retrofit_generator_nonlinear_UKF---controller_retrofit_generator_nonlinear_AGC_LQR_UKF
controller---con関数[内蔵関数]
con関数---controller_get_dx_u[get_dx_u]
con関数---controller_get_dx_u_linear[get_dx_u_linear]
con関数---controller_get_nx[get_nx]
con関数---controller_get_linear_matrix[get_linear_matrix]

subgraph コントローラの設計/controller.mの子クラス
    conイン
    削除予定controller_broadcast_PI
    controller_broadcast_PI_AGC
    controller_broadcast_PI_AGC_normal
    controller_LQR
    controller_retrofit_generator
    controller_retrofit_generator_nonlinear
    controller_retofit_type1
    controller_retrofit_generator_nonlinear_AGC_LQR
    controller_retrofit_generator_nonlinear_UKF
    controller_retrofit_generator_nonlinear_AGC_LQR_UKF
end
subgraph コントローラを自作する際に必要な抽象メソッド
    con関数
    controller_get_dx_u[get_dx_u]
    controller_get_dx_u_linear[get_dx_u_linear]
    controller_get_nx[get_nx]
    controller_get_linear_matrix[get_linear_matrix]
end


%%電力系統の設計
subgraph 電力系統の自作する際に操作する変数
    bus
    変数
    branch
end

%%　電力系統の設計（バスに関して）
変数---bus
bus==設定==>busm{bus.m}
busm---busイン[インスタンス]
busイン---bus_slack
busイン---bus_PV
busイン---bus_non_unit
busイン---bus_PQ
変数---branch
subgraph バスを定義する関数/bus.mの子クラス
    busイン
    bus_slack
    bus_PV
    bus_non_unit
    bus_PQ
end

%%　電力系統の設計（機器に関して）
busm---add_component
subgraph 機器情報を追加する関数
    add_component
end
add_component==設計==>component{component.m}
component---comイン[インスタンス]
comイン---component_empty
comイン---generator_AGC
comイン---load_varying_impedance
load_varying_impedance---load_const_impedance
comイン---load_varying_power
load_varying_power---load_const_power
comイン---solor_farm
comイン---wind_farm
component---com関数[内蔵関数]
com関数---initialize
com関数---get_nx
com関数---get_nu
com関数---get_dx_I
com関数---get_linear_matrix
com関数---get_dx_I_linear

subgraph 機器を自作する際に必要な抽象メソッド
    com関数
    initialize
    get_nx
    get_nu
    get_dx_I
    get_linear_matrix
    get_dx_I_linear
end
subgraph 機器の設計/component.mの子クラス
    comイン
    component_empty
    generator_AGC
    load_varying_impedance
    load_const_impedance
    load_varying_power
    load_const_power
    solor_farm
    wind_farm
end
```

***

初めて利用する方向けのチュートリアル  
メソッドやクラスなどの詳しい説明は [Docs](../Docs/docs.md)へ

## [Step1（既存の系統モデルのシミュレーション）](./step1.md)

- 対象者：制御工学についての知識はあるが，電力系統については知識がない技術者
- できるようになること：
    - 既存の電力系統モデルに対して，初期値応答・外乱応答・入力応答などのシミュレーションを実行する

## [Step2（線形化したシステムを使う）](./step2.md)

- 対象者：制御工学の技術者
- できるようになること：
    - 線形化したシステムでのシミュレーションを行う
    - 線形化したシステムの状態空間表現を取得する

## [Step3（制御器の導入）](./step3.md)

- 対象者：レトロフィット制御の論文を読み，実際にシミュレーションを行いたい技術者
- できるようになること：
    - システムに既存のコントローラを付加してシミュレーションを行う
    - 既存のコントローラを付加されたシステムの状態空間表現を取得する

## [Step4（電力系統の自作）](./step4.md)

- 対象者：シミュレーション用の電力系統を自作したい技術者
- できるようになること：
    - 電力系統の自作
        - バスの定義
        - ブランチの定義
        - 機器の定義

## [Step5（機器の自作）](./step5.md)

- 対象者：既存の種類以外の機器を使用したい技術者
- できるようになること：
    - 機器の自作

## [Step6（制御器の自作）](./step6.md)

- 対象者：既存の種類以外の制御器を使いたい技術者
- できるようになること：
    - 制御器の自作

## おまけ

- レトロフィット制御器の自作
- 電力系統のシステム同定
