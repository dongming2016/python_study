import sys
sys.path.append('C:\\Users\\35037\\AppData\\Roaming\\Python\\Python37\\site-packages')
print(sys.path)

import pdfplumber
import re
import os
from datetime import datetime

# 基础设置
base_path = 'D:\\bank\\CMB\\2019-04-02-23-01-47'
output_path = 'D:\\bank\\CMB\\'
# Number = int(input('请输入您想要处理的文件数量：'))
leaf_path = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
# Number = 10


colums = {
    '1': '文件名',
    '名称': '理财产品',
    '理财计划期限|存款期限': '募集期',
    '类型': '产品类型',
    '认购期': '产品期限(天）',
    '发行规模': '计划募集规模（亿）',
    '认购起点|起存金额':'认购起点（万）',
    '本金及利息':'业绩基准（预期收益率）',
    '销售费率': '销售费率',
    '托管费率': '托管费率',
    '认购费': '认购费',
    '赎回费': '赎回费',
    '固定投资管理费率': '管理费',
    '挂钩标的': '投向资产',
    '估值方法': '估值方法',
    '风险等级': '风险等级',
    '客户类型': '客户类型',
}

n = 1


# 根据模板获取数据
def get_data_by_template(template, content_template=None, handler=None, td_num = 1):
    def get_data(tr, result):
        # print(template, td_num)
        # print('asdfffffffffff==', template)
        if tr[0] and re.search(template, tr[0].replace('\n', '')):
            if content_template == None:
                if handler:
                    handler(tr[td_num].replace('\n', ''), result, template)
                    # print('cccccccccccccccccccccccccccccddddddd',result)
                    return result[template]
                # print('cccccccccccccccccccccccccccccddddddd', result)
                result[template] = tr[td_num].replace('\n', '')
                return result[template]
            else:
                if tr[td_num]:
                    print(content_template, tr[td_num])
                    if handler:
                        handler(re.findall(content_template, tr[td_num].replace('\n', '')), result, template)
                        return re.findall(content_template, tr[td_num].replace('\n', ''))

                    result[template] = re.findall(content_template, tr[td_num].replace('\n', ''))[0]
                    return result[template]
                else:
                    # 获取某个字段失败
                    # print('getting %s failed of file %s' % (template, file))
                    return ''
        else:
            # 获取某个字段失败
            # print('getting %s failed of file %s' % (template, file))
            return ''
    return get_data


def create_dir(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)
        return True
    else:
        print('路径已存在')
        return False


def compare(x):
    # print(x)
    stat_x = os.stat( x[0])
    # print(stat_x)
    return stat_x.st_atime

# 读取指定文件
# file_reg后面用来做模糊搜索
def get_files_path(file_path, file_reg = ''):
    files_name = os.listdir(file_path)
    file_paths = [(file_path + '/' + file, file)for file in files_name if file.endswith('.pdf')]
    file_paths.sort(key=compare, reverse=True)
    print(file_paths)
    return file_paths

# 向excel中写文件
# 后面可以借助工具包来实现
def write_excel(data, output_path):
    output = open(output_path + '/bank_output_(%s).xls' % leaf_path, 'w', encoding='utf8')
    # final_table = [['a', 'b'], ['c', 'd']]
    for colum in colums.values():
        output.write(colum)
        output.write('\t')
    output.write('\n')
    for column1 in data:
        for item in colums.keys():
            v = column1.get(item, '')
            # print(v)
            # if column[item]:
            output.write(v)
            # else:
            output.write('\t')
        output.write('\n')
    output.close()
    print('================================OK!!!==============================')


def handle_start_point(start_points, result, content_template):
    if not start_points:
        return
    for start_point in start_points[0]:
        if start_point:
            result[content_template] = start_point


def handle_date(dates, result, content_template):
    print(dates)
    if not dates:
        return
    # print('+++++++++++++++++++++++++++++++++', dates)
    result[content_template] = dates[0][1].replace(' ', '') + '-' + dates[0][1].replace(' ', '')
    print(result[content_template])
    # print('cccccccccccccccccccccccccccccddddddd', result)
    # return result


def handle_interest(interests, result, content_template):
    print(interests)
    if not interests:
        return
    result[content_template] = interests[0] + '/' + interests[1]
    # print('cccccccccccccccccccccccccccccddddddd', result)
    # return result



def handle_scale(scales, result, content_template):
    print(scales)
    if not scales:
        return
    for scale in scales[0]:
        if scale:
            # print('cccccccccccccccccccccccccccccddddddd',scale)
            result[content_template] = scale
            # print('cccccccccccccccccccccccccccccddddddd', result)
            return result[content_template]
    # return result


