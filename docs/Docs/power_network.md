# （準備中）電力系統モデルについて

## power_network

[@power_network/power_network.m]()

全ての電力系統モデルの基底クラス．  


## network_68bus

[network_68bus.m]()

IEEE 68bus 16machine システムの実装．  
発電機として[generator](/Docs/component/#generator)を，負荷として[load_const_impedance](/Docs/component/#load_const_impedance), [load_const_power](/Docs/component/#load_const_power), [load_random_power](/Docs/component/#load_random_power)を導入したネットワークである．  
ネットワーク定義の際に `net=network_68bus(load_type)`のように定義する．ここで，load_typeには1~2を代入する．負荷には，1の場合は[load_const_impedance](/Docs/component/#load_const_impedance)，2の場合は[load_const_power](/Docs/component/#load_const_power)を導入する．引数が省略されている場合は[load_const_impedance](/Docs/component/#load_const_impedance)を負荷として導入する．[](現状、load_typeには1~3が代入できるが、3は今後削除予定なので省略した)  


## network_68bus_AGC_const_power

[network_68bus_AGC_const_power1.m]()

IEEE 68bus 16machine システムの実装．  
発電機として[generator_AGC](/Docs/component/#generator_agc)を，負荷として[load_const_impedance](/Docs/component/#load_const_impedance), [load_varying_power](/Docs/component/#load_varying_power)を導入したネットワークである．


## network_68bus_AGC_varying_impedance

[network_68bus_AGC_varying_impedance.m]()

IEEE 68bus 16machine システムの実装．  
発電機として[generator_AGC](/Docs/component/#generator_agc)を，負荷として[load_varying_impedance](/Docs/component/#load_varying_impedance)を導入したネットワークである．

## network_68bus_const_power

[network_68bus_const_power.m]()

IEEE 68bus 16machine システムの実装．  
発電機として[generator](/Docs/component/#generator)を，負荷として[load_const_impedance](/Docs/component/#load_const_impedance), [load_varying_power](/Docs/component/#load_varying_power)を導入したネットワークである．  
一部のバスに[load_varying_power](/Docs/component/#load_varying_power)の負荷を，その他全てのバスに[load_const_impedance](/Docs/component/#load_const_impedance)の負荷を導入している（フォルト時の計算を可能にするため）


## network_70bus

[network_70bus.m]()

定本さんの論文(magazine)における風力発電機を含んだ電力ネットワーク．
