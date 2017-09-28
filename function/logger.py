import logging,os,time
import configparser

base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\','/')
#存储地址
log_path = base_dir + "/log"
#读取配置文件地址
logini_path = base_dir + "/configuration/log.conf"

cf = configparser.ConfigParser()
cf.read(logini_path)
control_file_open = int(cf.get("log_control","control_file_open"))
control_stream_open = int(cf.get("log_control","control_stream_open"))
formatter = cf.get("log_control","formatter").replace('|','%')

class Log:
    def __init__(self):
        self.logname = os.path.join(log_path,'%s.log'%time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        #日志输出格式
        self.formatter = logging.Formatter(formatter)

    def __console(self,level,message):
        if control_file_open == 1:
            #FileHandler,用于写到本地
            fh = logging.FileHandler(self.logname,'a',encoding='utf-8')
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(self.formatter)
            self.logger.addHandler(fh)

        if control_stream_open == 1:
            #StreamHandler,用于输出控制台
            sh = logging.StreamHandler()
            sh.setLevel(logging.DEBUG)
            sh.setFormatter(self.formatter)
            self.logger.addHandler(sh)

        #写入日志
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        # #避免日志重复输出
        if control_stream_open == 1:
            self.logger.removeHandler(sh)
        if control_file_open == 1:
            self.logger.removeHandler(fh)
        #关闭打开的文件
            fh.close()

    def debug(self,message):
        self.__console('debug',message)

    def info(self,message):
        self.__console('info',message)

    def error(self,message):
        self.__console('error',message)

    def warning(self,message):
        self.__console('warning',message)

#测试函数
if __name__ == '__main__':
    log = Log()
    log.info('begin test')
    #log.info('this is my test')
    # log.warning('test end')