def handle_type(types, result, content_template):
    if not types:
        return
    # for type in types:
    #     if type:
    result['名称'] = types.replace('\n', '')
    if re.findall(r'结构性存款|非保本理财计划', types):
        result['类型'] = re.findall(r'结构性存款|非保本理财计划', types)[0]
    # result[content_template] = type
    # print('cccccccccccccccccccccccccccccddddddd', result)
    return result
    # return result

def handle_rate(rates, results, content_template):
    print(rates)
    if not rates:
        return
    items = ['销售费率', '托管费率', '固定投资管理费率']
    count = 0
    for rate in rates[0]:
        if rate:
            # print('cccccccccccccccccccccccccccccddddddd', rate)
            results[items[count]] = rate
        count += 1
    # return results


# 获取数据
def transform_data(file_paths, Number):
    get_name = get_data_by_template('名称', None, handle_type)
    # get_start_point = get_data_by_template('认购起点', '(\d+).*1\W*份.*认购起点份额为.*?(\d+\W*万)份')
    get_start_point = get_data_by_template('认购起点|起存金额', '须为.*?(\d+\W*万)份|认购起点份额为.*?(\d+\W*万)份|(\d+\W*万)元', handle_start_point)
    get_limit = get_data_by_template('理财计划期限|存款期限', r'\d+\W*天')
    get_subscription_periode = get_data_by_template('认购期',r'(\d*\W*年\W*\d*\W*月\W*\d*\W*日)\W*\d*:\d*\W*至(\W*\d*\W*年\W*\d*\W*月\W*\d*\W*日)\W*\d*:\d*', handle_date)
    get_scale = get_data_by_template('发行规模', r'(\d+.*元\w+)|每期上限(\d+.*\w+)人民币', handle_scale)
    get_rate = get_data_by_template('费用', r'\W*(\d+.\d+%)/年\S+\n*.*?\W*(\d+.\d+%)/年|\W*(\d+.\d+%)/年\S+\n*.*?\W*(\d+.\d+%)/年\S+\n*.*?\W*(\d+.\d+%)/年', handle_rate)
    get_interest_rate1 = get_data_by_template(r'本金及利息', r'\d+.\d+%', handle_interest)
    get_cast_assess = get_data_by_template(r'挂钩标的')
    # get_type = get_data_by_template('类型', '结构性存款|非保本理财计划', handle_type)
    get_methods = [get_name, get_start_point, get_limit, get_subscription_periode, get_scale, get_rate, get_interest_rate1, get_cast_assess]
    # get_interest_rate2 = get_data_by_template(r'理财计划于第%w+个自动终止清算日自动终止', r'\d+.\d+%')
    final_data = []
    file_NO = 0
    final_table = []
    # file_count = 0
    for file_path in file_paths:
        if file_NO > Number:
            print(file_NO, Number)
            break
        file_NO += 1
        print('================================handling the (%s)th file' % file_NO)
        try:
            print('------------------------------------- handling file: %s ---- %s' % file_path)
        except UnicodeEncodeError as e:
            print('UnicodeEncodeError', e)
        with pdfplumber.open(file_path[0]) as pdf:
                results = {'1': '=hyperlink("%s","%s")' % (file_path[0], file_path[1])}
                final_table.append(results)
                for page in pdf.pages:
                    for tab in page.extract_tables():
                        print(tab)
                        for td in tab:
                            td_count = -1
                            # print('===========================result', results)
                            for method in get_methods:
                                result =method(td, results)
                                # print('+++++++++++++++++++++++result++++++++++++++++++++', results)
                                # print('+++++++++++++++++++++++result', file_path, td_count)
                                td_count += 1
                                if result != '':
                                    # results[td_count] = result
                                    print('+++++++++++++++++++++++result', file_path, td_count)
                                    print('====================results', file_path, results)
                                    break
                            # print('+++++++++++++++++++++++++++', [get_name(td, file_path[0]), get_start_point(td, file_path[0]), get_limit(td, file_path[0]),
                            #        get_subscription_periode(td, file_path[0]), get_scale(td, file_path[0]), get_rate(td, file_path[0]), get_interest_rate1(td, file_path[0])])
    return final_table

# 文件主入口
def pdf2xls(file_path, out_put_path,  Number):
    # create_dir(out_put_path + '/out_put')
    # 首先读取所有文件
    files_path = get_files_path(file_path)
    print(file_path)
    # 其次将文件转化为想要的数据结构
    datas = transform_data(files_path,  Number)
    # 最后写入excel中
    write_excel(datas, out_put_path + '/out_put')


if __name__ =='__main__':
    Number = input('请输入文件数目：')
    pdf2xls(base_path, output_path, Number)
