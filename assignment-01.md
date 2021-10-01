

# CMPS 2200 Assignment 1

**Name:**________Raphael Mahari_________________


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. **Asymptotic notation**

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 

.  2^{n+1} <= (2^n)
  make c = 2 and n= anything
  2^{n+1} <= 2(2^n) 
  == 2^{n+1} <= (2^{n+1})
  therefore yes as they are the same if n = 1 then 
.  2^{1+1} <= (2^{1+1})
4 = 4 
.  
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  $2^{2^n} <= O(2^n)$
 .  
$2^{2^n} <= (2^n)
let c be 2 and n be 1
$2^{2^n} <= 2(2^n)
== $2^{2^n} <= (2^{n+1})
 $2^{2 ^ 1} <= (2^{1+1})
 = $2^{2} <= (2^{2})
 4 <= 4
 so yes 
.  
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  
.  
$n^{1.01} <= O(\mathrm{log}^2 n
.  let n be 14.467 and c be 1 
14.467 ^1.01 <= 1 x {log}^2 (14.467) 
14.858 <= {log}(14.467) x {log}^(14.467)
14.858 <= 3.85469387 x 3.85469387
14.858 <= 14.858

let n be 4.136 and c be 1

4.136  ^1.01 <= 1 x {log}^2 (4.136) 
4.195 <= {log}(4.136) x {log}^(4.136)
4.195 <= 2.0482 x 2.0482
4.195 <= 4.195

So there exist an n and a c where n^1.01 will always be larger but there exist an n and c where  {log}^2(n) will be larger for a time. 

.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
  $n^{1.01} >= \Omega(\mathrm{log}^2 n)
.  
let n be 4.136 and c be 1

4.136  ^1.01 >= 1 x {log}^2 (4.136) 
4.195 >= {log}(4.136) x {log}^(4.136)
4.195 >= 2.0482 x 2.0482
4.195 >= 4.195
.  

.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  
.  let c be 1 and n be 2.205
$\sqrt{2.205} >= (\mathrm{log}3 x 2.205)^3)
1.485 >= 1.1407786558^3

.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  
.  
.  
.  

  - 1g. Consider the definition of "Little o" notation:
  
$g(n) \in o(f(n))$ means that for **every** positive constant $c$, there exists a constant $n_0$ such that $g(n) \le c \cdot f(n)$ for all $n \ge n_0$. There is an analogous definition for "little omega" $\omega(f(n))$. The distinction between $o(f(n))$ and $O(f(n))$ is that the former requires the condition to be met for **every** $c$, not just for some $c$. For example, $10x \in o(x^2)$, but $10x^2 \notin o(x^2)$.  

.  

**Prove** that $o(g(n)) \cap \omega(g(n))$ is the empty set.  

$o(g(n)) == o(n) > g(n)
\omega(g(n)) == omega(n) < g(n)
therefore 
.  
.  prove that a number can not be bigger and smaller than a number 
prove x < y and x > y can not be true 
this would mean x < y > x meaning x 
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  



2. **SPARC to Python**

Consider the following SPARC code:  
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. What does this function do, in your own words?  

.  
.  fibanocio
.  
.  
.  
.  
  


3. **Parallelism and recursion**

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. What is the Work and Span of this implementation?  

.  As it is not pareilzable span = Work 
the runt time would be O(n^2)
.  
.  
.  
.  
.  
.  
.  
.  


  - 3c. Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. What is the Work and Span of this sequential algorithm?  
.  
.  as we are not perelizing it the Span = Work
O(log(n))
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3e. Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  
.  
.  work is O(log(n))
span is 2w(n/2)+ O(n)
.  
.  
.  
.  
.  

