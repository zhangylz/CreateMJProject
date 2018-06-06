# -*- coding:utf-8 -*-
from flask import Flask, render_template, request, url_for, make_response, session
import json
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.secret_key = 'A0Zr98j/3yX:R!XHH!jmN]LWX/,?RT'

PAI_QIANG = ['wan_1', 'wan_2', 'wan_3', 'wan_4', 'wan_5', 'wan_6', 'wan_7', 'wan_8', 'wan_9',
             'tiao_1', 'tiao_2', 'tiao_3', 'tiao_4', 'tiao_5', 'tiao_6', 'tiao_7', 'tiao_8', 'tiao_9',
             'tong_1', 'tong_2', 'tong_3', 'tong_4', 'tong_5', 'tong_6', 'tong_7', 'tong_8', 'tong_9',
             'dong_feng', 'nan_feng', 'xi_feng', 'bei_feng', 'hong_zhong', 'fa_cai', 'bai_ban',
             'chun', 'xia', 'qiu', 'dong', 'mei', 'lan', 'zhu', 'ju']
cardMap = ['cardCnt1','cardCnt2','cardCnt3','cardCnt4','cardCnt5','cardCnt6','cardCnt7','cardCnt8','cardCnt9',
                'cardCnt11','cardCnt12','cardCnt13','cardCnt14','cardCnt15','cardCnt16','cardCnt17','cardCnt18','cardCnt19',
                'cardCnt21','cardCnt22','cardCnt23','cardCnt24','cardCnt25','cardCnt26','cardCnt27','cardCnt28','cardCnt29',
                'cardCnt31','cardCnt32','cardCnt33','cardCnt34','cardCnt35','cardCnt36','cardCnt37',
                'cardCnt41','cardCnt42','cardCnt43','cardCnt44','cardCnt45','cardCnt46','cardCnt47','cardCnt48',
                'cardCnt51','cardCnt52','cardCnt53','cardCnt54'
              ]

HU_MATH = ['algo_qingyise', 'algo_duiduihu', 'algo_quemen', 'algo_gangkai', 'algo_huagangkai', 'algo_hunyise',
           'algo_qidui', 'algo_shisanyao', 'algo_dadiaoche', 'algo_bianzhang', 'algo_kazhang', 'algo_diaojiang',
           'algo_qianggang', 'algo_juezhang', 'algo_ziyise', 'algo_haidi', 'algo_quanshunzi']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('CreateMJTemp.html')
    elif request.method == 'POST':
        keys = []
        values = []
        for i in request.form:
            keys.append(i)
            values.append(request.form[i])
        dict_data = dict(zip(keys, values))
        session['messages'] = json.dumps(make_json_data(dict_data), ensure_ascii=False)
        return url_for('download_json')

@app.route('/download_json', methods=['GET', 'POST'])
def download_json():
    if request.method == 'POST':
        response = make_response(session['messages'])
        response.headers['Content-Disposition'] = 'attachment; filename=config.json'
        return response

def make_json_data(data):
    # 会出现两次data,第一次是空{}
    if len(data) > 0:
        ret = {}
        keys = data.keys()
        # 牌墙
        pai_qiang = []
        for pai in cardMap:
            if data[pai]:
                pai_qiang.append(int(data[pai]))
        ret['wall'] = pai_qiang

        # 花牌
        hua_pai = []
        for hua in list(filter(lambda x:'selected' in x, keys)):
            if data[hua]:
                hua_pai.append(int(data[hua]))
        if len(hua_pai) > 0:
            ret['hua'] = hua_pai
        else:
            ret['hua'] = None

        # 名称
        ret['gameName'] = data['game_name']
        ret['gameEName'] = data['game_enname']
        # if len(data['nodeid']) > 0:
        #     ret['nodeId'] = int(data['nodeid'])
        # else:
        #     ret['nodeId'] = 0

        # 玩家人数
        if data['basefunc_player'] == 'four':
            ret['maxPlayer'] = 4
        elif data['basefunc_player'] == 'three':
            ret['maxPlayer'] = 3
        elif data['basefunc_player'] == 'two':
            ret['maxPlayer'] = 2

        # 胡型算法
        if data['extra_algo'] == 'yipaoduoxiang':
            ret['isHuMore'] = True
        elif data['extra_algo'] == 'jiehu':
            if data['extra_algo_jiehu'] == 'budeng':
                ret['autoHu'] = True
            elif data['extra_algo_jiehu'] == 'deng':
                ret['autoHu'] = False

        # 吃碰杠胡
        if 'basefunc_chi' in data:
            ret['canChi'] = True
        else:
            ret['canChi'] = False

        if 'basefunc_ting' in data:
            ret['canTing'] = True
        else:
            ret['canTing'] = False

        if 'basefunc_hu7dui' in data:
            ret['canHuQiDui'] = True
        else:
            ret['canHuQiDui'] = False

        if 'basefunc_hu13yao' in data:
            ret['canHuYao'] = True
        else:
            ret['canHuYao'] = False

        huMath = []
        for math_key in range(len(HU_MATH)):
            if HU_MATH[math_key] in data:
                huMath.append(math_key + 1)
        if len(huMath) > 0:
            ret['huMath'] = huMath
        else:
            ret['huMath'] = None

        # 牌型列表
        card_type = []
        paixing_name_list = sorted(list(filter(lambda x:'paixing_name' in x, keys)))
        paixing_value_list = sorted(list(filter(lambda x:'paixing_value' in x, keys)))
        paixing_miaoshu_list = sorted(list(filter(lambda x:'paixing_miaoshu' in x, keys)))
        paixing_var_list = sorted(list(filter(lambda x:'paixing_var' in x, keys)))
        for i in range(len(paixing_name_list)):
            tmp_card_type = {'name':data[paixing_name_list[i]],
                             'fan':data[paixing_value_list[i]],
                             'descrip':data[paixing_miaoshu_list[i]],
                             'variable':data[paixing_var_list[i]]
                             }
            card_type.append(tmp_card_type)
        if len(card_type) > 0:
            ret['cardType'] = card_type
        else:
            ret['cardType'] = None
        # 自定义规则
        ret['lnode'] = int(data['nodeid_0'])
        ret['tnode'] = int(data['nodeid_1'])
        ret['lgateport'] = int(data['gateport_0'])
        ret['tgateport'] = int(data['gateport_1'])        
        ret['lclusterport'] = int(data['clusterport_0'])
        ret['tclusterport'] = int(data['clusterport_1'])      
        return ret

if __name__ == '__main__':
    app.run(debug=True)