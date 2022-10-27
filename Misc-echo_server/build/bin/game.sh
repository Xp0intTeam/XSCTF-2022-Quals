#!/bin/bash

echo "Plaese input a number: "
read input

# TODO: 检查输入是否为合法数字，防止命令执行

if [[ "$input" -gt 10086 ]]; 
then
    echo "It's too big.";
else
    echo "It's too small.";
fi

echo "Exiting..."
exit 0
