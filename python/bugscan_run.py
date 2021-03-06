#!/usr/bin/env python
# -*- coding: utf-8 -*-
Bugscan='https://www.bugscan.net/'
from common import *
import binascii
from decode import Decoder

from miniCurl import Curl
curl = Curl()
import util
from functools import partial
from fingerprint import FingerPrint
import hackhttp
hackhttp=hackhttp.hackhttp()
fingerprint=FingerPrint()

import sys
import util

EXP_DIR  =  '/home/leo/Desktop/bugscan0727/exp'
def get_decode(filename):
    #dekey_dic = {'expback_2078pyc_dis.py': '28221b5847a673c1d138bec680e5aab1421a9eed705aca4c316159fd2291b910', 'expback_12pyc_dis.py': 'c3ff499db0ad225bc0cbd0f9cbd7910edaa8861a1f3ebe4cc7b168d1bdad3254', 'expback_189pyc_dis.py': 'a13b6776facce2ce24b9407fe76b7d9a2ac9f97fd11b4c03da49c5dc1bfdd4ed', 'expback_77pyc_dis.py': '345095a6a09c0643bcf41007fd1311cdf4889004e886b2bca8d4881fb27a7fca', 'expback_72pyc_dis.py': '8c97d8c12ebb049684db59720d39ad8b38b0081d8cc8d022bd7768ab0bc7c699', 'expback_24pyc_dis.py': 'a27d8237a5f282cdeae742d17cd4e2ca40a686f9debe7307d414394cf8eb469a', 'expback_88pyc_dis.py': 'e77e60afe46271e855a1aaf4738acb8d2712649d7a0e38ee6de5e3cb6e102b19', 'expback_2065pyc_dis.py': '345095a6a09c0643bcf41007fd1311cdf4889004e886b2bca8d4881fb27a7fca', 'exp4.py': '253f4221df8307dfb23c39726a022382162a520739738590c39520b032c15c30', 'expback_38pyc_dis.py': '8505495a868258d1a09f88cf12b87431531bedca34a3dafc03ab58d741c0bbd7', 'expback_1756pyc_dis.py': 'ab5d21d688e5789a47b617d47dc68e48a51243b1b93d3beaf737e411310753fe', 'exp104.py': '145f01b740b46451cc03bbae9d56fe31e385aa681381a9f4ce445f7997baeff5', 'expback_76pyc_dis.py': '0d98a92bbfd99bbfbcf9419d686661ac36d55d2a7ecc0c19768b0d7b0bd9191d', 'expback_18pyc_dis.py': '38ad0c291a56f74acaee1019f24f188a7ddbb6cc51d7e4c29fa993b568404fd1', 'expback_70pyc_dis.py': 'efb1fdfd9905e92bacd3a5367c4727dc7ae722ab7f214e1434b6e25041d34190', 'expback_8pyc_dis.py': 'a13b6776facce2ce24b9407fe76b7d9a2ac9f97fd11b4c03da49c5dc1bfdd4ed', 'expback_6pyc_dis.py': '1d2d57097a9f25403de685038570b272b68e61ec0ad821f5db4ce2e380ba4f4e', 'expback_33pyc_dis.py': '48a2a41fd1a72f6feb52c058c767b31726ef9480f5624b9733cf8088e26475b6', 'expback_26pyc_dis.py': 'a27d8237a5f282cdeae742d17cd4e2ca40a686f9debe7307d414394cf8eb469a', 'expback_28pyc_dis.py': 'c3ff499db0ad225bc0cbd0f9cbd7910edaa8861a1f3ebe4cc7b168d1bdad3254', 'expback_1994pyc_dis.py': 'ffcc396606397e831f857f22b90d87ca05dd77452e7c2760df0f39d9d3f664cb', 'expback_22pyc_dis.py': '3f9632f701953df91e7b13b428d18ab7a549520831cc2a46984c83e81b933673', 'expback_23pyc_dis.py': 'e0a46b005bc3e4b63bf33f9097023d87614810c0b71a355e0934a7bc8a862f32', 'expback_1766pyc_dis.py': 'ac03b075a298860de07a3b68886ffff1dd2cec245ee4a7ea7c3e677dd9cf9cb0', 'expback_1070pyc_dis.py': '24000815b2f04e2f070d02f649539c6c6330a1bc45ad798962466966b7a220a4', 'expback_83pyc_dis.py': 'dd9108e2cb4dce78981dc247e24bd0df5c4b004058ebf271788a8e792d85a026', 'expback_100pyc_dis.py': 'a13b6776facce2ce24b9407fe76b7d9a2ac9f97fd11b4c03da49c5dc1bfdd4ed', 'expback_2112pyc_dis.py': 'ac03b075a298860de07a3b68886ffff1dd2cec245ee4a7ea7c3e677dd9cf9cb0', 'expback_29pyc_dis.py': '24000815b2f04e2f070d02f649539c6c6330a1bc45ad798962466966b7a220a4', 'expback_89pyc_dis.py': '0d4af56f54b549460eae50cb9dc579022c7e046e050fbc72242da5f616e21867', 'expback_57pyc_dis.py': 'ef632082c7620cf54876da74a1660bfb9c06eb94549b5f3bca646474000d0c46', 'expback_63pyc_dis.py': 'a13b6776facce2ce24b9407fe76b7d9a2ac9f97fd11b4c03da49c5dc1bfdd4ed', 'expback_64pyc_dis.py': 'ef632082c7620cf54876da74a1660bfb9c06eb94549b5f3bca646474000d0c46', 'expback_811pyc_dis.py': 'f8feb1e2013b989686230a93b8a543f2db83f2cc6b4dbc40f8b30bdf5e0dfeb9', 'expback_54pyc_dis.py': '4903f9969575cdef55f7b2ed2a12f89b97664e7fb5eb0898e6fd4f6775f166f3', 'expback_34pyc_dis.py': 'd289da3e7b9c736756e3429c23db20228f8e3547d3a4b540da1f86aaf22ff02f', 'expback_2083pyc_dis.py': '345095a6a09c0643bcf41007fd1311cdf4889004e886b2bca8d4881fb27a7fca', 'expback_15pyc_dis.py': 'a13b6776facce2ce24b9407fe76b7d9a2ac9f97fd11b4c03da49c5dc1bfdd4ed', 'expback_1055pyc_dis.py': '7b650aed66397b6e1ba67dfdd39c9626c4c9fec89eebf397a76caa9d0ce45d26', 'expback_60pyc_dis.py': 'a13b6776facce2ce24b9407fe76b7d9a2ac9f97fd11b4c03da49c5dc1bfdd4ed', 'expback_65pyc_dis.py': '24000815b2f04e2f070d02f649539c6c6330a1bc45ad798962466966b7a220a4', 'expback_59pyc_dis.py': '6ff51d6ad8855be91270868f2f9d9b2e225c722941906d5c0728a9409ef23b50', 'expback_2067pyc_dis.py': 'ac03b075a298860de07a3b68886ffff1dd2cec245ee4a7ea7c3e677dd9cf9cb0', 'expback_75pyc_dis.py': '3f9632f701953df91e7b13b428d18ab7a549520831cc2a46984c83e81b933673', 'expback_62pyc_dis.py': 'de92d01ce1a391792c2d4f41996a0b77c6c47605f032bdca21b0b5fd36c0f0f6', 'expback_1786pyc_dis.py': '345095a6a09c0643bcf41007fd1311cdf4889004e886b2bca8d4881fb27a7fca', 'expback_1745pyc_dis.py': '39b9843a532fed97e232f0a471ffbfb4079d8163a5e7dd52681e57c1e6520e53', 'expback_61pyc_dis.py': 'e1244c9d55465d4083a2a832fc4732472b91426238d7935d0e39126138afdac1', 'expback_39pyc_dis.py': '9a176f89756545161a807d6b5803333756eccaaad7ea2daa4e5eeb6c37a09ec0', 'expback_58pyc_dis.py': '2ec6a4bd513d71efdaaccb3aaf5c27487aef537f6091d14fcce0617c29dbf424', 'expback_2110pyc_dis.py': '33d7e04bb6b1e472eddb674398e5a3fce8abed59863e43f727ad78498ed63c27', 'expback_13pyc_dis.py': '253f4221df8307dfb23c39726a022382162a520739738590c39520b032c15c30', 'expback_1995pyc_dis.py': 'ef632082c7620cf54876da74a1660bfb9c06eb94549b5f3bca646474000d0c46', 'expback_71pyc_dis.py': 'ef632082c7620cf54876da74a1660bfb9c06eb94549b5f3bca646474000d0c46', 'expback_37pyc_dis.py': 'bce1c8cb73e24b4a1518702a3080d00aad9583c2a25f4c59b4dffb06c009a25f', 'expback_101pyc_dis.py': 'a13b6776facce2ce24b9407fe76b7d9a2ac9f97fd11b4c03da49c5dc1bfdd4ed', 'expback_25pyc_dis.py': 'ac03b075a298860de07a3b68886ffff1dd2cec245ee4a7ea7c3e677dd9cf9cb0', 'expback_16pyc_dis.py': 'f5cebead3a728f681d272e67879a393bc37e3c857076d1b09926eeee1a34739b', 'expback_45pyc_dis.py': '6eaf26b1043248ae94ca258db5d5b068a610a213aa1d2af703532163d0bd1717', 'expback_30pyc_dis.py': 'e034570d4d73b2deeed98ff76911c89ff03ae6f0cef61a09f4091b55783c18b2', 'expback_102pyc_dis.py': '1d2d57097a9f25403de685038570b272b68e61ec0ad821f5db4ce2e380ba4f4e', 'expback_19pyc_dis.py': 'bce1c8cb73e24b4a1518702a3080d00aad9583c2a25f4c59b4dffb06c009a25f', 'expback_1062pyc_dis.py': '345095a6a09c0643bcf41007fd1311cdf4889004e886b2bca8d4881fb27a7fca', 'expback_17pyc_dis.py': 'b9e36259d273b00edcbf28048f0b716e08634efaab283f693ca067fe2162f575', 'expback_36pyc_dis.py': '145f01b740b46451cc03bbae9d56fe31e385aa681381a9f4ce445f7997baeff5', 'expback_74pyc_dis.py': 'a13b6776facce2ce24b9407fe76b7d9a2ac9f97fd11b4c03da49c5dc1bfdd4ed', 'expback_641pyc_dis.py': 'bb4d873dfab45ce19dbb43ea954ddf1248a2a41fd1a72f6feb52c058c767b317', 'exp622.py': '145f01b740b46451cc03bbae9d56fe31e385aa681381a9f4ce445f7997baeff5', 'expback_73pyc_dis.py': 'c3facf1cb2752b65516b130189a508e1469f38055b509392cba7b314ffa070fb', 'expback_1071pyc_dis.py': '0d4af56f54b549460eae50cb9dc579022c7e046e050fbc72242da5f616e21867', 'expback_2066pyc_dis.py': '345095a6a09c0643bcf41007fd1311cdf4889004e886b2bca8d4881fb27a7fca', 'expback_1056pyc_dis.py': 'd876bfdb7f8cc8e92678c67ed1db7e37a95dd5ef8aaeb304cb7f8a8e86dd9dbc'}
    dekey_dic = {'expback_64pyc_dis.py': 'ef632082c7620cf54876da74a1660bfb9c06eb94549b5f3bca646474000d0c46', 'expback_2066pyc_dis.py': '345095a6a09c0643bcf41007fd1311cdf4889004e886b2bca8d4881fb27a7fca', 'expback_57pyc_dis.py': 'ef632082c7620cf54876da74a1660bfb9c06eb94549b5f3bca646474000d0c46', 'exp2366.py': '', 'exp2016.py': '', 'expback_100pyc_dis.py': 'a13b6776facce2ce24b9407fe76b7d9a2ac9f97fd11b4c03da49c5dc1bfdd4ed', 'expback_1055pyc_dis.py': '7b650aed66397b6e1ba67dfdd39c9626c4c9fec89eebf397a76caa9d0ce45d26', 'expback_45pyc_dis.py': '6eaf26b1043248ae94ca258db5d5b068a610a213aa1d2af703532163d0bd1717', 'expback_22pyc_dis.py': '3f9632f701953df91e7b13b428d18ab7a549520831cc2a46984c83e81b933673', 'expback_25pyc_dis.py': 'ac03b075a298860de07a3b68886ffff1dd2cec245ee4a7ea7c3e677dd9cf9cb0', 'expback_15pyc_dis.py': '', 'expback_28pyc_dis.py': 'c3ff499db0ad225bc0cbd0f9cbd7910edaa8861a1f3ebe4cc7b168d1bdad3254', 'expback_13pyc_dis.py': '253f4221df8307dfb23c39726a022382162a520739738590c39520b032c15c30', 'expback_61pyc_dis.py': 'e1244c9d55465d4083a2a832fc4732472b91426238d7935d0e39126138afdac1', 'expback_33pyc_dis.py': '48a2a41fd1a72f6feb52c058c767b31726ef9480f5624b9733cf8088e26475b6', 'expback_1071pyc_dis.py': '3d500608da701822cdb9d87c98f28f44eb85b9df06157f3719926283397b40f0', 'expback_101pyc_dis.py': 'a13b6776facce2ce24b9407fe76b7d9a2ac9f97fd11b4c03da49c5dc1bfdd4ed', 'expback_23pyc_dis.py': 'e0a46b005bc3e4b63bf33f9097023d87614810c0b71a355e0934a7bc8a862f32', 'expback_29pyc_dis.py': '24000815b2f04e2f070d02f649539c6c6330a1bc45ad798962466966b7a220a4', 'expback_39pyc_dis.py': '9a176f89756545161a807d6b5803333756eccaaad7ea2daa4e5eeb6c37a09ec0', 'expback_59pyc_dis.py': '6ff51d6ad8855be91270868f2f9d9b2e225c722941906d5c0728a9409ef23b50', 'expback_62pyc_dis.py': 'de92d01ce1a391792c2d4f41996a0b77c6c47605f032bdca21b0b5fd36c0f0f6', 'expback_2065pyc_dis.py': '345095a6a09c0643bcf41007fd1311cdf4889004e886b2bca8d4881fb27a7fca', 'expback_1070pyc_dis.py': '', 'expback_2112pyc_dis.py': 'ac03b075a298860de07a3b68886ffff1dd2cec245ee4a7ea7c3e677dd9cf9cb0', 'expback_98pyc_dis.py': '', 'exp1484.py': '', 'expback_82pyc_dis.py': 'a13b6776facce2ce24b9407fe76b7d9a2ac9f97fd11b4c03da49c5dc1bfdd4ed', 'expback_1056pyc_dis.py': 'd876bfdb7f8cc8e92678c67ed1db7e37a95dd5ef8aaeb304cb7f8a8e86dd9dbc', 'expback_1756pyc_dis.py': 'ab5d21d688e5789a47b617d47dc68e48a51243b1b93d3beaf737e411310753fe', 'expback_953pyc_dis.py': '', 'expback_63pyc_dis.py': 'a13b6776facce2ce24b9407fe76b7d9a2ac9f97fd11b4c03da49c5dc1bfdd4ed', 'expback_60pyc_dis.py': 'a13b6776facce2ce24b9407fe76b7d9a2ac9f97fd11b4c03da49c5dc1bfdd4ed', 'expback_83pyc_dis.py': 'dd9108e2cb4dce78981dc247e24bd0df5c4b004058ebf271788a8e792d85a026', 'expback_2083pyc_dis.py': '345095a6a09c0643bcf41007fd1311cdf4889004e886b2bca8d4881fb27a7fca', 'expback_641pyc_dis.py': 'bb4d873dfab45ce19dbb43ea954ddf1248a2a41fd1a72f6feb52c058c767b317', 'expback_1766pyc_dis.py': 'ac03b075a298860de07a3b68886ffff1dd2cec245ee4a7ea7c3e677dd9cf9cb0', 'expback_2110pyc_dis.py': '33d7e04bb6b1e472eddb674398e5a3fce8abed59863e43f727ad78498ed63c27', 'exp679.py': '', 'expback_19pyc_dis.py': '8505495a868258d1a09f88cf12b87431531bedca34a3dafc03ab58d741c0bbd7', 'expback_76pyc_dis.py': '0d98a92bbfd99bbfbcf9419d686661ac36d55d2a7ecc0c19768b0d7b0bd9191d', 'expback_70pyc_dis.py': 'efb1fdfd9905e92bacd3a5367c4727dc7ae722ab7f214e1434b6e25041d34190', 'exp2106.py': '', 'expback_72pyc_dis.py': '8c97d8c12ebb049684db59720d39ad8b38b0081d8cc8d022bd7768ab0bc7c699', 'expback_73pyc_dis.py': 'c3facf1cb2752b65516b130189a508e1469f38055b509392cba7b314ffa070fb', 'expback_89pyc_dis.py': '0d4af56f54b549460eae50cb9dc579022c7e046e050fbc72242da5f616e21867', 'expback_18pyc_dis.py': '54cf6db8b1c27e5c0c73a151a9a0ccdd7b3e2dbccc5c00c041c3479d205a62c4', 'expback_77pyc_dis.py': '345095a6a09c0643bcf41007fd1311cdf4889004e886b2bca8d4881fb27a7fca', 'expback_30pyc_dis.py': 'e034570d4d73b2deeed98ff76911c89ff03ae6f0cef61a09f4091b55783c18b2', 'exp2355.py': '', 'expback_65pyc_dis.py': '345095a6a09c0643bcf41007fd1311cdf4889004e886b2bca8d4881fb27a7fca', 'exp4.py': '', 'expback_2067pyc_dis.py': 'ac03b075a298860de07a3b68886ffff1dd2cec245ee4a7ea7c3e677dd9cf9cb0', 'expback_35pyc_dis.py': '', 'expback_6pyc_dis.py': '3f9632f701953df91e7b13b428d18ab7a549520831cc2a46984c83e81b933673', 'expback_1994pyc_dis.py': 'ffcc396606397e831f857f22b90d87ca05dd77452e7c2760df0f39d9d3f664cb', 'expback_1062pyc_dis.py': '345095a6a09c0643bcf41007fd1311cdf4889004e886b2bca8d4881fb27a7fca', 'expback_1786pyc_dis.py': '345095a6a09c0643bcf41007fd1311cdf4889004e886b2bca8d4881fb27a7fca', 'expback_58pyc_dis.py': '2ec6a4bd513d71efdaaccb3aaf5c27487aef537f6091d14fcce0617c29dbf424', 'expback_24pyc_dis.py': 'a27d8237a5f282cdeae742d17cd4e2ca40a686f9debe7307d414394cf8eb469a', 'exp2357.py': '', 'expback_34pyc_dis.py': 'd289da3e7b9c736756e3429c23db20228f8e3547d3a4b540da1f86aaf22ff02f', 'exp622.py': '', 'expback_17pyc_dis.py': 'b9e36259d273b00edcbf28048f0b716e08634efaab283f693ca067fe2162f575', 'expback_36pyc_dis.py': '145f01b740b46451cc03bbae9d56fe31e385aa681381a9f4ce445f7997baeff5', 'expback_54pyc_dis.py': '4903f9969575cdef55f7b2ed2a12f89b97664e7fb5eb0898e6fd4f6775f166f3', 'expback_12pyc_dis.py': 'e3bb69fcc78187a0039fccb03c46298456d5ffb095a1203945c91c59ca3e1993', 'expback_71pyc_dis.py': 'ef632082c7620cf54876da74a1660bfb9c06eb94549b5f3bca646474000d0c46', 'expback_8pyc_dis.py': 'f8302acee10371dc21ac9029b3a35f45bcdc1b3ecfefefb25771bac202ac32ec', 'expback_811pyc_dis.py': 'f8feb1e2013b989686230a93b8a543f2db83f2cc6b4dbc40f8b30bdf5e0dfeb9', 'expback_75pyc_dis.py': '3f9632f701953df91e7b13b428d18ab7a549520831cc2a46984c83e81b933673', 'exp1962.py': '', 'expback_1995pyc_dis.py': 'ef632082c7620cf54876da74a1660bfb9c06eb94549b5f3bca646474000d0c46', 'expback_1745pyc_dis.py': '39b9843a532fed97e232f0a471ffbfb4079d8163a5e7dd52681e57c1e6520e53', 'exp849.py': '', 'expback_16pyc_dis.py': 'f5cebead3a728f681d272e67879a393bc37e3c857076d1b09926eeee1a34739b', 'expback_88pyc_dis.py': 'e77e60afe46271e855a1aaf4738acb8d2712649d7a0e38ee6de5e3cb6e102b19', 'expback_2078pyc_dis.py': '28221b5847a673c1d138bec680e5aab1421a9eed705aca4c316159fd2291b910', 'expback_74pyc_dis.py': 'a13b6776facce2ce24b9407fe76b7d9a2ac9f97fd11b4c03da49c5dc1bfdd4ed', 'expback_26pyc_dis.py': 'bb4d873dfab45ce19dbb43ea954ddf1248a2a41fd1a72f6feb52c058c767b317', 'expback_189pyc_dis.py': 'a13b6776facce2ce24b9407fe76b7d9a2ac9f97fd11b4c03da49c5dc1bfdd4ed', 'expback_37pyc_dis.py': 'bce1c8cb73e24b4a1518702a3080d00aad9583c2a25f4c59b4dffb06c009a25f', 'expback_102pyc_dis.py': '1d2d57097a9f25403de685038570b272b68e61ec0ad821f5db4ce2e380ba4f4e', 'expback_38pyc_dis.py': '8505495a868258d1a09f88cf12b87431531bedca34a3dafc03ab58d741c0bbd7','expback_1054pyc_dis.py':'ac03b075a298860de07a3b68886ffff1dd2cec245ee4a7ea7c3e677dd9cf9cb0'}

    try:
        de_key = dekey_dic[filename]
    except:
        return ''
    decode = Decoder(binascii.a2b_hex(de_key)).decode
    return decode 

