#!/usr/bin/env python
# -*- coding:utf-8 -*-
from jd_assistant import Assistant

if __name__ == '__main__':
    """
    重要提示：此处为示例代码之一，请移步下面的链接查看使用教程👇
    https://github.com/tychxn/jd-assistant/wiki/1.-%E4%BA%AC%E4%B8%9C%E6%8A%A2%E8%B4%AD%E5%8A%A9%E6%89%8B%E7%94%A8%E6%B3%95
    """

    sku_id = '100012043978'  # 商品id
    sku_ids = '100012043978'  # 商品id
    area = '4_50950_58472'  # 区域id
    asst = Assistant()  # 初始化
    asst.login_by_QRcode()  # 扫码登陆
    #普通商品购买
    #asst.buy_item_in_stock(sku_ids=sku_ids, area=area, wait_all=False, stock_interval=0.2)  # 根据商品是否有货自动下单
	#秒杀
    #asst.exec_seckill(sku_id=sku_id, retry=100, interval=5, num=1, fast_mode=True)
    #定时秒杀
    #asst.exec_seckill_by_time(sku_ids=sku_ids, buy_time='2020-04-14 09:59:58.000', retry=100, interval=1, num=1, fast_mode=True)

    asst.exec_seckill_mutil_process_by_time(sku_ids=sku_ids, buy_time='2020-04-13 09:59:59.750', retry=100, interval=1, num=1, fast_mode=True)

    # 6个参数：
    # sku_ids: 商品id。可以设置多个商品，也可以带数量，如：'1234' 或 '1234,5678' 或 '1234:2' 或 '1234:2,5678:3'
    # area: 地区id
    # wait_all: 是否等所有商品都有货才一起下单，可选参数，默认False
    # stock_interval: 查询库存时间间隔，可选参数，默认3秒
    # submit_retry: 提交订单失败后重试次数，可选参数，默认3次
    # submit_interval: 提交订单失败后重试时间间隔，可选参数，默认5秒
