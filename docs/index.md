# 電力系統に対するレトロフィット制御シミュレータ

本サイトはpower_simulator の公式ドキュメントです.  
### <span style="font-size: 130%; color: black;">power_simulatorとは？</span>
power_simulatorは、各人で電力系統システムの設計・解析するために作られたMATLAB言語のツールです。  
具体的には、解析したい電力ネットワークを定義し、その初期応答や外乱応答、線形化システムの導出などの解析を行うことで、落雷などによって地絡が起きた際の状態やコントローラを新しく設計し導入した時の安定・不安定を解析するなど様々な状況を想定した解析を補助します。  
power_simulatorを制作する背景に使われている数理モデル等は「**参考書：電力システム制御理論**」の内容に即しており、こちらで紹介された理論をもとに構築されたものとなっております。理論に基づいてシュミレーションを進めて行きたい方は参考書の内容にそれぞれ対応付けながら進めていただくと分かりやすいかと思います。テキストに即したTutorialは[[こちら](←久木くんが作ってくれたファイル)]()  
  
### <span style="font-size: 130%; color: black;">power_simulatorを使うためのステップ</span>
power_simulatorで解析するには大きく分けて２つのステップがあります。
<div style="text-align: center;">
```mermaid
graph LR
作る((電力システム<br>を定義する))
作る-->解析((電力システム<br>を解析する))
```
</div>
以下に各ステップごとに説明していきます。
  
<div style="text-align: center;">
<span style="font-size: 180%; color: black;">【電力システムって何で構成されてるの？ click↓】</span></div>
[<img src="/Figures/index-3.jpg" width=100%; style="border: 3px pink solid;">](new_Tutorials/intro_net.md)
  
<div style="text-align: center;">
<span style="font-size: 180%; color: black;">【電力システムを作成/定義する click↓】</span></div>
[<img src="/Figures/index-1.jpg" width=100%; style="border: 3px pink solid;">](new_Tutorials/make_net.md)
  
<div style="text-align: center;">
<span style="font-size: 180%; color: black;">【作成した電力システムを解析する click↓】</span></div>
[<img src="/Figures/index-2.jpg" width=100%; style="border: 3px pink solid;">](new_Tutorials/analysis_net.md)

## Contents

- [Tutorials](./Tutorials/tutorials.md)  
    初めて利用する方向けのチュートリアル
- [Docs](./Docs/docs.md)  
    既存のメソッドやクラスについての情報集

## Require

- Optimization Toolbox
- Control System Toolbox
- Robust Control Toolbox