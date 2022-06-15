# markdown基本操作

## 字体样式  
*斜体*  
**斜体加粗**  
<u>下划线</u>  
~~删除线~~
***
## 序号
* 无序列表  
1. 有序列表    
    * 列表嵌套
2. 有序列表
    * 列表嵌套
***
## 区块
> 区块引用    
>> 第一层嵌套  
>>> 第二层嵌套

> 区块中使用列表  
> 1. 有序列表
> * 无序列表  
1. 列表中使用区块
    > 区块1  
    > 区块2

***
## 代码  
`main()`函数

    <?php  
    echo 'markdown';  
    function test(){  
    echo 'test';  
    }
  
```javascript
$(document).ready(function(){
  alert('markdown');  
});
```
***
## 链接
链接的使用 [点击](https://www.baidu.com)

<https://www.baidu.com>

百度网站[baidu][B]  
google网站[google][R]

[B]: https://www.baidu.com
[R]: http://www.google.cn/

***
## 表格
|左对齐|居中|右对齐|
|:---|:---:|---:|
|单元|单元|单元|
|单元|单元|单元|
***
## 希腊语
|符号|表示方式|
|:---:|:---:|
|$$\alpha$$|\alpha|
|$$\gamma$$|\gamma|
|$$\pi$$|\pi|
|$$\Pi$$|\Pi|
|$$\phi$$|\phi|
|$$\varphi$$|\varphi|
|$$\varPhi$$|\varPhi|
|$$\theta$$|\theta|
***
## 数学函数
|符号|表示方式|
|:---:|:---:|
|$$f(x)=sin(x)+12$$|f(x)=sin(x)+12|
|$$\sum_{n=1}^{100} n$$|\sum_{n=1}^{100} n|
|$$n^2$$|n^2|
|$$k_n^2$$|k_n^2|
|$$\frac{3}{4}$$|\frac{3}{4}|
|$$\sum_{n=1}^N{3x^n}$$|\sum_{n=1}^N{3x^n}|
|$$\prod{3x^n}$$|\prod{3x^n}|
|$$\prod_{n=1}^N{3x^n}$$|\prod_{n=1}^N{3x^n}|
|$$\sqrt{4}$$|\sqrt{4|
|$$\int^5_1{f(x)}{\rm d}x$$|\int^5_1{f(x)}{\rm d}x|
|$$\iint^5_1{f(x+1)}{\rm d}x$$|\iint^5_1{f(x+1)}{\rm d}x|
***
## 运算符
|符号|表示方式|
|:---:|:---:|
|$$\lim$$|\lim|
|$$\exp$$|\exp|
|$$\to$$|\to|
|$$\bmod$$|\bmod|
|$$\equiv$$|\equiv|
|$$+\infty$$|+\infty|
|$$-\infty$$|-\infty|
|$$\geq$$|\geq|
|$$\leq$$|\leq|
|$$\subset$$|\subset|
|$$\supset$$|\supset|
|$$\in$$|\in|
|$$\pm$$|\pm|
|$$\mp$$|\mp|
|$$\cdot$$|\cdot|
|$$\times$$|\times|
|$$\div$$|\div|
|$$\not=$$|\not=|
|$$\not<$$|\not<|
|$$\not\supset$$|\not\supset|
|$$\prod$$|\prod|
|$$\coprod$$|\coprod|
|$$\bigoplus$$|\bigoplus|
|$$\bigotimes$$|\bigotimes|
|$$\bigodot$$|\bigodot|
|$$\bigcup$$|\bigcup|
|$$\bigcap$$|\bigcap|
|$$\bigsqcup$$|\bigsqcup|
|$$\bigvee$$|\bigvee|
|$$\bigwedge$$|\bigwedge|
|$$a''$$|a''|
|$$\hat{a}$$|\hat{a}|
|$$\bar{a}$$|\bar{a}|
|$$\grave{a}$$|\grave{a}|
|$$\dot{a}$$|\dot{a}|
|$$\ddot{a}$$|\ddot{a}|
|$$\not{a}$$|\not{a}|
|$$\not={a}$$|\not={a}|
|$$\overrightarrow{AB}$$|\overrightarrow{AB}|
|$$\overline{aaa}$$|\overline{aaa}|
|$$\underline{aaa}$$|\underline{aaa}|
|$$\vec{a}$$|\vec{a}|
|$$\color{red}{x}$$|\color{red}{x}|
|$$\int y{\rm d}x$$|\int y{\rm d}x|
|$$\dots$$|\dots|
|$$\vdots$$|\vdots|
|$$\ddots$$|\ddots|
***
## 三角函数
|符号|表示方式|
|:---:|:---:|
|$$\log_2{18}$$|\log_2{18}|
|$$\ln2$$|\ln2|
|$$\bot$$|\bot|
|$$\angle$$|\angle|
|$$45^\circ$$|45^\circ|
|$$\sin\frac{\pi}{2}$$|\sin\frac{\pi}{2}|
|$$\cos$$|\cos|
|$$\tan$$|\tan|
|$$\leftarrow$$|\leftarrow|
|$$\rightarrow$$|\rightarrow|
|$$\longrightarrow$$|\longrightarrow|
|$$\uparrow$$|\uparrow|
|$$\downarrow$$|\downarrow|
***
## 线性方程
$$
\begin{Bmatrix}
a&b\\
c&d
\end{Bmatrix}
$$

$$
\begin{bmatrix}
x_{00} & x_{01} & \dots & x_{0n}\\
x_{10} & x_{11} & \dots & x_{1n}\\
\vdots & \vdots & \ddots & \vdots\\
x_{m0} & x_{m1} & \dots & x_{mn}
\end{bmatrix}
$$

$$
\mathbf{x}=
\begin{bmatrix}
x_{1}& \color{red}{x}_{2} & \cdots & x_{n}
\end{bmatrix}
$$

$$
\mathbf{x}=
\begin{bmatrix}
x_{1} \\ 
\color{red}{x}_{2} \\
\vdots \\
x_{n}
\end{bmatrix}
$$

$$
\begin{CD}
A @>a>> B \\
@VbVV @AAcA\\
C @= D
\end{CD}
$$
***
## 其他
|符号|表示方式|
|:---:|:---:|
|$$[a]$$|[a]|
|$$\lang f \rang$$|\lang f \rang|
|$$\lfloor f \rfloor$$|\lfloor f \rfloor|
|$$\lceil f \rceil$$|\lceil f \rceil|
|$$\ulcorner f \urcorner$$|\ulcorner f \urcorner|