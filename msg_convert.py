# -*- coding: utf-8 -*-
__author__ = 'haoyuewen'

from xml.dom import minidom
import re

class XmlDomainConvert:

    def convert(self, xml_str, domain):

        messageDoc = minidom.parseString(xml_str)
        messageEle = messageDoc.documentElement
        toAttr = messageEle.attributes['to']
        fromAttr = messageEle.attributes['from']
        toVal = toAttr.value
        fromVal = fromAttr.value

        domain = domain

        p = re.compile('[@|/]')

        tmp_to_arr = p.split(toVal)
        if len(tmp_to_arr) == 1:
            toValNew = domain
        else:
            tmp_to_arr[1] = domain
            toValNew = tmp_to_arr[0] + '@' + tmp_to_arr[1] + ((len(tmp_to_arr) == 3) and ('/' + tmp_to_arr[2]) or '')

        tmp_from_arr = p.split(fromVal)
        if len(tmp_from_arr) == 1:
            fromValNew = domain
        else:
            tmp_from_arr[1] = domain
            fromValNew = tmp_from_arr[0] + '@' + tmp_from_arr[1] + ((len(tmp_from_arr) == 3) and ('/' + tmp_from_arr[2]) or '')

        toAttr.value = toValNew
        fromAttr.value = fromValNew

        return messageEle.toxml()

if __name__ == '__main__':
    xdc = XmlDomainConvert()
    xml_str = '''
        <message from="spark-chat.cadillac-1.com" to="admin@spark-chat.cadillac-1.com"><body>服务器或插件更新被找到: Openfire 3.10.0</body></message>
    '''
    print xdc.convert(xml_str, 'wechat.cadillac-1.com');