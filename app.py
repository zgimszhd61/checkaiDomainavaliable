import dns.resolver

def is_domain_available(domain):
    resolver = dns.resolver.Resolver()
    resolver.timeout = 1  # 设置单次查询超时时间为5秒
    # resolver.lifetime = 10  # 设置整个查询的最大持续时间为10秒

    try:
        resolver.resolve(domain, 'MX')
        return False  # 域名已被注册 
    except dns.resolver.NXDOMAIN:
        return True   # 域名未被注册
    except dns.resolver.Timeout:
        return False  # DNS解析超时
    except Exception as e:
        # print(f"发生错误: {e}")
        return False  # 处理其他异常情况

mlist = ['xialong.ai', 'huashu.ai', 'meiyun.ai', 'tianfei.ai', 'shengli.ai', 
         'longqing.ai', 'lixia.ai', 'jiehan.ai', 'yunmei.ai', 'shuqing.ai', 
         'feibai.ai', 'duwen.ai', 'kaisheng.ai', 'wenping.ai', 'xinqing.ai', 
         'hualong.ai', 'busheng.ai', 'tianhua.ai', 'qingshu.ai', 'feiyun.ai', 
         'xinyuan.ai', 'zhongxin.ai', 'yuehua.ai', 'qinglong.ai', 'fengyun.ai', 
         'xiaoyao.ai', 'xuanwu.ai', 'shanshui.ai', 'yuexing.ai', 'shuanghua.ai', 
         'yongheng.ai', 'xuanfeng.ai', 'yueqing.ai', 'zhuxing.ai', 'shijie.ai', 
         'yujing.ai', 'yuejian.ai', 'shijian.ai', 'xingshuai.ai', 'zhangxin.ai', 
         'huoyun.ai', 'qingyue.ai']

mlist = list(set(mlist))

for item in mlist:
    if (is_domain_available(item)):
        print("{} - {}".format(item,is_domain_available(item)))
