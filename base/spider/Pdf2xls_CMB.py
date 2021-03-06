import sys
# sys.path.append('')
import pdfplumber
import re
import os
from datetime import datetime
import ExcelWriter
import My_Logger
import logging
import types
leaf_path = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
root_logger = My_Logger.Logger('cmb_transform', r'CMB_transform_log.log')


colums = {
    '1': '文件名',
    '名称': '理财产品',
    '理财计划期限|存款期限': '募集期',
    '类型': '产品类型',
    '认购期': '产品期限(天）',
    '发行规模': '计划募集规模（亿）',
    '认购起点|起存金额':'认购起点（万）',
    '本金及利息|业绩比较基准':'业绩基准（预期收益率）',
    '销售费率': '销售费率',
    '托管费率': '托管费率',
    '认购费': '认购费',
    '赎回费': '赎回费',
    '固定投资管理费率': '管理费',
    '挂钩标的': '投向资产',
    '估值方法': '估值方法',
    '风险等级': '风险等级',
    '客户类型': '客户类型',
    '原始数据': '原始数据'
}

n = 1

def create_dir(file_path):
    if not os.path.exists(base_path):
        os.makedirs(file_path)
        return True
    else:
        return False

# 根据模板获取数据
def get_data_by_template(template, content_template=None, handler=None, td_num = 1):
    def get_data(tr, result):
        if tr[0] and re.search(template, tr[0].replace('\n', '')):
            if content_template == None:
                if handler:
                    handler(tr[td_num].replace('\n', ''), result, template,tr[td_num].replace('\n', ''))
                    return result[template]
                result[template] = tr[td_num].replace('\n', '')
                return result[template]
            else:
                if tr[td_num]:
                    if handler:
                        handler(re.findall(content_template, tr[td_num].replace('\n', '')), result, template, tr[td_num].replace('\n', ''))
                        return re.findall(content_template, tr[td_num].replace('\n', ''))

                    result[template] = re.findall(content_template, tr[td_num].replace('\n', ''))[0]
                    return result[template]
                else:
                    # 获取某个字段失败
                    root_logger.warning('getting %s failed' % template)
                    return ''
        else:
            # 获取某个字段失败

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
    # print(file_paths)
    return file_paths

# 向excel中写文件
# 后面可以借助工具包来实现
def write_excel(data, output_path):
    create_dir(output_path)
    # output = open(output_path + '/bank_output_(%s).xls' % leaf_path, 'w', encoding='utf8')
    # print('文件路径：' + output_path + '/bank_output_(%s).xls' % leaf_path )
    # print(data)
    # # final_table = [['a', 'b'], ['c', 'd']]
    # for colum in colums.values():
    #     output.write(colum)
    #     output.write('\t')
    # output.write('\n')
    # for column1 in data:
    #     for item in colums.keys():
    #         v = column1.get(item, '')
    #         # print(v)
    #         # if column[item]:
    #         output.write(v)
    #         # else:
    #         output.write('\t')
    #     output.write('\n')
    # output.close()
    ExcelWriter.write_single_excel(output_path + '/招商银行_(%s).xls' % leaf_path, '招商银行', data, colums)
    print('================================OK!!!==============================')


def handle_start_point(start_points, result, content_template, content):
    if not start_points:
        return
    for start_point in start_points[0]:
        if start_point:
            result[content_template] = start_point


def handle_date(dates, result, content_template, content):
    if not dates:
        return
    result[content_template] = dates[0][1].replace(' ', '') + '-' + dates[0][1].replace(' ', '')
    # return result


def handle_interest(interests, result, content_template, content):
    if not interests:
        return
    result[content_template] = interests[0] + '/' + interests[1]
    return result



def handle_scale(scales, result, content_template, content):
    if not scales:
        return
    for scale in scales[0]:
        if scale:
            result[content_template] = scale
            return result[content_template]
    # return result


def handle_type(types, result, content_template, content):
    if not types:
        return
    result['名称'] = types.replace('\n', '')
    if re.findall(r'结构性存款|非保本理财计划', types):
        result['类型'] = re.findall(r'结构性存款|非保本理财计划', types)[0]
    return result

def handle_type1(types, result, content_template, content):
    # print('================= geta type =================', types)
    if not result.get('类型'):
        result['类型'] = types
    return result

