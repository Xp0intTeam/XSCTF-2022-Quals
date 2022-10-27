<?php

class sing {
    public function __wakeup()
    {
        ikun::$caixukun_baby = true;
    }
}

class basketball {
    private $i_want_a_basketball_or_flag;
    public function __toString()
    {
        if (ikun::$ikun_baby) {
            if(!preg_match("/\;|cat|flag|[0-9]|\*|more|wget|less|head|sort|tail|tac|sed|cut|awk|strings|od|curl/i", $this->i_want_a_basketball_or_flag)){
                return system($this->i_want_a_basketball_or_flag);
            }
            else
            {
                throw new Error("~~aiyo~~!");
            }
        } else {
            throw new Error("~~aiyo,what are you doing~~!");
        }
    }
}


class rap {
    public function __invoke()
    {
        ikun::$ikun_baby = true;
        return "practice lasts two and a half years" . $this->value;
    }
}

class dance {
    public function __destruct()
    {
        if (ikun::$caixukun_baby) {
            ($this->kunkun)();
        } else {
            throw new Error("oh no~,Hello nasty");
        }
    }
}

class ikun {
    public static $caixukun_baby = false;
    public static $ikun_baby = false;
}

if (isset($_GET['flag'])) {
    unserialize(base64_decode($_GET['flag']));
} else {
    highlight_file(__FILE__);
}
?>