sys.path.append(EXP_DIR)
_G = {
    'scanport':False,
    'subdomain': False,
    'target': 'www.zgqmlt.com',
    'disallow_ip':['127.0.0.1'],
    'kv' : {},
    #'user_dict':'http://192.168.0.158/1.txt'
    #'pass_dict':'http://192.168.0.158/1.txt'
    }

util._G = _G

import sys

def debug(fmt, *args):
    print(fmt % args)
    sys.stdout.flush()

LEVEL_NOTE = 0
LEVEL_INFO =1
LEVEL_WARNING = 2
LEVEL_HOLE = 3

def _problem(level, body, uuid=None, log=[]):
    debug('[LOG] <%s> %s (uuid=%s)', ['note', 'info', 'warning', 'hole'][level], body,str(uuid))
    if log:
        if isinstance(log,dict):
            log=[log]
        for l in log:
            print l['response'][:200]
            sys.stdout.flush()

            
security_note = partial(_problem,LEVEL_NOTE)
security_info = partial(_problem,LEVEL_INFO)
security_warning = partial(_problem,LEVEL_WARNING)
security_hole = partial(_problem,LEVEL_HOLE)

def task_push(service, arg, uuid = None, target=None):
    if uuid is None:
        uuid = str(arg)
        
    debug('[JOB] <%s> %s (%s/%s)', service, arg, uuid, target)
    import os
    for path, subdirs, files in os.walk(EXP_DIR):
        for fname in files:
            if not fname.endswith('.py'): continue
	    #print fname
            pname = fname[:-3]
            #try:
            # print pname
            plg = __import__(pname)
            # print plg.__dict__.keys()
            #mod = plg.__dict__[name]
            mod = plg
            mod.decode = get_decode(fname)
            mod.curl = curl
            mod.security_note = security_note
            mod.security_info = security_info
            mod.security_warning = security_warning
            mod.security_hole = security_hole
            mod.util = util
            res = None
            # if no assign  -> res = (True, arg)
            if not mod.__dict__.has_key('assign'):
               res = (True, arg)
            else:
               # if assign Success  ->   res = (True, arg)
               # if assign fail     ->   res = None
               res = mod.assign(service, arg)


            try:
                mod.audit(res[1])
            except Exception as e:
                pass
            #except Exception as e:
            #    pass
            
if __name__ == '__main__':
    f = open('target.txt')
    for target in f:
        target = target.strip()
        #print target
        task_push('www',target,'uuidxxxxxxxxxxxxxxxxx',target)
