# 生成日志信息
import logging
# 1. 创建日志模块
loginLogger = logging.getLogger("main")
log = logging.getLogger('test')
# 2. 设置日志等级
log.setLevel(logging.INFO)

# 3. 创建日志文件编码与格式
file_log = logging.FileHandler('module_log.txt', encoding='utf-8')
fmt = logging.Formatter('%(name)s--%(levelname)s--%(asctime)s--%(message)s')
file_log.setFormatter(fmt)
# 设置文件日志等级
file_log.setLevel(logging.ERROR)

# 创建控制台输出
stream_log = logging.StreamHandler()
# 设置控制台输出格式
stream_log.setFormatter(fmt)
# 设置控制台输出等级
stream_log.setLevel(logging.DEBUG)

# 将日志句柄添加到日志模块
log.addHandler(file_log)
log.addHandler(stream_log)

# 创建日志内容
log.debug('debug')
log.info('info')
log.warning('warning')
log.error('error')


