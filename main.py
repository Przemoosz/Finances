import databasefunctions
import os
import configparser

def main():
    path=os.getcwd()+'\\config.ini'
    #print(os.listdir(os.getcwd()))
    #print('config.ini'  not in os.listdir(os.getcwd()))
    if 'config.ini' not in os.listdir(os.getcwd()):
        exit("Config.ini not found. Start setup.py first to create configuration file!")
    con=configparser.ConfigParser()
    con.read('config.ini')
    db_host=con['DATABASE']['hostname']
    db_user = con['DATABASE']['username']
    try:
        db_port = int(con['DATABASE']['port'])
    except ValueError:
        exit("Can not conver 'port' to intiger! Run setup.py again and type correct port!")
    db_pass = con['DATABASE']['password']
    #global timer_mode
    timer_mode=con['Timer']['timer']
    databasefunctions.acc_table_overview(host=db_host, user=db_user, password=db_pass, port=db_port)
    pass
if __name__ == '__main__':
    main()