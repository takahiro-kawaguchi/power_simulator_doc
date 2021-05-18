# （準備中）バスに接続する機器について

[]( power_networkのリンクを入れる場所は"TODO_link" を挿入しておく )

## クラスの全体像(再掲)

まずは機器に関するクラスの全体像を示します。

[](TODO_link→以下の図のリンクを正しいリンクへ変更)
```mermaid
graph LR

base{power_simulator}---component

component---component_empty
component---generator_AGC
generator_AGC---generator
component---load_varying_impedance
load_varying_impedance---load_const_impedance
component---load_varying_power
load_varying_power---load_const_power
component---solar_farm
component---wind_farm

click base "https://www.google.com/"
click component "https://www.google.com/"
click component_empty "https://www.google.com/"
click generator_AGC "https://www.google.com/"
click generator "https://www.google.com/"
click load_varying_impedance "https://www.google.com/"
click load_const_impedance "https://www.google.com/"
click load_varying_power "https://www.google.com/"
click load_const_power "https://www.google.com/"
click solar_farm "https://www.google.com"
click wind_farm "https://www.google.com"
```

## component

[component.m]()

全てのComponentクラスの基底クラス．  

## component_empty

[component_empty.m]()


## generator_AGC

[gennerator_AGC.m]()


### generator

[generator.m]()


## load_varying_impedance

[load_varying_impedance.m]()


### load_const_impedance

[load_const_impedance.m]()


## load_varying_power

[load_varying_power.m]()


### load_const_power

[load_const_power.m]()


## solar_farm

[solar_farm.m]()


## wind_farm

[wind_farm.m]()

