import os
def abc():

    path = os.path.dirname(os.path.realpath(__file__))
    print("the path ", path)
    print("os.pardir ", os.pardir)
    pardir = os.path.abspath(os.path.join(path, os.pardir))
    print("the pardir ", pardir)
    jdbc_file = '{}/jdbc/mssql-jdbc-9.2.1.jre8.jar'.format(pardir)
    print("jdbc file ", jdbc_file)
    sql_file  = '{}/sql/lvs_export.sql'.format(pardir)
    print("sql file ", sql_file)
    #csv_file  = '{}tmp/lvs_inventory_{}.csv'.format(config["paths"]["data_path"], dt.datetime.strftime(dt.datetime.now(), "%Y%m%d"))



if __name__ == '__main__':
    abc()
