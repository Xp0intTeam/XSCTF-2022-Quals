<?php
error_reporting(0);
$score = $_POST['score'];
$flag=$_POST['checkcode']==md5('ctfer');
function getflag($score, $flag){
    if($score <= -2000 && $flag){
        echo "flag{D0_w311_ctfer_!_1s_it_a_g00d_g@me_?}";
    }elseif($score <= -2000 && !$flag){
         echo "No real ctfer!";
        }else{
            echo "No enough!";
        }
}
getflag($score, $flag);
?>