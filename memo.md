
# やったことメモ


## OpenEmuでゲームを動かす

できた



## デスクトップでキャプチャしてopencvに読み込ませる

できた


## pythonからkeyboardを入力する

pyguiautoというライブラリがあって、それを使うとできた



## opencvを使って画像から道路を認識する

## opencvを使って画像からアイテムを認識する

## channer rnnを触ってみる


## マリオカートの環境とエージェントについて

よくわからんくなってきたぞ

[ChainerRLで三目並べを深層強化学習（Double DQN）してみた](http://qiita.com/uezo/items/87b25c93199d72a56a9a)

これが参考になるかも。


とりあえず中の意味はよくわからんけど、マリオカートの情報を当てはめるとして

* 前提
  * レースはじまるまでは人が操作
* 環境のリセット
  * やりなおし
* 実行
  * これが操作性強いゲームだと難しいのでは？と思った
    * accelerator
    * 左 + accelerator
    * 右 + accelerator
    * 左 + jump
    * 右 + jump
    * アイテムを使う
    * back
    * 左 + back
    * 右 + back
* 勝利判定
  * まぁまずはゴールするところまで
  * ゴールしたら視点がかわるのでそれで判断します
* 報酬
  * 正しい方向へ進む
  * 逆走
    * ジュゲムがなんか持っているので判断？
  * 道じゃないところを走る
  * 壁にぶつかる
  * 邪魔ものにあたる
  * 崖、池に落ちる
* ランダムうち？
  * 適当にコントロールせよってこと？
  * jumpとアクセルをランダムにする？
* エージェントでダレ？
  * 多分プレイヤーのこと
* ゲームシーンがある
  * まだスタートしていない
  * レーシング中
  * ゴール 

## キャプチャが遅いので低レイヤーの言語で試す

Boost Pythonというのが存在するとか

```sh
$ brew install boost-python --with-python3
```


```sh
$ export CPLUS_INCLUDE_PATH=$HOME.pyenv/versions/anaconda3-2.3.0/include/python3.4m
$ g++ -I`python -c 'from distutils.sysconfig import *; print(get_python_inc())'` -DPIC -bundle -fPIC -o basic.so basic.cpp -lboost_python  -framework Python
```


エラー

```
Undefined symbols for architecture x86_64:
  "boost::python::detail::init_module(PyModuleDef&, void (*)())", referenced from:
      _PyInit_basic in basic-578ae8.o
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
```

[Unable to link against Boost.Python on OS X](http://stackoverflow.com/questions/33653001/unable-to-link-against-boost-python-on-os-x)

>The solution I am currently using is to reinstall boost-python without python 2.7 support

ほう...


```sh
$ brew uninstall boost-python
$ brew install boost-python --with-python3 --without-python
```


```sh
$ g++ -I`python -c 'from distutils.sysconfig import *; print(get_python_inc())'` -DPIC -bundle -fPIC -o basic.so basic.cpp -lboost_python -framework Python
```

```
ld: library not found for -lboost_python
clang: error: linker command failed with exit code 1 (use -v to see invocation)
```

orz

ググったがよくわからんくなってきたぞ。やけくそになる。

```sh
$ g++ -I`python -c 'from distutils.sysconfig import *; print(get_python_inc())'` -DPIC -bundle -fPIC -o basic.so basic.cpp -lboost_python3
```

```
Undefined symbols for architecture x86_64:
  "_PyLong_FromLong", referenced from:
      boost::python::to_python_value<int const&>::operator()(int const&) const in basic-4f6997.o
  "_PyLong_Type", referenced from:
      boost::python::to_python_value<int const&>::get_pytype() const in basic-4f6997.o
  "__Py_NoneStruct", referenced from:
      boost::python::api::object::object() in basic-4f6997.o
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
```

ほぅ。。。エラー内容が変わった。

```sh
$ g++ -I`python -c 'from distutils.sysconfig import *; print(get_python_inc())'` -DPIC -bundle -fPIC -o basic.so basic.cpp -lboost_python3 -framework Python
```


できた！


しかし、謎のエラーが発生するようになった


```sh
$ python
Python 3.4.4 |Anaconda 2.3.0 (x86_64)| (default, Jan  9 2016, 17:30:09)
[GCC 4.2.1 (Apple Inc. build 5577)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import basic
>>> dir(basic)
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'add_int', 'hello', 'hello_char']
>>> basic.add_int(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __repr__ returned non-string (type str)
>>> basic.add(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __repr__ returned non-string (type str)
>>> basic.hello()
'hello!'
>>> basic.hello_char()
'hello!'
```


謎。stack overflowに質問投げた。
