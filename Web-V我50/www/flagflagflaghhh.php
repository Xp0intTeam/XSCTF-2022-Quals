<?php
error_reporting(0);
highlight_file(__FILE__);

$input = $_POST['a'];
if (isset($input)) {
    if (substr($input, 0, 5) == "vme50" and substr($input, -1, 1) == "!") {
        if ($input == "vme50!") {
            die("Speak a little louder, I can't hear you!");
        }
        if (preg_match('/vme50.+?!/is', $input)) {
            die("xing bu xing a.Speak much louder!");
        }
        system("cat /flag");
    } else
        echo "Bie lai zhan bian!!!";
}
