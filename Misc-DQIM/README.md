* **题目名称：** DQIM

* **题目类型：** MISC

* **题目难度：** 中等 / 困难

* **出题人：** hututu

* **考点：**  

1. 基于除法域的量化索引调制水印嵌入和提取（方案复现）

2. matlab语法

3. 随机置乱复原


* **描述：**  摊牌了，整了个论文题

* **flag：** flag{data_hiding_in_division!!!}

* **Writeup：**  

  QIM 一种量化索引调制水印方案，主要思想在于将像素点移动到最近的某一个区域，而此区域代表一个值，从而实现水印的嵌入。
  
  以下是嵌入公式：
  $$
  p'=\lfloor\cfrac{p+m[i]\Delta}{2\Delta}\rfloor2\Delta+m[i]\Delta
  $$
  水印嵌入方法如下：
  $$
  m[i]=\lfloor \cfrac{p'}{\Delta} \rfloor\ mod \ 2
  $$
  给的图片中其实是论文的链接 https://doi.org/10.1007/978-981-19-5209-8_4 ，论文的最简方案中则增加了一个步骤，将水印嵌入域进行调整，上下p1和p2两个像素点进行相除后得到的数值再作为上述p进行水印嵌入，而嵌入后得值p'再乘以p2得到新的p1'，再将p1'和p2放置回图像中，完成水印嵌入。因此在提取水印时，需要将上下两个像素值相除后在进行上述式子的计算，提取出数据。
  
  在给的源码中应该注意到，除去水印嵌入操作，增加了一个flag图片置乱操作，给出了随机数种子，因此可以进行复现，得到相同的随机数序列，从而得到置乱顺序，恢复flag图像。
  
  提取脚本如下：
  
  ```matlab
  clear
  global delta
  global b
  global lambda
  lambda=1;
  delta=1;
  b=2;
  watermarked_lena=imread("watermarked_sample.png");
  
  rng(2022);
  order=[];
  while length(order)~=512*80
      a=randi([1,512*80],1);
      if ismember(a,order)
      else
          order=[order,a];
      end
  end
  reorder=1:512*80;
  for i=1:length(order)
      reorder(order(i))=i;
  end
  
  flag=Extract(reshape(watermarked_lena(1:3:480,:,1),2,[]));
  flag=flag(reorder);
  f=reshape(flag,80,[]);
  imwrite(f*255,"w.jpg");
  function w=Extract(p)
      global delta;
      global b;
      global lambda;
      w=zeros(1,length(p));
      p=p(1,:)./(p(2,:)*lambda);
      for i=1:length(p)
          w(i)=mod(p(i)/delta,b);
      end
  end
  ```
  
  
