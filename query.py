def main_select(valueBox, search, select, conn):

    select_like = ("'" + '%' + select + '%' + "'")

    cursor = conn.cursor()

    if search.isdigit():

        product = "[Полный код]"
        #q = ('SELECT ' + valueBox + ' FROM WebMonitordb WHERE ' + product + ' = ' + ' and [Филиал] like ' + select_like + 'GROUP BY ' + valueBox)
        q = ('SELECT ' + valueBox + ' FROM WebMonitordb where ' + product + ' = ' + search + 'and [Филиал] like ' + select_like)
        cursor.execute(u'p_selectFromWebMonitorWithParams %s', q)
        data_back = cursor.fetchall()
        conn.close()

    else:

        product = "[Название]"
        search_like = ("'" + '%' + search + '%' + "'")
        q = ("SELECT " + valueBox + " FROM WebMonitordb WHERE " + product + " like " + search_like + " and [Филиал] like " + select_like + "GROUP BY " + valueBox)
        cursor.execute(u'p_selectFromWebMonitorWithParams %s', q)
        data_back = cursor.fetchall()
        conn.close()

    return data_back
