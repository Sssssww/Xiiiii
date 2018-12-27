import configparser

# 第一步生产相应ConfigParserd的实例
cfg = configparser.ConfigParser()
# 生产实例后需要读入相应的配置文件
cfg.read("text_cfg.cfg")

sp_name = cfg.get("Smallplane","name")
print(sp_name)

