# （準備中）バスに接続する機器について

[]( power_networkのリンクを入れる場所は"TODO_link" を挿入しておく )

## クラスの全体像

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
<font size=3>([component.m]())</font> [](TODO_link)

全てのComponentクラスの基底クラス．  


## component_empty
<font size=3>([component_empty.m]())</font> [](TODO_link)




## generator_AGC
<font size=3>([generator_AGC.m]())</font> [](TODO_link)


## generator
<font size=3> ([generator.m]())</font> [](TODO_link)


## load_varying_impedance
<font size=3>([load_varying_impedance.m]())</font> [](TODO_link)


## load_const_impedance
<font size=3>([load_const_impedance.m]())</font> [](TODO_link)


## load_varying_power
<font size=3>([load_varying_power.m]())</font> [](TODO_link)


## load_const_power
<font size=3>([load_const_power.m]())</font> [](TODO_link)


## solar_farm
<font size=3>([solar_farm.m]())</font> [](TODO_link)

風力発電機の実装（ ***component*** クラスの派生クラス）  
<font size=5 color="red">(削除 or 要説明追加)</font>

## wind_farm
<font size=3>([wind_farm.m]())</font> [](TODO_link)

風力発電機の実装（ ***component*** クラスの派生クラス）  
<font size=5 color="red">(削除 or 要説明追加)</font>
