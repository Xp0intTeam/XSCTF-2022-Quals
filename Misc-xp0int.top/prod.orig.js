var logo_cnt = 0;

function click_check() {
    logo_cnt++;
    if (logo_cnt == 3) {
        alert("0:efdd57e9");
    }
}

function to_func(obj) {
    obj.getElementsByTagName('span')[0].outerText = "2:ea1787f7";
}

obj = document.getElementsByClassName('xp0int_logo')[0];
if (obj) {
    obj.onclick = click_check;
} else {
    obj = document.getElementsByClassName('events__title')[0];
    if (obj) {
        setTimeout(to_func, 273000, obj);
    }
}
