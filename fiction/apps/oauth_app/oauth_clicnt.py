# -*- coding: utf-8 -*-
__author__ = 'MeiHai'
__date__ = '2018/7/26 17:29'
import json
from urllib.parse import urlencode,urlparse,parse_qs
from urllib.request import urlopen
class OAuth_QQ():

    def __init__(self, client_id, client_key, redirect_uri):
        self.client_id = client_id
        self.client_key = client_key
        self.redirect_uri = redirect_uri

    def get_auth_url(self):
        '''

        获取授权页面的网址
        '''

        params = {
            'client_id':self.client_id,
            'response_type':'code',
            'redirect_uri':self.redirect_uri,
            'scop' : 'get_user_info',
            'state': 1
        }
        url = 'https://graph.qq.com/oauth2.0/authorize?%s' % urlencode(params)

        return url

    def get_access_token(self, code):
        """根据code获取access_token"""
        params = {'grant_type': 'authorization_code',
                  'client_id': self.client_id,
                  'client_secret': self.client_key,
                  'code': code,
                  'redirect_uri': self.redirect_uri}
        url = 'https://graph.qq.com/oauth2.0/token?%s' % urlencode(params)

        # 访问该网址，获取access_token
        response = urlopen(url).read().decode('utf-8')
        result = parse_qs(response, True)
        print(result)
        access_token = (result.get('access_token'))[0]
        self.access_token = access_token
        return access_token

    def get_open_id(self):
        """获取QQ的OpenID"""
        print(self.access_token,'===========================')
        params = {'access_token': self.access_token}
        url = 'https://graph.qq.com/oauth2.0/me?%s' % urlencode(params)
        response = urlopen(url).read().decode('utf-8')
        print(response,'--------------------------------')
        v_str = str(response)[9:-3]  # 去掉callback的字符
        v_json = json.loads(v_str)
        openid = v_json['openid']
        self.openid = openid
        return openid

    def get_qq_info(self):
        """获取QQ用户的资料信息"""
        params = {'access_token': self.access_token,
                  'oauth_consumer_key': self.client_id,
                  'openid': self.openid}
        url = 'https://graph.qq.com/user/get_user_info?%s' % urlencode(params)

        response = urlopen(url).read().decode('utf-8')
        return json.loads(response)


