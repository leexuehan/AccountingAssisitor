from configparser import ConfigParser


class ConfigFileUtils(object):
    @staticmethod
    def read_sort_list(sort_name):
        conf = ConfigParser()
        conf.read("..\\conf\\sortlist.conf", encoding='utf-8')
        names = conf.options(sort_name)
        return names


    @staticmethod
    def add_item_into_sorts(item_name, sort_name):
        conf = ConfigParser()
        conf.read("..\\conf\\sortlist.conf", encoding='utf-8')
        conf.set(sort_name, item_name, '')
        conf.write(open("..\\conf\\sortlist.conf", "w", encoding='utf-8'))

    @staticmethod
    def delete_item_from_sorts(item_name, sort_name):
        conf = ConfigParser()
        conf.read("..\\conf\\sortlist.conf", encoding='utf-8')
        conf.remove_option(sort_name, item_name)
        conf.write(open("..\\conf\\sortlist.conf", "w", encoding='utf-8'))


if __name__ == '__main__':
    ConfigFileUtils.add_item_into_sorts('面面膜', 'coals')
    ConfigFileUtils.delete_item_from_sorts('洗中块1', 'coals')

# age = conf.get("section1", "age")
# print(age)

# #获取所有的section
# sections = conf.sections()
# print(sections)
#
# #写配置文件
#
# # 更新指定section, option的值
# conf.set("section2", "port", "8081")
#
# # 写入指定section, 增加新option的值
# conf.set("section2", "IEPort", "80")
#
# # 添加新的 section
# conf.add_section("new_section")
# conf.set("new_section", "new_option", "http://www.cnblogs.com/tankxiao")
#
# # 写回配置文件
# conf.write(open("c:\\test.conf","w"))
