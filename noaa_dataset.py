from ftplib import FTP
import os

def ftp_connect():
    ftp_server = 'ftp.ncdc.noaa.gov'
    username = ''
    password = ''
    ftp = FTP()
    ftp.set_debuglevel(1)
    ftp.connect(ftp_server, 21)
    ftp.login(username, password)
    return ftp

def download_file():
    ftp = ftp_connect()
    data_path = '/pub/data/noaa/'
    begin_year = int(input('输入起始年份：'))
    end_yaer = int(input('输入结束年份：'))
    while begin_year <= end_yaer:
        path = data_path + str(begin_year)
        data_list = ftp.nlst(path)
        if os.path.exists('noaa') is True:
            os.mkdir('noaa/' + str(begin_year) + '/')
        else:
            os.mkdir('noaa')
            os.mkdir('noaa/' + str(begin_year) + '/')
        for eachfile in data_list:
            localpaths = eachfile.split('/')
            localpath = localpaths[len(localpaths) - 1]
            localpath = 'noaa/' + str(begin_year) + '/' + localpath
            bufsize = 1024
            fp = open(localpath, 'wb')
            ftp.retrbinary('RETR ' + eachfile, fp.write, bufsize)
        begin_year = begin_year + 1
    ftp.set_debuglevel(0)
    fp.close()
    ftp.quit()

def main():
    download_file()

if __name__ == "__main__":
    main()
