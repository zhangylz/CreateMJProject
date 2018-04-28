var data = [{"card1":{index:1}, "card2":{index:2},"card3":{index:3},"card4":{index:4}, "card5":{index:5},"card6":{index:6},"card7":{index:7}, "card8":{index:8},"card9":{index:9},},
            {"card1":{index:11}, "card2":{index:12},"card3":{index:13},"card4":{index:14}, "card5":{index:15},"card6":{index:16},"card7":{index:17}, "card8":{index:18},"card9":{index:19},},
            {"card1":{index:21}, "card2":{index:22},"card3":{index:23},"card4":{index:24}, "card5":{index:25},"card6":{index:26},"card7":{index:27}, "card8":{index:28},"card9":{index:29},},
            {"card1":{index:31}, "card2":{index:32},"card3":{index:33},"card4":{index:34}, "card5":{index:35},"card6":{index:36},"card7":{index:37}, "card8":{index:41, checked:true},"card9":{index:42, checked:true},},
            {"card1":{index:43, checked:true}, "card2":{index:44, checked:true},"card3":{index:45, checked:true},"card4":{index:46, checked:true}, "card5":{index:47, checked:true},"card6":{index:48, checked:true},"card7":{index:51}, "card8":{index:52},"card9":{index:53},},
            {"card1":{index:54},},
        ];

var cardMap = [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,
                31,32,33,34,35,36,37,41,42,43,44,45,46,47,48,51,52,53,54
              ];

function initCardMap() {
    var gap = 1;
    for (var i = 0; i < 50; i++) {
        if (i > 0 && i%10 == 0)
            gap++;
        cardMap[i] = i + gap;
    }
};

function cardFormatter(value, row, index) {//赋予的参数
    var  pngPath = '';
    var status = '';
    if (value != undefined && value != '') {
        pngPath = '../static/images/card/' + value.index+ '.png';
        if (value.checked != undefined && value.checked == true) {
            status = 'checked';
        } 
    } else {
        return ['<div> </div>'].join('');
    }
    return [
        '<div>',
            '<div  style="float:left;width:25%;vertical-align:middle;">',
                '<input type="checkbox" id = "selected" name="selected" style="float:left;vertical-align:middle;" {checked} /input>'.format({checked:status}),
            '</div>',
            '<div  style="float:left;width:45%;vertical-align:middle;">',
                '<img src="{path}" height=55 width=50 alt="" style="float:left;vertical-align:middle;" /img>'.format({path:pngPath}),
            '</div>',
            '<div  style="float:left;width:20%;vertical-align:middle;">',
                '<input class="form-control" maxlength="1" name="cardCnt" id="cardCnt" placeholder="4" style="float:left;width: 10px;vertical-align:middle;" /input>',
            '</div>',
        '</div>',
    ].join('');
};


function initTable(obj) {
    obj.bootstrapTable({
        idField: 'name',
        showHeader:false,
        columns: [
                [
                    {
                        field: 'card1',
                        title: '牌',
                        formatter: cardFormatter //自定义方法，添加操作按钮
                    },
                    {
                        field: 'card2',
                        title: '牌',
                        formatter: cardFormatter //自定义方法，添加操作按钮
                    },
                    {
                        field: 'card3',
                        title: '牌',
                        formatter: cardFormatter //自定义方法，添加操作按钮
                    },
                    {
                        field: 'card4',
                        title: '牌',
                        formatter: cardFormatter //自定义方法，添加操作按钮
                    },
                    {
                        field: 'card5',
                        title: '牌',
                        formatter: cardFormatter //自定义方法，添加操作按钮
                    },
                    {
                        field: 'card6',
                        title: '牌',
                        formatter: cardFormatter //自定义方法，添加操作按钮
                    },
                    {
                        field: 'card7',
                        title: '牌',
                        formatter: cardFormatter //自定义方法，添加操作按钮
                    },
                    {
                        field: 'card8',
                        title: '牌',
                        formatter: cardFormatter //自定义方法，添加操作按钮
                    },
                    {
                        field: 'card9',
                        title: '牌',
                        formatter: cardFormatter //自定义方法，添加操作按钮
                    },
                ],
            ],
        data: data
    });
}


