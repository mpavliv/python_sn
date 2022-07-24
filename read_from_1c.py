from dbfread import DBF


def read_data():
    print('started loading from db')
    sss = ''
    list_sn = []
    table_name = DBF('D:/Base1C/SC302.dbf')
    names = {}
    table_name.encoding = 'cp1251'
    for record in table_name:
        code = record['ID']
        descr = record['DESCR']
        names[code] = descr


    table_doc = DBF('D:/Base1C/1sjourn.dbf')
    docs = {}
    table_doc.encoding = 'cp1251'
    for record in table_doc:
        code = record['IDDOC']
        descr = record['DOCNO']
        docs[code] = descr


    sn = {}
    number = 0
    table_sn = DBF('D:/Base1C/SC16112.dbf')
    table_sn.encoding = 'cp1251'
    for record in table_sn:
        code = record['CODE']
        product_code = record['SP16114']
        if product_code in names:
            product_name = names[product_code]
        else:
            product_name = ''
        fabric1_code = record['SP16115']
        if fabric1_code in names:
            fabric1_name = names[fabric1_code]
        else:
            fabric1_name = ''
        fabric2_code = record['SP16116']
        if fabric2_code in names:
            fabric2_name = names[fabric2_code]
        else:
            fabric2_name = ''
        fabric3_code = record['SP16117']
        if fabric3_code in names:
            fabric3_name = names[fabric3_code]
        else:
            fabric3_name = ''
        doc_code = record['SP16120']
        if doc_code in docs:
            doc_name = 'Замовлення ' + docs[doc_code]
        else:
            doc_name = ''
        remarks = record['SP16121']
        result = code + '/;' + product_name + '/;' + fabric1_name + '/;' + fabric2_name \
                 + '/;' + fabric3_name + '/;' + doc_name + '/;' + remarks
        list_sn.append(result)
        sss += result + '\n'
        index = 'index' + str(number)
        number = number +1
        list_sn.append(result)


    print('ended loading from db')
    return list_sn