def handle_rate(rates, results, content_template, content):
    if not rates:
        return
    items = ['销售', '托管', '管理']
    # count = 0
    for rate in rates[0]:
        if rate:
            sale = re.findall(r'销售\w*\W*(\d+.\d+%/年)', rate)
            # print(sale)
            if sale:
                results['销售费率'] = sale[0]
            else:
                delegate = re.findall(r'托管\w*\W*(\d+.\d+%/年)', rate)
                if delegate:
                    results['托管费率'] = delegate[0]
                else:
                    manage = re.findall(r'管理\w*\W*(\d+.\d+%/年)', rate)
                    if manage:
                        results['固定投资管理费率'] = manage[0]

    return results


# 获取数据
def transform_data(file_paths, Number):
    get_name = get_data_by_template('名称', None, handle_type)
    get_start_point = get_data_by_template('认购起点|起存金额', r'须为.*?(\d+\W*万)份|认购起点份额为.*?(\d+\W*万)份|(\d+\W*万)元|最低份额为\W*(\d+\W*\w+)份', handle_start_point)
    get_limit = get_data_by_template('理财计划期限|存款期限', r'\d+\W*天')
    get_subscription_periode = get_data_by_template('认购期',r'(\d*\W*年\W*\d*\W*月\W*\d*\W*日)\W*\d*:\d*\W*[至|到](\W*\d*\W*年\W*\d*\W*月\W*\d*\W*日)\W*\d*:\d*', handle_date)
    get_scale = get_data_by_template('发行规模', r'(\d+.*元\w+)|每期上限(\d+.*\w+)人民币|上限\W*(\d+\W*\w{1})', handle_scale)
    get_rate = get_data_by_template('费用', r'\W*([销售|托管|管理]\w*\W*\d+.\d+%/年)\S+\n*.*?\W*([销售|托管|管理]'
                                          r'\w*\W*\d+.\d+%/年)\S+\n*.*?\W*([销售|托管|管理]\w*\W*\d+.\d+%/年)|'
                                          r'\W*([销售|托管|管理]\w*\W*\d+.\d+%/年)\S+\n*.*?\W*([销售|托管|管理]\w*\W*\d+.\d+%/年)', handle_rate)
    get_interest_rate1 = get_data_by_template(r'本金及利息|业绩比较基准', r'\d+.\d+%|d+.\d+%-d+.\d+%', handle_interest)
    get_cast_assess = get_data_by_template(r'挂钩标的')
    get_type = get_data_by_template('类型', None, handle_type1)
    get_methods = [get_name, get_start_point, get_limit, get_subscription_periode, get_scale, get_rate, get_interest_rate1, get_cast_assess, get_type]
    file_NO = 0
    final_table = []
    # file_count = 0
    for file_path in file_paths:
        file_NO += 1
        if file_NO > Number:
            # print(file_NO, Number)
            break

        print('==================handling the (%s)th file==============' % file_NO)
        try:
            root_logger.debug('-----------------handling file: %s ---- %s-------------------- ' % file_path)
        except UnicodeEncodeError as e:
            root_logger.error('UnicodeEncodeError', e)
        with pdfplumber.open(file_path[0]) as pdf:
                results = {'1': 'hyperlink("%s","%s")' % (file_path[0], file_path[1])}
                final_table.append(results)
                result1 = ''
                for page in pdf.pages:
                    for tab in page.extract_tables():
                        result1 += '('
                        for td in tab:
                            td_count = -1
                            for method in get_methods:
                                result =method(td, results)
                                for t in td:
                                    if type(t) == type('a') :
                                        result1 += t
                                td_count += 1
                                if result != '':
                                    results[td_count] = result
                                    break
                        result1 += ');'
                        results.setdefault('原始数据', result1)

    return final_table

# 文件主入口
def pdf2xls(file_path, out_put_path,  Number):
    # create_dir(out_put_path + '/out_put')
    # 首先读取所有文件
    files_path = get_files_path(file_path)
    # 其次将文件转化为想要的数据结构
    datas = transform_data(files_path,  Number)
    # 最后写入excel中
    write_excel(datas, out_put_path + '/out_put')


if __name__ =='__main__':
    base_path = input('请输入你所处理的文件路径：')
    output_path = base_path
    Number = int(input('请输入文件数目：'))
    pdf2xls(base_path, output_path, Number)
