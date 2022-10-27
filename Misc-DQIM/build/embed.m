clear
global delta
global b
global lambda
delta=1;
b=2;
lambda=1;

% sample
sample=ones(512,"uint8")*80;
hint=imread("hint.png");
sample(481:512,1:424)=hint(:,:,1);
% message
flag=imread("flag.jpg");% 512*80
for i=1:80
    for j=1:512
        if(flag(i,j)<200)
            flag(i,j)=0;
        else
            flag(i,j)=1;
        end
    end
end


rng(2022);
order=[];
while length(order)~=512*80
    a=randi([1,512*80],1);
    if ismember(a,order)
    else
        order=[order,a];
    end
end
flag=flag(order);


watermarked_lena=Embed(reshape(sample(1:3:480,:,1),2,[]),reshape(flag,1,[]));
result(1:3:480,1:512,1)=reshape(watermarked_lena,160,[]);
result(2:3:480,1:512,1)=sample(2:3:480,1:512);
result(3:3:480,1:512,1)=sample(3:3:480,1:512);
result(481:512,1:512,1)=sample(481:512,1:512);
imwrite(result,"watermarked_sample.png");



function m=Embed(p,s)
    global delta;
    global b;
    global lambda;
    m=p;
    p1=p(1,:)./(p(2,:)*lambda);
    p2=p(2,:);
    for i=1:length(s)
        %[p1(i),s(i),p2(i)]
        m(1,i)=((p1(i)+delta*s(i))/(b*delta)*b*delta+s(i)*delta)*p2(i)*lambda;
    end
end