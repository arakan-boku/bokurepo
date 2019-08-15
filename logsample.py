import logging

# ログをファイルにはきだす
logging.basicConfig(filename='logs/testlog.log', level=logging.DEBUG)

# ログを出力する
for i in range(100):
    logging.info('warning %s %s', 'testlog', str(i))
