# （準備中）バスについて

[]( power_networkのリンクを入れる場所は"TODO_link" を挿入しておく )

## クラスの全体像(再掲)

まずはバスに関するクラスの全体像を示します。

[](TODO_link→以下の図のリンクを正しいリンクへ変更)
```mermaid
graph LR

base{power_simulator}---bus

bus---bus_non_unit
bus---bus_PQ
bus---bus_PV
bus---bus_slack

click base "https://www.google.com/"
click bus "https://www.google.com/"
click bus_non_unit "https://www.google.com/"
click bus_PQ "https://www.google.com/"
click bus_PV "https://www.google.com/"
click bus_slack "https://www.google.com/"
```

## bus

[bus.m]()

全てのBusクラスの基底クラス．  


## bus_non_unit

[bus_non_unit.m]()

non-unit Busの実装．  


## bus_PQ

[bus_PQ.m]()

PQ Busの実装．  

## bus_PV

[bus_PV.m]()

PV Busの実装．  

## bus_slack

[bus_slack.m]()

slack (swing) Busの実装．  
