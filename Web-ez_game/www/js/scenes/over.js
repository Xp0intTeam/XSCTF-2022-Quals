class Over extends Scene{
    setup() {
        
        this.game.data.end = true;

        this.updateView()

        this.event();
    }

    //secret！don't edit it!!!!!!!!!!
    fl4g(score, name) {
        var request=new XMLHttpRequest();
        
        request.open('post','flag.php');
        
        request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
        
        var score_1 =score;
        
        request.send("score="+score_1+"&checkcode="+md5(name));

        request.onreadystatechange=function () {
            if(request.readyState==4&&(request.status==200||request.status==304)){
                alert(request.responseText);
            }
        }
    }


    updateView(){
        const {
            time,
            score,
            shoot,
        } = this.game.data;
        $('#over .time').innerHTML = numberFormat(time);
        $('#over .score').innerHTML = numberFormat(score);
        $('#over .shoot').innerHTML = numberFormat(shoot);
    }

    event(){
        const {
            time,
            score,
            shoot,
        } = this.game.data;
        const btn = $('#submit-btn');
        const name = $('#name');
        on(
            btn,
            'click',
            ()=>{
                this.game.data.name = name.value;
                this.game.rank();
                this.fl4g(score, name.value);
            }
        );

        on(
            name,
            'input',
            ()=>{
                const empty = name.value === '';
                const attr = empty ? 'setAttribute' : 'removeAttribute';
                btn[attr]('disabled','disabled');
            }
        ) 
    }
}