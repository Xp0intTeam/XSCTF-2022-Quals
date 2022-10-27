clear
global delta
global b
global lambda
lambda=1;
delta=1;
b=2;
watermarked_lena=imread("watermarked_sample.png");

%load order.mat
????
order=[];

reorder=1:512*80;
for i=1:length(order)
    reorder(?????)=i;
end

flag=Extract(reshape(watermarked_lena(1:3:480,:,1),2,[]));
flag=flag(reorder);
f=reshape(flag,80,[]);
imwrite(????,"w.jpg");

function w=Extract(p)
    global delta;
    global b;
    global lambda;
    w=zeros(1,length(p));
    p=p(1,:)????(p(2,:)????lambda);
    for i=1:length(p)
        w(i)=mod(p(i),????);
    end
end