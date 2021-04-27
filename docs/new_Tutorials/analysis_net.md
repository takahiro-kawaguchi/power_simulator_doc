<img src="/Figures/index-2.jpg" width=100%;>

# <div style="text-align: center;"><span style="font-size: 130%; color: black;">電力ネットワークの解析</span></div>

***
前の章では電力ネットワークを定義し、その情報を変数`net`に格納する所までできたと思います。
本章では、その変数`net`をクラス内でメソッドとして定義されている関数を用いて、シュミレーションしていきます。  
  
<br>
<span style="font-size: 125%; color: black;">__本章を始めるにあたって用意するもの：`電力ネットワークの情報を格納した変数net`__</span>  
  
<br>
まだ変数`net`を定義していなくて、取り敢えず解析をしてみたいという方は「電力ネットワークの作成編」の【既存のモデルを使う】の章で書かれているインスタンスを用いる方法が良いかと思います。  

```matlab
%サンプルコード
net = network_9bus;  %9busモデルの情報をnetに格納する
net = network_68bus; %68busモデルの情報をnetに格納する
net = network_70bus; %70busモデルの情報をnetに格納する

```

## <span style="font-size: 100%; color: black;">【定義した電力モデルのシュミレーション】</span>
- 基本的なシュミレーションの仕方
- オプションの設定の仕方。(入出力応答・初期値応答・外乱応答などの解析の実行)
- シュミレーション結果をグラフとして表示する。  
  <span style="font-size: 140%; color: green;">↑主にSTEP1の内容を貼り付ける</span>

## <span style="font-size: 100%; color: black;">【定義した電力モデルの線形化】</span>
- 線形化したシステムの状態空間表現を得る。
- 線形化したシステムのシュミレーションを実行する。  
  <span style="font-size: 140%; color: green;">↑主にSTEP２の内容を貼り付ける</span>

---
<div style="text-align: center;">
```mermaid
graph TB
作成(電力ネットワークの構成編のページへ)
解析(電力ネットワークの作成編のページへ)
style 作成 fill:#fff,stroke:#000,stroke-width:1px
style 解析 fill:#fff,stroke:#000,stroke-width:1px
click 作成 "http://127.0.0.1:8000/new_Tutorials./make_net/"
click 解析 "/analysis_net.md"
```
</div>