# coding=utf-8

class Facebook:
        class Auto_Bot:
            try:
                def __init__(self):
                    try:
                        self.Installer()
                        self.username = ''
                        self.commented = []
                        self.password = ''
                        self.logged = False
                        self.friends = ''
                        self.Browse_Profile = ''
                        self.group_list = ''
                        self.pages_list = ''
                        self.account_name = ''
                        self.account_url = ''
                        self.sys.stdout.write("\x1b]2;TPCT Facebook Auto Bot Version 1\x07")
                        self.plateform_check()
                        def cls():
                            import os
                            os.system('cls' if os.name == 'nt' else 'clear')
                        cls()
                        self.Service_Start()
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except Exception as e:
                        pass

                Coder = '''
                    _____ ____   ____   ___ _____  _____ ____   ____ _____
                   |  ___| __ ) | __ ) / _ \_   _ |_   _|  _ \ / ___|_   _|
                   | |_  |  _ \ |  _ \| | | || |    | | | |_) | |     | |
                   |  _| | |_)  | |_) | |_| || |    | | |  __/| |___  | |
                   |_|   |____/ |____/ \___/ |_|    |_| |_|    \____| |_|
                                    Th3 Professional Cod3r
                   Github: https://github.com/TPCT
                   Facebook: https://www.facebook.com/Taylor.Ackerley.9\n'''

                class Installer:
                    import os, shutil
                    def __init__(self):
                        self.Admin_Rights()
                        self.Import_Checker()

                    def Admin_Rights(self):
                        try:
                            import os, sys, platform
                            if str(platform.system()).lower().startswith('linux'):
                                open('/etc/Mod', 'w+')
                                os.unlink('/etc/Mod')
                            elif str(platform.system()).lower().startswith('windows'):
                                open('c:/Mod', 'w+')
                                os.unlink('c:/Mod')
                            else:
                                open('/etc/Mod', 'w+')
                                os.unlink('/etc/Mod')
                        except KeyboardInterrupt as e:
                            self.os._exit(1)
                        except Exception as e:
                            e = e.args
                            if e[0] == 13:
                                print('[+] Sorry You Need To Use Script As Admin Script Will Exit')
                                sys.exit(1)
                            else:
                                pass

                    def Import_Checker(self):
                        try:
                            __import__('imp').find_module('robobrowser')
                        except ImportError:
                            import pip
                            pip.main(['install', 'robobrowser'])
                            pass

                import time, random, re, string, sys, warnings, os, pip, traceback, math, getpass, pickle, \
                    signal, platform, pickle, robobrowser, requests, tarfile, zipfile
                from robobrowser import RoboBrowser
                browser = ''
                Browser = ''

                def plateform_check(self):
                    if str(self.platform.system()).lower().startswith('linux'):
                        browser = self.RoboBrowser(
                            user_agent='Mozilla/5.0 (Macintosh; PPC Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0',
                            multiplier=True,
                            allow_redirects=True, history=True, parser='lxml')
                        self.browser = browser
                    elif str(self.platform.system()).lower().startswith('windows'):
                        browser = self.RoboBrowser(
                            user_agent='Mozilla/5.0 (Macintosh; PPC Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0',
                            multiplier=True,
                            allow_redirects=True, history=True, parser='html.parser')
                        self.browser = browser
                    else:
                        browser = self.RoboBrowser(
                            user_agent='Mozilla/5.0 (Macintosh; PPC Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0',
                            multiplier=True,
                            allow_redirects=True, history=True, parser='lxml')
                        self.browser = browser

                def login(self):
                    try:
                        if self.logged and str(self.username).strip().__len__() > 0 and str(
                                self.password).strip().__len__() > 0:
                            self.browser.open('https://m.facebook.com/login.php')
                            for a in self.browser.find_all('a'):
                                if str(a['href']).__contains__('/a/language.php?l=en_GB'):
                                    self.browser.open('https://m.facebook.com' + a['href'])
                                    break
                            form = self.browser.get_form('login_form')
                            form['email'] = self.username
                            form['pass'] = self.password
                            self.browser.submit_form(form)
                            if self.browser.find_all('div', {'class': 'z'}):
                                print(
                                    '[-][error] Something went wrong : ' +
                                    self.browser.find_all('div', {'class': 'z'})[
                                        0].text)
                                self.os._exit(1)
                                pass
                            elif str(self.browser.url).__contains__('checkpoint'):
                                print(
                                    '[-][error] Something went wrong : Check your account now it might be blocked')
                                self.os._exit(1)
                                pass
                            else:
                                self.browser.open('https://m.facebook.com/home.php?_rdr')
                                if self.browser.find('div', {'id': 'header'}):
                                    self.logged = True
                                    self.account_name_gen()
                                    return True
                                else:
                                    print('[-][Not Logged] Service Stopped System Will Close')
                                    return False
                                    self.os._exit(1)
                        else:
                            print('[-][Not Logged] Service Stopped System Will Close')
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except Exception as e:
                        print('[-][Not Logged] Service Stopped ' + str(e) + ' System Will Close')
                        self.os._exit(1)
                        pass

                def Login(self, username=None, password=None):
                    try:
                        if str(self.platform.system()).lower().startswith('linux'):
                            browser = self.RoboBrowser(
                                user_agent='Mozilla/5.0 (Macintosh; PPC Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0',
                                multiplier=True,
                                allow_redirects=True, history=True, parser='lxml')
                        elif str(self.platform.system()).lower().startswith('windows'):
                            browser = self.RoboBrowser(
                                user_agent='Mozilla/5.0 (Macintosh; PPC Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0',
                                multiplier=True,
                                allow_redirects=True, history=True, parser='html.parser')
                        else:
                            browser = self.RoboBrowser(
                                user_agent='Mozilla/5.0 (Macintosh; PPC Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0',
                                multiplier=True,
                                allow_redirects=True, history=True, parser='lxml')
                        if str(username).strip().__len__() > 0 and str(password).strip().__len__() > 0:
                            browser.open('https://m.facebook.com/login.php')
                            for a in browser.find_all('a'):
                                if str(a['href']).__contains__('/a/language.php?l=en_GB'):
                                    browser.open('https://m.facebook.com' + a['href'])
                                    break
                            form = browser.get_form('login_form')
                            form['email'] = username
                            form['pass'] = password
                            browser.submit_form(form)
                            if browser.find_all('div', {'class': 'z'}):
                                print(
                                    '[-][error] Something went wrong : ' +
                                    browser.find_all('div', {'class': 'z'})[
                                        0].text)
                                self.os._exit(1)
                                pass
                            elif str(browser.url).__contains__('checkpoint'):
                                print(
                                    '[-][error] Something went wrong : Check your account now it might be blocked')
                                self.os._exit(1)
                                pass
                            else:
                                browser.open('https://m.facebook.com/home.php?_rdr')
                                if browser.find('div', {'id': 'header'}):
                                    print('[+][Logged] Service Started successfully')
                                    print('[+][start] Fetching Your Account Name')
                                    browser.open('https://m.facebook.com/profile.php')
                                    user = \
                                        browser.find_all('div', {'id': 'm-timeline-cover-section'})[0].find_all(
                                            'div')[
                                            2].find_all('div')[0].find_all('div')[2].find_all('strong')[0].text
                                    print('[+][Welcome] ' + str(user) + '')
                                    self.logged = True
                                    self.username = username
                                    self.password = password
                                    print('[+][Done] Fetching Your Account Name')
                                    return True
                                else:
                                    print('[-][Not Logged] Service Stopped System Will Close')
                                    self.os._exit(1)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except Exception as e:
                        print('[-][Not Logged] Service Stopped ' + str(
                            self.traceback.print_exc()) + ' System Will Close')
                        self.os._exit(1)
                        pass

                def friend_list_gen(self):
                    try:
                        if self.logged:
                            friends = {}
                            self.browser.open(
                                'https://m.facebook.com/friends/center/friends/?fb_ref=fbm&ref_component=mbasic_bookmark&ref_page=XMenuController')
                            while 1:
                                try:
                                    if self.browser.find('div', {'id': 'header'}):
                                        for item in self.browser.find_all('a'):
                                            if str(item['href']).__contains__(
                                                    '/friends/hovercard/mbasic/?uid='):
                                                if not str(item).split('>')[1].split('<')[0] in friends:
                                                    friends[str(item).split('>')[1].split('<')[0]] = item[
                                                        'href']
                                                else:
                                                    if not friends[str(item).split('>')[1].split('<')[0]] == \
                                                            item[
                                                                'href']:
                                                        friends[
                                                            str(item).split('>')[1].split('<')[0] + str(
                                                                self.random.randint(0, 999999999))] = item[
                                                            'href']
                                            elif str(item['href']).__contains__(
                                                    '/friends/center/friends/?ppk='):
                                                self.browser.open('http://m.facebook.com' + item['href'])
                                        if not str(self.browser.parsed).__contains__(
                                                '/friends/center/friends/?ppk='):
                                            break
                                    else:
                                        print('[-][Not Logged] Service Stopped')
                                        self.os._exit(1)
                                        break
                                    pass
                                except KeyboardInterrupt as e:
                                    self.os._exit(1)
                                except:
                                    break
                                    pass
                            m = {}
                            for friend_name, friend_url in friends.items():
                                self.browser.open('https://m.facebook.com' + friend_url)
                                for hovera in self.browser.find_all('a'):
                                    if str(hovera['href']).endswith('hovercard'):
                                        m[friend_name] = hovera['href']
                                        break
                                        pass
                                    pass
                            friends = m
                            if self.logged and friends.__len__() > 0:
                                print('[+][Log] Friends Number: [' + str(friends.__len__()) + ']')
                                return friends
                            elif self.logged and friends.__len__() == 0:
                                print('[+][Log] Friends Number: [0] Service will stop')
                                self.os._exit(1)
                            else:
                                pass
                                pass
                        else:
                            print('[-][Not Logged] Service Stopped')
                            pass
                        self.os._exit(1)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass

                def encrypter(self, data=None, key=0):
                    Encrypted_Data = ''
                    if key <= 10:
                        for c in data:
                            shipper = round(key * 4 * (4 / 3) * (5 / 4) * (1 / 3) * (5) + 10)
                            salt = (ord(c) * 4) - shipper
                            pepper = round(salt + key)
                            Encrypted_Data += chr(pepper)
                        return Encrypted_Data
                    else:
                        for c in data:
                            shipper = round(key * (1 / 4) * (4 / 3) * (5 / 4) * (1 / 3) * (1 / 5) - 5)
                            salt = (ord(c) * 4) + (1 / 4) - shipper
                            pepper = round(salt + key * (1 / key - 10))
                            Encrypted_Data += chr(pepper)
                        return Encrypted_Data

                def random_word(self, length):
                    return ''.join(
                        self.random.choice(self.string.ascii_lowercase.lower()) for i in range(length))

                def Facebook_Accounts_Maker(self, Number=0, File_To_Save=None):
                    try:
                        self.browser.open('https://m.facebook.com/reg')
                        form = self.browser.get_form(action='https://m.facebook.com/reg/')
                        form['firstname'].value = 'jackie'
                        form['lastname'].value = 'eslam'
                        form['reg_email__'].value = 'soloam@extremail.ru'
                        form['sex'].value = '1'
                        form['birthday_day'].value = '14'
                        form['birthday_month'].value = '8'
                        form['birthday_year'].value = '1998'
                        form['reg_passwd__'].value = 'Cod3r@Cod3r'
                        self.browser.submit_form(form)
                        print(self.browser.url)
                        open('Mono.html', 'w+').write(str(self.browser.parsed))
                    except:
                        print(traceback.print_exc())  # Working on it

                def unfriend_all(self, sleep_thread):
                    if self.logged:
                        try:
                            print('[+][Log][start] unfriend all Service')
                            friends = self.friends.items()
                            for friend_name, friend_url in friends:
                                self.browser.open('https://m.facebook.com' + friend_url)
                                if str(self.browser.url).__contains__('profile.php?id='):
                                    try:
                                        self.browser.open(
                                            'https://m.facebook.com/removefriend.php?friend_id=' +
                                            str(self.browser.url).split('=')[
                                                1].split('&')[0] + '&unref=profile_gear')
                                        form = self.browser.get_form(action='/a/removefriend.php')
                                        self.browser.submit_form(form,
                                                                 submit='https://m.facebook.com' + form.action)
                                        print('[+][Log][success] unfriend all Service :[' + friend_name + ']')
                                        break
                                        pass
                                    except KeyboardInterrupt:
                                        self.os._exit(1)
                                    except Exception as e:
                                        print('[+][Log][failed] unfriend all Service :[' + friend_name + ']')
                                    pass
                                else:
                                    for a in self.browser.find_all('div', {'id': 'm-timeline-cover-section'})[
                                        0].find_all('a'):
                                        try:
                                            if str(a['href']).__contains__('/messages/thread/'):
                                                self.browser.open(
                                                    'https://m.facebook.com/removefriend.php?friend_id=' +
                                                    str(a['href']).split('/')[
                                                        3] + '&unref=profile_gear')
                                                form = self.browser.get_form(action='/a/removefriend.php')
                                                self.browser.submit_form(form,
                                                                         submit='https://m.facebook.com' + form.action)
                                                print(
                                                    '[+][Log][success] unfriend all Service :[' + friend_name + ']')
                                                break
                                                pass
                                            else:
                                                pass
                                        except KeyboardInterrupt:
                                            self.os._exit(1)
                                        except Exception as e:

                                            print(
                                                '[+][Log][failed] unfriend all Service :[' + friend_name + ']')
                                        pass
                                    pass
                                pass
                            print('[+][Log][Done] unfriend all Service')
                            self.os._exit(1)
                            pass
                        except KeyboardInterrupt:
                            self.os._exit(1)
                        except Exception as e:
                            print('[-][error] Service Stopped ' + str(e) + ' System Will Close')
                            pass
                    else:
                        print('[-][Not Logged] Wall Message Service Stopped')
                        self.os._exit(1)
                        pass

                def decrypter(self, data=None, key=0):
                    import re
                    Decrypted_Data = ''
                    if key <= 10:
                        for c in data:
                            c = ord(c)
                            shipper = round(key * 4 * (4 / 3) * (5 / 4) * (1 / 3) * (5) + 10)
                            salt = (c - key) + shipper
                            pepper = round(salt / 4)
                            checked = re.sub('/[\x00-\x1F\x80-\xFF]/', '', chr(pepper))
                            Decrypted_Data += checked
                        return Decrypted_Data
                    else:
                        for c in data:
                            c = ord(c)
                            shipper = round(key * (1 / 4) * (4 / 3) * (5 / 4) * (1 / 3) * (1 / 5) - 5)
                            salt = c - (key * (1 / key - 10)) - 0.5 + shipper
                            pepper = round(salt / 4)
                            checked = re.sub('/[\x00-\x1F\x80-\xFF]/', '', chr(pepper))
                            Decrypted_Data += checked
                    return Decrypted_Data

                def group_list_gen(self):
                    try:
                        if self.logged:
                            group_list = {}
                            self.browser.open('https://m.facebook.com/groups')
                            while str(self.browser.find_all('div')[7].find_all('ul')[0].find_all('a')[len(
                                    self.browser.find_all('div')[7].find_all('ul')[0].find_all(
                                        'a')) - 1].text).lower() == 'see all':
                                for a in self.browser.find_all('div')[7].find_all('ul')[0].find_all('a'):
                                    if str(a.text).lower() != 'see all':
                                        if a.text not in group_list or group_list[a.text] != a['href']:
                                            group_list[a.text] = a['href']
                                        elif a.text in group_list or group_list[a.text] != a['href']:
                                            group_list[a.text + str(self.random.randint(0, 9999999))] = a[
                                                'href']
                                        else:
                                            pass
                                    else:
                                        self.browser.open('https://m.facebook.com' + a['href'])
                                        pass
                                    pass
                                pass
                            for a in self.browser.find_all('div')[7].find_all('ul')[0].find_all('a'):
                                if str(a.text).lower() != 'see all':
                                    if a.text not in group_list or group_list[a.text] != a['href']:
                                        group_list[a.text] = a['href']
                                    elif a.text in group_list or group_list[a.text] != a['href']:
                                        group_list[a.text + str(self.random.randint(0, 9999999))] = a['href']
                                    else:
                                        pass
                                else:
                                    self.browser.open(a['href'])
                                    pass
                                pass
                            print('[+][Log] Groups Number : [' + str(group_list.__len__()) + ']')
                            return group_list
                            pass
                        else:
                            print('[-][Not Logged] Service Stopped')
                            pass
                        self.os._exit(1)
                        pass
                    except Exception as e:
                        pass

                def account_name_gen(self):
                    try:
                        if self.logged:
                            self.browser.open('https://m.facebook.com/profile.php')
                            self.account_url = 'https://m.facebook.com' + \
                                               self.browser.find_all('div', {'id': 'header'})[0].find_all(
                                                   'div')[
                                                   0].find_all(
                                                   'a')[
                                                   2][
                                                   'href'].split('?')[0]
                            self.account_name = \
                                browser.find_all('div', {'id': 'm-timeline-cover-section'})[0].find_all('div')[
                                    2].find_all('div')[0].find_all('div')[2].find_all('strong')[0].text
                        else:
                            print('[-][Not Logged] Service Stopped')
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass

                def pages_list_gen(self):
                    try:
                        if self.logged:
                            pages_list = {}
                            see_more = []
                            m = 11
                            account = str(self.account_url).split('?')[0].split('/')[3]
                            self.browser.open('https://m.facebook.com/' + account + '?v=likes')
                            for div in self.browser.find_all('div', {'id': 'root'})[0].find_all('div')[
                                0].find_all(
                                'div'):
                                if div.find_all('h4', {'class': 'bv i'}):
                                    for a in div.find_all('a'):
                                        try:
                                            if str(a['href']).split('?')[1] == 'fref=none':
                                                if a.text not in pages_list or pages_list[a.text] != a['href']:
                                                    pages_list[a.text] = a['href']
                                                elif a.text in pages_list or pages_list[a.text] != a['href']:
                                                    pages_list[a.text + str(self.random.randint(0, 9999999))] = \
                                                        a[
                                                            'href']
                                                else:
                                                    pass
                                            else:
                                                if str(a.text).lower() == 'see more':
                                                    see_more.append('https://m.facebook.com' + a['href'])
                                        except KeyboardInterrupt as e:
                                            self.os._exit(1)
                                        except:
                                            pass
                                        pass
                                    pass
                                elif div.find_all('h4'):
                                    for a in div.find_all('a'):
                                        try:
                                            if str(a['href']).split('?')[1] == 'fref=none':
                                                if a.text not in pages_list or pages_list[a.text] != a['href']:
                                                    pages_list[a.text] = a['href']
                                                elif a.text in pages_list or pages_list[a.text] != a['href']:
                                                    pages_list[a.text + str(self.random.randint(0, 9999999))] = \
                                                        a[
                                                            'href']
                                                else:
                                                    pass
                                            else:
                                                if str(a.text).lower() == 'see more':
                                                    see_more.append('https://m.facebook.com' + a['href'])
                                        except KeyboardInterrupt as e:
                                            self.os._exit(1)
                                        except:
                                            pass
                                        pass
                                    pass
                                else:
                                    pass

                            for see in see_more:
                                url = str(see).split('=')
                                url.pop()
                                url = "=".join(url)
                                self.browser.open(url + '=' + str(m))
                                while len(self.browser.find_all('div', {'class': 'bn'})) > 1:
                                    for div in self.browser.find_all('div', {'class': 'bn'}):
                                        for a in div.find_all('a'):
                                            try:
                                                if str(a['href']).split('?')[1] == 'fref=none':
                                                    if a.text not in pages_list or pages_list[a.text] != a[
                                                        'href']:
                                                        pages_list[a.text] = a['href']
                                                    elif a.text in pages_list or pages_list[a.text] != a[
                                                        'href']:
                                                        pages_list[
                                                            a.text + str(self.random.randint(0, 9999999))] = \
                                                            a[
                                                                'href']
                                                    else:
                                                        pass
                                                else:
                                                    pass
                                            except KeyboardInterrupt as e:
                                                self.os._exit(1)
                                            except:
                                                pass
                                            pass
                                        pass
                                    m += 11
                                    self.browser.open(url + '=' + str(m))
                                    pass
                                pass
                            print('[+][Log] Pages Number : [' + str(pages_list.__len__()) + ']')
                            return pages_list
                        else:
                            print('[-][Not Logged] Service Stopped')
                            pass
                        self.os._exit(1)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass

                def Comments_Fetcher(self):
                    print('[+][Start] Fetching Commented Lists')
                    try:
                        read = open('F_PG.DAT', 'r+').read()
                        for r in read.split("\n"):
                            if str(self.decrypter(r, 10)).strip().replace(' ', '').__len__() > 0:
                                self.commented.append(self.decrypter(r, 10))
                    except FileNotFoundError:
                        open('F_PG.DAT', 'w+').read()
                    except Exception as e:
                        pass
                    try:
                        read = open('F_GP.DAT', 'r+').read()
                        for r in read.split("\n"):
                            if str(self.decrypter(r, 11)).strip().replace(' ', '').__len__() > 0:
                                self.commented.append(self.decrypter(r, 11))
                    except FileNotFoundError:
                        open('F_GP.DAT', 'w+').read()
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass
                    try:
                        read = open('F_FBF.DAT', 'r+').read()
                        for r in read.split("\n"):
                            if str(self.decrypter(r, 12)).strip().replace(' ', '').__len__() > 0:
                                self.commented.append(self.decrypter(r, 12))
                    except FileNotFoundError:
                        open('F_FBF.DAT', 'w+').read()
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass
                    print('[+][Done] Fetching Commented Lists Service')
                    pass

                def url_encoder(self, message):
                    try:
                        urls = self.re.findall(
                            'http[s]?://(?:[a-za-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fa-f][0-9a-fa-f]))+',
                            message)
                        l = [self.string.ascii_lowercase, self.string.ascii_uppercase]
                        ran = l[self.random.randint(0, 1)]
                        for url in urls:
                            encrypted = ''.join(
                                self.random.choice(ran) for _ in range(self.random.randint(7, 34)))
                            self.browser.open(
                                'http://tinyurl.com/create.php?source=indexpage&url=' + url + '&submit=make+tinyurl!&alias=' + encrypted)
                            message = message.replace(url,
                                                      self.browser.find('div', {'id': 'copyinfo'})[
                                                          'data-clipboard-text'])
                            return message
                        return message
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        return message
                    pass

                def message_all_friends(self, message=None, sleep_thread=0):
                    try:
                        if self.logged:
                            print('[+][Log][start] Post Message To All Service')
                            friends = self.friends
                            for friend_name, friend_url in friends.items():
                                self.browser.open('https://m.facebook.com' + friend_url)
                                for a in self.browser.find_all('a'):
                                    try:
                                        if str(a['href']).__contains__('/messages/thread'):
                                            self.browser.open('https://m.facebook.com' + a['href'])
                                            break
                                        else:
                                            pass
                                        pass
                                    except TypeError:
                                        pass
                                    except KeyboardInterrupt as e:
                                        self.os._exit(1)
                                    except:
                                        pass
                                try:
                                    message = self.url_encoder(message)
                                    self.browser.find_all('textarea')[0].insert(0, message)
                                    form = self.browser.get_forms()[1]
                                    form.action = 'https://m.facebook.com' + form.action
                                    self.browser.submit_form(form, submit=form.submit_fields['send'])
                                    print(
                                        '[+][Log][success] Post Message To All Service :[' + friend_name + ']')
                                    pass
                                except TypeError:
                                    pass
                                except KeyboardInterrupt as e:
                                    self.os._exit(1)
                                except:
                                    try:
                                        message = self.url_encoder(message)
                                        self.browser.find_all('textarea')[0].insert(0, message)
                                        form = self.browser.get_forms()[1]
                                        form.action = 'https://m.facebook.com' + form.action
                                        self.browser.submit_form(form, submit=form.submit_fields['send'])
                                        print(
                                            '[+][Log][success] Post Message To All Service :[' + friend_name + ']')
                                        pass
                                    except TypeError:
                                        pass
                                    except KeyboardInterrupt as e:
                                        self.os._exit(1)
                                    except Exception as e:
                                        print(
                                            '[+][Log][failed] Post Message To All Service :[' + friend_name + ']')
                                        pass
                                    pass
                                self.time.sleep(sleep_thread)
                                pass
                            self.os._exit(1)
                            print('[+][Log][Done] Post Message To All Service')
                            pass
                        else:
                            print('[-][Not Logged] Service Stopped')
                            pass
                        self.os._exit(1)
                        print('[+][Done] Post To All Friends Messages')
                        pass
                    except Exception as e:
                        pass

                def wall_message_for_all_friends(self, message=None, sleep_thread=0):
                    try:
                        if self.logged:
                            friends = self.friends
                            for friend_name, friend_url in friends.items():
                                self.browser.open('https://m.facebook.com' + friend_url)
                                try:
                                    message = self.url_encoder(message)
                                    self.browser.find_all('textarea')[0].insert(0, message)
                                    form = self.browser.get_forms()[1]
                                    form.action = 'https://m.facebook.com' + form.action
                                    self.browser.submit_form(form, submit=form.submit_fields['view_post'])
                                    self.time.sleep(sleep_thread)
                                    print('[+][Log][success] Wall Message Service :[' + friend_name + ']')
                                    pass
                                except KeyboardInterrupt as e:
                                    self.os._exit(1)
                                except Exception:
                                    print('[+][Log][failed] Message Service :[' + friend_name + ']')
                                    pass
                        else:
                            print('[-][Not Logged] Wall Message Service Stopped')
                            self.os._exit(1)
                        self.os._exit(1)
                        print('[+][Done] Post To All Friends Walls')
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass

                def autobot(self, message=None):
                    try:
                        if self.logged:
                            print('[+][Log][Start] Auto Bot (messages) Service')
                            message_list = {}
                            while True:
                                message = self.url_encoder(message)
                                self.browser.open('https://m.facebook.com/messages')
                                for element in self.browser.find_all('table'):
                                    if ' '.join(element['class']) == 'bl bm bn bo bp bq br':
                                        if not str(element.find_all('a')[0]).split('>')[1].split('<')[0].split('(')[0] in message_list:
                                            message_list[
                                                str(element.find_all('a')[0]).split('>')[1].split('<')[0].split('(')[0]] = 'https://m.facebook.com' + element.find_all(
                                                'a')[0]['href']
                                            pass
                                        else:
                                            message_list[str(element.find_all('a')[0]).split('>')[1].split('<')[0].split('(')[0] + str(
                                                self.random.randint(0,
                                                                    99999999))] = 'https://m.facebook.com' + element.find_all(
                                                'a')[0]['href']
                                    pass
                                for message_name, message_url in message_list.items():
                                    if message_list[message_name] != 'delete':
                                        try:
                                            self.browser.open(message_url)
                                            self.time.sleep(2)
                                            self.browser.find_all('textarea')[0].insert(0, message)
                                            form = self.browser.get_forms()[1]
                                            form.action = 'https://m.facebook.com' + form.action
                                            self.browser.submit_form(form, submit=form.submit_fields['send'])
                                            message_list[message_name] = 'delete'
                                            print('[+][success] Auto Bot (messages) Service :[' +
                                                  str(message_name).split('(')[
                                                      0] + ']')
                                            pass
                                        except KeyboardInterrupt as e:
                                            self.os._exit(1)
                                        except:
                                            try:
                                                self.Browser.get(message_url)
                                                self.time.sleep(2)
                                                self.Browser.find_element_by_name('body').send_keys(
                                                    'sorry this the bot')
                                                self.Browser.find_element_by_name('Send').click()
                                                message_list[message_name] = 'delete'
                                                print('[+][success] Auto Bot (messages) Service :[' +
                                                      str(message_name).split('(')[
                                                          0] + ']')
                                                pass
                                            except KeyboardInterrupt as e:
                                                self.os._exit(1)
                                            except:
                                                pass
                                            pass
                                        pass
                                    pass
                                for key in list(message_list):
                                    if message_list[key] == 'delete':
                                        message_list.pop(key, None)
                                        pass
                                    pass
                                pass
                            print('[+][Done] Auto Bot (messages) Service')
                            self.Browser.quit()
                            self.os._exit(1)
                            pass
                        else:
                            print('[-][Not Logged] Service Stopped')
                            self.os._exit(1)
                            pass
                        self.os._exit(1)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except Exception as e:
                        print(self.traceback.print_exc())
                        pass

                def unlike_all_friends(self, sleep_thread):
                    try:
                        if self.logged and self.friends.__len__() > 0:
                            print('[+][Start] unLike Post Service')
                            for friend_name, friend_url in self.friends.items():
                                post_links = []
                                self.browser.open('https://m.facebook.com' + friend_url)
                                for div in self.browser.find_all('div'):
                                    try:
                                        if str(div['id']).startswith('u_'):
                                            for a in div.find_all('a'):
                                                if str(a['href']).__contains__('/a/like.php') and \
                                                                str(a['href']).split('?')[1].split('&')[
                                                                    0] == 'ul=1':
                                                    post_links.append('https://m.facebook.com' + a['href'])
                                                    pass
                                                pass
                                            pass
                                        else:
                                            pass
                                        pass
                                    except KeyboardInterrupt as e:
                                        self.os._exit(1)
                                    except:
                                        pass
                                    pass
                                for post in post_links:
                                    self.browser.open(post)
                                    print('[+][Log][success] unLike Post Service : [' + friend_name + ']')
                                    self.time.sleep(sleep_thread)
                                pass
                            print('[+][Done] unLike Post (bot) Service')
                            pass
                        else:
                            print('[-][Not Logged] Service Stopped')
                            pass
                        self.os._exit(1)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass
                    pass

                def post_to_groups_wall(self, post=None, sleep_thread=2):
                    try:
                        if self.logged:
                            groups = self.group_list
                            for group_name, group_url in groups.items():
                                try:
                                    self.browser.open('https://m.facebook.com' + group_url)
                                    message = self.url_encoder(post)
                                    self.browser.find_all('textarea', {'name': 'xc_message'})[0].insert(0,
                                                                                                        message)
                                    form = self.browser.get_forms()[1]
                                    form.action = 'https://m.facebook.com' + form.action
                                    self.browser.submit_form(form, submit=form.submit_fields['view_post'])
                                    print('[+][Log][success] Post To Groups Wall Service :[' + group_name + ']')
                                    self.time.sleep(sleep_thread)
                                    pass
                                except KeyboardInterrupt as e:
                                    self.os._exit(1)
                                except Exception as e:

                                    print('[+][Log][failed] Post To Groups Wall Service :[' + group_name + ']')
                                    pass
                                pass
                            print('[+][Log][Done] Post To Groups Wall Service')
                            self.os._exit(1)
                            pass
                        else:
                            print('[-][Not Logged] Service Stopped')
                            pass
                        self.os._exit(1)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass

                def comment_to_pages(self, comment=None, sleep_thread=2):
                    try:
                        if self.logged:
                            pages = self.pages_list
                            print('[+][Log][Start] Comment To Pages Posts Service')
                            for page_name, page_url in pages.items():
                                try:
                                    xm = 0
                                    self.browser.open('https://m.facebook.com' + page_url)
                                    for comment_div in self.browser.find_all('div', {'id': 'recent'})[
                                        0].find_all(
                                        'div'):
                                        try:
                                            if str(comment_div['id']).startswith('u_'):
                                                if xm < 1:
                                                    for a in comment_div.find_all('a'):
                                                        if str(a['href']).lower().__contains__(
                                                                '/story.php?story_fbid='):
                                                            xm = 1
                                                            a = 'https://m.facebook.com' + a['href']
                                                            self.browser.open(a)
                                                            form = self.browser.get_form(
                                                                self.browser.find_all('form')[0])
                                                            comment = self.url_encoder(comment)
                                                            form['comment_text'].value = comment
                                                            self.browser.submit_form(form,
                                                                                     'https://m.facebok.com' +
                                                                                     self.browser.find_all(
                                                                                         'form')[
                                                                                         0][
                                                                                         'action'])
                                                            try:
                                                                m = self.browser.find_all('div', {
                                                                    'title': 'User Comments Blocked'})[0]
                                                                print(
                                                                    '[+][Log][Failed] Comment To Pages Posts Service [' + str(
                                                                        m['title']) + ']:[' + page_name + ']')
                                                                break
                                                            except KeyboardInterrupt as e:
                                                                self.os._exit(1)
                                                            except:
                                                                print(
                                                                    '[+][Log][Success] Comment To Pages Posts Service :[' + page_name + ']')
                                                                self.time.sleep(sleep_thread)
                                                                self.time.sleep(1)
                                                                break
                                                            pass
                                                        pass
                                                    pass
                                                else:
                                                    break
                                        except KeyboardInterrupt as e:
                                            self.os._exit(1)
                                        except:
                                            pass
                                    pass
                                except KeyboardInterrupt as e:
                                    self.os._exit(1)
                                except:
                                    print(
                                        '[+][Log][Failed] Comment To Pages Posts Service :[' + page_name + ']')
                                    pass
                                pass
                            print('[+][Log][Done] Comment To Pages Posts Service')
                            pass
                        else:
                            print('[-][Not Logged] Service Stopped')
                            pass
                        self.os._exit(1)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass

                def comment_to_pages_Bot(self, comment=None, sleep_thread=2):
                    try:
                        if self.logged:
                            pages = self.pages_list
                            commented = self.commented
                            print('[+][Log][Start] Comment To Pages Posts Service')
                            while True:
                                for page_name, page_url in pages.items():
                                    try:
                                        xm = 0
                                        self.browser.open('https://m.facebook.com' + page_url)
                                        for comment_div in self.browser.find_all('div', {'id': 'recent'})[
                                            0].find_all(
                                            'div'):
                                            try:
                                                if str(comment_div['id']).startswith('u_'):
                                                    if xm < 1:
                                                        for a in comment_div.find_all('a'):
                                                            if str(a['href']).lower().__contains__(
                                                                    '/story.php?story_fbid='):
                                                                xm = 1
                                                                a = 'https://m.facebook.com' + a['href']
                                                                if a not in commented:
                                                                    self.browser.open(a)
                                                                    form = self.browser.get_form(
                                                                        self.browser.find_all('form')[0])
                                                                    comment = self.url_encoder(comment)
                                                                    form['comment_text'].value = comment
                                                                    self.browser.submit_form(form,
                                                                                             'https://m.facebok.com' +
                                                                                             self.browser.find_all(
                                                                                                 'form')[
                                                                                                 0][
                                                                                                 'action'])
                                                                    try:
                                                                        m = self.browser.find_all('div', {
                                                                            'title': 'User Comments Blocked'})[
                                                                            0]
                                                                        print(
                                                                            '[+][Log][Failed] Comment To Pages Posts Service [' + str(
                                                                                m[
                                                                                    'title']) + ']:[' + page_name + ']')
                                                                        break
                                                                    except KeyboardInterrupt as e:
                                                                        self.os._exit(1)
                                                                    except:
                                                                        print(
                                                                            '[+][Log][Success] Comment To Pages Posts Service :[' + page_name + ']')
                                                                        a = str(a).split('&refid=')[0]
                                                                        commented.append(a)
                                                                        try:
                                                                            open('F_PG.DAT', 'a+').write(
                                                                                self.encrypter(a, 10) + "\n")
                                                                        except KeyboardInterrupt as e:
                                                                            self.os._exit(1)
                                                                        except:
                                                                            open('F_PG.DAT', 'a+')
                                                                            pass
                                                                        self.time.sleep(sleep_thread)
                                                                        self.time.sleep(1)
                                                                        break
                                                                else:
                                                                    break
                                                                    pass
                                                                pass
                                                            pass
                                                        pass
                                                    else:
                                                        break
                                            except KeyboardInterrupt as e:
                                                self.os._exit(1)
                                            except:
                                                pass
                                        pass
                                    except KeyboardInterrupt as e:
                                        self.os._exit(1)
                                    except:
                                        print(
                                            '[+][Log][Failed] Comment To Pages Posts Service :[' + page_name + ']')
                                        pass
                                    pass
                            print('[+][Log][Done] Comment To Pages Posts Service')
                            pass
                        else:
                            print('[-][Not Logged] Service Stopped')
                            pass
                        self.os._exit(1)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass

                def comment_to_friends(self, comment=None, sleep_thread=2):
                    try:
                        if self.logged:
                            pages = self.friends
                            print('[+][Log][Start] Comment To Friends Posts Service')
                            for page_name, page_url in pages.items():
                                try:
                                    xm = 0
                                    self.browser.open('https://m.facebook.com' + page_url)
                                    for comment_div in self.browser.find_all('div', {'id': 'recent'})[
                                        0].find_all(
                                        'div'):
                                        try:
                                            if str(comment_div['id']).startswith('u_'):
                                                if xm < 1:
                                                    for a in comment_div.find_all('a'):
                                                        if str(a['href']).lower().__contains__(
                                                                'story.php?story_fbid='):
                                                            xm = 1
                                                            a = 'https://m.facebook.com' + a['href']
                                                            self.browser.open(a)
                                                            form = self.browser.get_form(
                                                                self.browser.find_all('form')[0])
                                                            comment = self.url_encoder(comment)
                                                            form['comment_text'].value = comment
                                                            self.browser.submit_form(form,
                                                                                     'https://m.facebok.com' +
                                                                                     self.browser.find_all(
                                                                                         'form')[
                                                                                         0][
                                                                                         'action'])
                                                            try:
                                                                m = self.browser.find_all('div', {
                                                                    'title': 'User Comments Blocked'})[0]
                                                                print(
                                                                    '[+][Log][Failed] Comment To Friends Posts Service [' + str(
                                                                        m['title']) + ']:[' + page_name + ']')
                                                                break
                                                            except KeyboardInterrupt as e:
                                                                self.os._exit(1)
                                                            except:
                                                                print(
                                                                    '[+][Log][Success] Comment To Friends Posts Service :[' + page_name + ']')
                                                                self.time.sleep(sleep_thread)
                                                                self.time.sleep(1)
                                                                break
                                                            break
                                                            pass
                                                        else:
                                                            pass
                                                        pass
                                                    pass
                                                else:
                                                    break
                                        except KeyboardInterrupt as e:
                                            self.os._exit(1)
                                        except:
                                            pass
                                    pass
                                except KeyboardInterrupt as e:
                                    self.os._exit(1)
                                except:
                                    print(
                                        '[+][Log][Failed] Comment To Friends Posts Service :[' + page_name + ']')
                                    pass
                                pass
                            print('[+][Log][Done] Comment To Friends Posts Service')
                            pass
                        else:
                            print('[-][Not Logged] Service Stopped')
                            pass
                        self.os._exit(1)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass

                def comment_to_friends_Bot(self, comment=None, sleep_thread=2):
                    try:
                        if self.logged:
                            pages = self.friends
                            commented = self.commented
                            print('[+][Log][Start] Comment To Friends Posts Service')
                            while True:
                                for page_name, page_url in pages.items():
                                    try:
                                        xm = 0
                                        self.browser.open('https://m.facebook.com' + page_url)
                                        for comment_div in self.browser.find_all('div', {'id': 'recent'})[
                                            0].find_all(
                                            'div'):
                                            try:
                                                if str(comment_div['id']).startswith('u_'):
                                                    if xm < 1:
                                                        for a in comment_div.find_all('a'):
                                                            if str(a['href']).lower().__contains__(
                                                                    'story.php?story_fbid='):
                                                                xm = 1
                                                                a = 'https://m.facebook.com' + a['href']
                                                                if a not in commented:
                                                                    self.browser.open(a)
                                                                    form = self.browser.get_form(
                                                                        self.browser.find_all('form')[0])
                                                                    comment = self.url_encoder(comment)
                                                                    form['comment_text'].value = comment
                                                                    self.browser.submit_form(form,
                                                                                             'https://m.facebok.com' +
                                                                                             self.browser.find_all(
                                                                                                 'form')[
                                                                                                 0][
                                                                                                 'action'])
                                                                    try:
                                                                        m = self.browser.find_all('div', {
                                                                            'title': 'User Comments Blocked'})[
                                                                            0]
                                                                        print(
                                                                            '[+][Log][Failed] Comment To Friends Posts Service [' + str(
                                                                                m[
                                                                                    'title']) + ']:[' + page_name + ']')
                                                                        break
                                                                    except KeyboardInterrupt as e:
                                                                        self.os._exit(1)
                                                                    except:
                                                                        print(
                                                                            '[+][Log][Success] Comment To Friends Posts Service :[' + page_name + ']')
                                                                        a = str(a).split('&refid=')[0]
                                                                        commented.append(a)
                                                                        try:
                                                                            open('F_FBF.DAT', 'a+').write(
                                                                                self.encrypter(a, 12) + "\n")
                                                                        except KeyboardInterrupt as e:
                                                                            self.os._exit(1)
                                                                        except:
                                                                            open('F_FBF.DAT', 'a+')
                                                                            pass
                                                                        self.time.sleep(sleep_thread)
                                                                        self.time.sleep(1)
                                                                        break
                                                                    break
                                                                    pass
                                                                else:
                                                                    break
                                                                    pass
                                                                pass
                                                            else:
                                                                pass
                                                            pass
                                                        pass
                                                    else:
                                                        break
                                            except KeyboardInterrupt as e:
                                                self.os._exit(1)
                                            except:
                                                pass
                                        pass
                                    except KeyboardInterrupt as e:
                                        self.os._exit(1)
                                    except:
                                        print(
                                            '[+][Log][Failed] Comment To Friends Posts Service :[' + page_name + ']')
                                        pass
                                    pass
                            print('[+][Log][Done] Comment To Friends Posts Service')
                            pass
                        else:
                            print('[-][Not Logged] Service Stopped')
                            pass
                        self.os._exit(1)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass

                def comment_to_groups(self, comment=None, sleep_thread=2):
                    try:
                        if self.logged:
                            pages = self.group_list
                            print('[+][Log][Start] Comment To Groups Posts Service')
                            for page_name, page_url in pages.items():
                                try:
                                    xm = 0
                                    self.browser.open('https://m.facebook.com' + page_url)
                                    for comment_div in \
                                            self.browser.find_all('div', {'id': 'm_group_stories_container'})[
                                                0].find_all(
                                                'div'):
                                        try:
                                            if str(comment_div['id']).startswith('u_'):
                                                if xm < 1:
                                                    for a in comment_div.find_all('a'):
                                                        if str(a['href']).lower().__contains__(
                                                                '?view=permalink&id='):
                                                            xm = 1
                                                            a = 'https://m.facebook.com' + a['href']
                                                            self.browser.open(a)
                                                            form = self.browser.get_forms()[1]
                                                            comment = self.url_encoder(comment)
                                                            form['comment_text'].value = comment
                                                            self.browser.submit_form(form,
                                                                                     'https://m.facebok.com' +
                                                                                     self.browser.find_all(
                                                                                         'form')[
                                                                                         0][
                                                                                         'action'])
                                                            try:
                                                                m = self.browser.find_all('div', {
                                                                    'title': 'User Comments Blocked'})[0]
                                                                print(
                                                                    '[+][Log][Failed] Comment To Groups Posts Service [' + str(
                                                                        m['title']) + ']:[' + page_name + ']')
                                                                break
                                                            except KeyboardInterrupt as e:
                                                                self.os._exit(1)
                                                            except:
                                                                print(
                                                                    '[+][Log][Success] Comment To Groups Posts Service :[' + page_name + ']')
                                                                self.time.sleep(sleep_thread)
                                                                self.time.sleep(1)
                                                                break
                                                            break
                                                            pass
                                                        else:
                                                            pass
                                                        pass
                                                    pass
                                                else:
                                                    break
                                        except KeyboardInterrupt as e:
                                            self.os._exit(1)
                                        except:
                                            pass
                                    pass
                                except KeyboardInterrupt as e:
                                    self.os._exit(1)
                                except:
                                    print(
                                        '[+][Log][Failed] Comment To Groups Posts Service :[' + page_name + ']')
                                    pass
                                pass
                            print('[+][Log][Done] Comment To Groups Posts Service')
                            pass
                        else:
                            print('[-][Not Logged] Service Stopped')
                            pass
                        self.os._exit(1)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except Exception as e:
                        pass

                def comment_to_groups_Bot(self, comment=None, sleep_thread=2):
                    try:
                        if self.logged:
                            pages = self.group_list
                            commented = self.commented
                            print('[+][Log][Start] Comment To Groups Posts Service')
                            while True:
                                for page_name, page_url in pages.items():
                                    try:
                                        xm = 0
                                        self.browser.open('https://m.facebook.com' + page_url)
                                        for comment_div in \
                                                self.browser.find_all('div',
                                                                      {'id': 'm_group_stories_container'})[
                                                    0].find_all(
                                                    'div'):
                                            try:
                                                if str(comment_div['id']).startswith('u_'):
                                                    if xm < 1:
                                                        for a in comment_div.find_all('a'):
                                                            if str(a['href']).lower().__contains__(
                                                                    '?view=permalink&id='):
                                                                xm = 1
                                                                a = 'https://m.facebook.com' + a['href']
                                                                if a not in commented:
                                                                    self.browser.open(a)
                                                                    form = self.browser.get_forms()[1]
                                                                    comment = self.url_encoder(comment)
                                                                    form['comment_text'].value = comment
                                                                    self.browser.submit_form(form,
                                                                                             'https://m.facebok.com' +
                                                                                             self.browser.find_all(
                                                                                                 'form')[
                                                                                                 0][
                                                                                                 'action'])
                                                                    try:
                                                                        m = self.browser.find_all('div', {
                                                                            'title': 'User Comments Blocked'})[
                                                                            0]
                                                                        print(
                                                                            '[+][Log][Failed] Comment To Pages Groups Service [' + str(
                                                                                m[
                                                                                    'title']) + ']:[' + page_name + ']')
                                                                        break
                                                                    except KeyboardInterrupt as e:
                                                                        self.os._exit(1)
                                                                    except:
                                                                        print(
                                                                            '[+][Log][Success] Comment To Groups Posts Service :[' + page_name + ']')
                                                                        a = str(a).split('&refid=')[0]
                                                                        commented.append(a)
                                                                        try:
                                                                            open('F_GP.DAT', 'a+').write(
                                                                                self.encrypter(a, 11) + "\n")
                                                                        except KeyboardInterrupt as e:
                                                                            self.os._exit(1)
                                                                        except:
                                                                            open('F_GP.DAT', 'a+')
                                                                            pass
                                                                        self.time.sleep(sleep_thread)
                                                                        self.time.sleep(1)
                                                                        break
                                                                    break
                                                                    pass
                                                                else:
                                                                    break
                                                                    pass
                                                            else:
                                                                pass
                                                            pass
                                                        pass
                                                    else:
                                                        break
                                            except KeyboardInterrupt as e:
                                                self.os._exit(1)
                                            except:
                                                pass
                                        pass
                                    except KeyboardInterrupt as e:
                                        self.os._exit(1)
                                    except:
                                        print(
                                            '[+][Log][Failed] Comment To Friends Posts Service :[' + page_name + ']')
                                        pass
                                    pass
                            print('[+][Log][Done] Comment To Friends Posts Service')
                            pass
                        else:
                            print('[-][Not Logged] Service Stopped')
                            pass
                        self.os._exit(1)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except Exception as e:
                        pass

                def delete_wall_posts_friends(self, sleep_thread=2):
                    try:
                        if self.logged:
                            user_agent = (
                                "Mozilla/5.0 (Macintosh; PPC Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0"
                            )
                            dcap = dict(self.DesiredCapabilities.PHANTOMJS)
                            dcap["phantomjs.page.settings.userAgent"] = user_agent
                            self.Browser = self.webdriver.PhantomJS(desired_capabilities=dcap,
                                                               executable_path='/usr/share/phantomjsbr/phanjs/bin/phantomjs')
                            self.Browser.get('https://www.facebook.com/login.php')
                            try:
                                self.Browser.find_element_by_name('email').send_keys(self.username)
                                self.Browser.find_element_by_name('pass').send_keys(self.password)
                                self.Browser.find_element_by_id('loginbutton').click()
                                pass
                            except KeyboardInterrupt as e:
                                self.os._exit(1)
                            except:
                                pass
                            print('[+][Log][start] Delete Wall Message Service')
                            friends = self.friends
                            account_url = self.account_url.split('/')[3]
                            for friend_name, friend_url in friends.items():
                                self.browser.open('https://m.facebook.com' + friend_url)
                                for div in self.browser.find_all('div'):
                                    try:
                                        if str(div['id']).startswith('u_'):
                                            if str(div.find_all('a')[0]['href']).split('?')[0].split('/')[
                                                1] == account_url:
                                                for a in div.find_all('a'):
                                                    if (
                                                            str(a['href']).__contains__('/nfx/basic/direct_actions/')):
                                                        try:
                                                            self.Browser.get(
                                                                'http://m.facebook.com' + str(a['href']))
                                                            print(self.Browser.page_source)
                                                            self.Browser.find_elements_by_name('action_key')[
                                                                1].click()
                                                            for e in self.Browser.find_elements_by_tag_name(
                                                                    'input'):
                                                                if e.get_attribute('value') == 'Continue':
                                                                    e.click()
                                                                    break
                                                            print(
                                                                '[+][Log][success] Delete Wall Message Service: ' + friend_name)
                                                        except Exception as e:
                                                            print(
                                                                '[+][Log][success] Delete Wall Message Service: ' + friend_name)
                                                            pass
                                            pass
                                        else:
                                            pass
                                        pass
                                    except KeyboardInterrupt as e:
                                        self.os._exit(1)
                                    except Exception as e:
                                        pass
                                    pass
                                pass
                            self.Browser.close()
                            self.Browser.quit()
                            print('[+][Log][Done] Delete Wall Message Service')
                            pass
                        else:
                            print('[-][Not Logged] Wall Message Service Stopped')
                            pass
                        self.Browser.close()
                        self.Browser.quit()
                        self.os._exit(1)
                        print('[+][Done] Post To All Friends Walls')
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass
                    pass

                def auto_liker(self, sleep_thread=2):
                    try:
                        if self.logged and self.friends.__len__() > 0:
                            print('[+][Start] Like Post Service')
                            for friend_name, friend_url in self.friends.items():
                                post_links = []
                                self.browser.open('https://m.facebook.com' + friend_url)
                                for div in self.browser.find_all('div'):
                                    try:
                                        if str(div['id']).startswith('u_'):
                                            for a in div.find_all('a'):
                                                if str(a['href']).__contains__('/a/like.php') and \
                                                                str(a['href']).split('?')[1].split('&')[
                                                                    0] == 'ul':
                                                    post_links.append('https://m.facebook.com' + a['href'])
                                                    pass
                                                pass
                                            pass
                                        else:
                                            pass
                                        pass
                                    except KeyboardInterrupt as e:
                                        self.os._exit(1)
                                    except:
                                        pass
                                    pass
                                for post in post_links:
                                    self.browser.open(post)
                                    print('[+][Log][success] Like Post Service : [' + friend_name + ']')
                                    self.time.sleep(sleep_thread)
                                pass
                            print('[+][Done] Like Post (bot) Service')
                            pass
                        else:
                            print('[-][Not Logged] Service Stopped')
                            pass
                        self.os._exit(1)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass
                    pass

                def auto_liker_bot(self, sleep_thread=2):
                    try:
                        if self.logged and self.friends.__len__() > 0:
                            print('[+][Start] Like Post (bot) Service')
                            liked = []
                            while True:
                                for link_name, link_url in self.friends.items():
                                    try:
                                        self.browser.open('https://m.facebook.com' + link_url)
                                        for div in self.browser.find_all('div'):
                                            try:
                                                if str(div['id']).startswith('u_'):
                                                    for a in div.find_all('a'):
                                                        if str(a['href']).__contains__('/a/like.php') and \
                                                                        str(a['href']).split('?')[1].split('&')[
                                                                            0] == 'ul':
                                                            if not 'https://m.facebook.com' + a[
                                                                'href'] in liked:
                                                                self.browser.open(
                                                                    'https://m.facebook.com' + a['href'])
                                                                print(
                                                                    '[+][Log][success] Like Post Service : [' + link_name + ']')
                                                                liked.append(
                                                                    'https://m.facebook.com' + a['href'])
                                                                self.time.sleep(sleep_thread)
                                                            pass
                                                        pass
                                                    pass
                                                else:
                                                    pass
                                                pass
                                            except KeyboardInterrupt as e:
                                                self.os._exit(1)
                                            except Exception as e:
                                                pass
                                    except KeyboardInterrupt as e:
                                        self.os._exit(1)
                                    except Exception as m:
                                        pass
                                    pass
                            print('[+][Done] Like Post (bot) Service')
                            pass
                        else:
                            print('[-][Not Logged] Service Stopped')
                            pass
                        self.os._exit(1)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass
                    pass

                def Message_To_All_Friends(self, message=None, sleep_thread=2):
                    try:
                        self.login()
                        print('[+][start] Friend List Generator Service')
                        self.friends = self.friend_list_gen()
                        print('[+][Done] Friend List Generator Service')
                        self.message_all_friends(message, sleep_thread)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass

                def Post_To_Groups_Wall(self, Post=None, sleep_thread=2):
                    try:
                        self.login()
                        print('[+][start] Groups List Generator Service')
                        self.group_list = self.group_list_gen()
                        print('[+][Done] Groups List Generator Service')
                        self.post_to_groups_wall(Post, sleep_thread)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass

                def Wall_Message_To_All_Friends(self, message=None, sleep_thread=2):
                    try:
                        self.login()
                        print('[+][start] Friend List Generator Service')
                        self.friends = self.friend_list_gen()
                        print('[+][Done] Friend List Generator Service')
                        self.wall_message_for_all_friends(message, sleep_thread)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass
                    pass

                def Comment_To_Pages_Posts(self, comment=None, sleep_thread=2):
                    try:
                        self.login()
                        print('[+][start] Pages List Generator Service')
                        self.pages_list = self.pages_list_gen()
                        print('[+][Done] Pages List Generator Service')
                        self.comment_to_pages(comment, sleep_thread)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass
                    pass

                def Auto_Bot(self, message=None):
                    self.login()
                    self.autobot(message)

                def Coment_To_Pages_Posts_BOT(self, comment=None, sleep_thread=2):
                    try:
                        self.login()
                        print('[+][start] Pages List Generator Service')
                        self.pages_list = self.pages_list_gen()
                        print('[+][Done] Pages List Generator Service')
                        self.comment_to_pages_Bot(comment, sleep_thread)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass
                    pass

                def Auto_Liker(self, sleep_thread=2):
                    try:
                        self.login()
                        print('[+][start] Friend List Generator Service')
                        self.friends = self.friend_list_gen()
                        print('[+][Done] Friend List Generator Service')
                        self.auto_liker(sleep_thread)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass
                    pass

                def Unlike_all_friends(self, sleep_thread=2):
                    try:
                        self.login()
                        print('[+][start] Friend List Generator Service')
                        self.friends = self.friend_list_gen()
                        print('[+][Done] Friend List Generator Service')
                        self.unlike_all_friends(sleep_thread)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass
                    pass

                def Auto_Liker_BOT(self, sleep_thread=2):
                    try:
                        self.login()
                        print('[+][start] Friend List Generator Service')
                        self.friends = self.friend_list_gen()
                        print('[+][Done] Friend List Generator Service')
                        self.auto_liker_bot(sleep_thread)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass
                    pass

                def Watcher(self, number_of_activities=10):
                    try:
                        self.login()
                        self.watcher(number_of_activities)
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass

                def Commet_Friends_Posts(self, Comment=None, sleep_thread=2):
                    try:
                        self.login()
                        print('[+][start] Friend List Generator Service')
                        self.friends = self.friend_list_gen()
                        print('[+][Done] Friend List Generator Service')
                        self.comment_to_friends(Comment, sleep_thread)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass
                    pass

                def Comment_Groups_Posts(self, Comment=None, sleep_thread=2):
                    try:
                        self.login()
                        print('[+][start] Groups List Generator Service')
                        self.group_list = self.group_list_gen()
                        print('[+][Done] Groups List Generator Service')
                        self.comment_to_groups(Comment, sleep_thread)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass
                    pass

                def Commet_Friends_Posts_Bot(self, Comment=None, sleep_thread=2):
                    try:
                        self.login()
                        print('[+][start] Friend List Generator Service')
                        self.friends = self.friend_list_gen()
                        print('[+][Done] Friend List Generator Service')
                        self.comment_to_friends_Bot(Comment, sleep_thread)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass
                    pass

                def Comment_Groups_Posts_Bot(self, Comment=None, sleep_thread=2):
                    try:
                        self.login()
                        print('[+][start] Groups List Generator Service')
                        self.group_list = self.group_list_gen()
                        print('[+][Done] Groups List Generator Service')
                        self.comment_to_groups_Bot(Comment, sleep_thread)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except Exception as e:
                        pass
                    pass

                def Comment_To_All(self, Comment=None, sleep_thread=2):
                    self.login()
                    try:
                        print('[+][start] Friend List Generator Service')
                        self.friends = self.friend_list_gen()
                        print('[+][Done] Friend List Generator Service')
                        print('[+][start] Groups List Generator Service')
                        self.group_list = self.group_list_gen()
                        print('[+][Done] Groups List Generator Service')
                        print('[+][start] Pages List Generator Service')
                        self.pages_list = self.pages_list_gen()
                        print('[+][Done] Pages List Generator Service')
                        self.comment_to_friends(Comment, sleep_thread)
                        self.comment_to_groups(Comment, sleep_thread)
                        self.comment_to_pages(Comment, sleep_thread)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass
                    pass

                def Comment_To_All_Bot(self, Comment=None, sleep_thread=2):
                    self.login()
                    try:
                        print('[+][start] Friend List Generator Service')
                        self.friends = self.friend_list_gen()
                        print('[+][Done] Friend List Generator Service')
                        print('[+][start] Groups List Generator Service')
                        self.group_list = self.group_list_gen()
                        print('[+][Done] Groups List Generator Service')
                        print('[+][start] Pages List Generator Service')
                        self.pages_list = self.pages_list_gen()
                        print('[+][Done] Pages List Generator Service')
                        self.comment_to_friends_Bot(Comment, sleep_thread)
                        self.comment_to_groups_Bot(Comment, sleep_thread)
                        self.comment_to_pages_Bot(Comment, sleep_thread)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass
                    pass

                def Unfriend_all(self, sleep_thread=2):
                    self.login()
                    try:
                        print('[+][start] Friend List Generator Service')
                        self.friends = self.friend_list_gen()
                        print('[+][Done] Friend List Generator Service')
                        self.unfriend_all(sleep_thread)
                        pass
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        pass
                    pass

                def Service_Start(self):
                    try:
                        print(self.Coder)
                        username = input('[+]Facebook Account Name: ')
                        password = self.getpass.getpass('[+]Facebook Account Password: ')
                        if str(username).strip().replace(' ', '').__len__() > 0 and str(
                                password).strip().replace(
                            ' ', '').__len__() > 0:
                            self.Login(username, password)
                            self.Comments_Fetcher()
                            try:
                                choose = int(input('[+]Please Choose One Of this Services To Start:'
                                                   '\n[+][1] Message To All Friends'
                                                   '\n[+][2] Auto Message BOT'
                                                   '\n[+][3] Post To All Friends Walls'
                                                   '\n[+][4] Post To All Groups Walls'
                                                   '\n[+][5] Comment On Latest Pages Posts'
                                                   '\n[+][6] Comment On Latest Pages Posts (BOT)'
                                                   '\n[+][7] Comment On Latest Friends Posts'
                                                   '\n[+][8] Comment On Latest Friends Posts (BOT)'
                                                   '\n[+][9] Comment On Latest Groups Posts'
                                                   '\n[+][10] Comment On Latest Groups Posts(BOT)'
                                                   '\n[+][11] Comment On All Latest Posts'
                                                   '\n[+][12] Comment On All Latest Posts (BOT)'
                                                   '\n[+][13] Auto Liker For All Friends'
                                                   '\n[+][14] Auto Liker For All Friends (BOT)'
                                                   '\n[+][15] Unfriend all'
                                                   '\n[+][16] Unlike all Friends'
                                                   '\n[+][Choose] Enter Your Choise: '))
                                if choose > 0 and choose < 17:
                                    thread = 2
                                    if choose == 1:
                                        message = input('[+]You have chose Message To All'
                                                        '\n[+]Enter Your Message Text To Start: ')
                                        try:
                                            thread = int(input(
                                                '[+]Enter Thread Sleep in seconds (optional set to zero for None) : '))
                                        except KeyboardInterrupt as e:
                                            self.os._exit(1)
                                        except:
                                            pass
                                        if str(message).strip().replace(' ', '').__len__() > 0:
                                            self.Message_To_All_Friends(message, thread)
                                        else:
                                            print(
                                                '[-][error] Message Is Empty. System Will Exit')
                                            self.os._exit(1)
                                    elif choose == 2:
                                        message = input('[+]You have chose Auto Bot Message'
                                                        '\n[+]Enter Your Message Text To Start: ')
                                        if str(message).strip().replace(' ', '').__len__() > 0:
                                            message = message
                                        else:
                                            print(
                                                '[-][error] Message Is Empty. System Will Exit')
                                            self.os._exit(1)
                                        self.Auto_Bot(message)
                                    elif choose == 3:
                                        message = input('[+]You have chose Post To All Friends Walls'
                                                        '\n[+]Enter Your Post Text To Start: ')
                                        try:
                                            thread = int(
                                                input(
                                                    '[+]Enter Thread Sleep in seconds (optional set to zero for None) : '))
                                        except KeyboardInterrupt as e:
                                            self.os._exit(1)
                                        except:
                                            pass
                                        if str(message).strip().replace(' ', '').__len__() > 0:
                                            self.Wall_Message_To_All_Friends(message, thread)
                                        else:
                                            print(
                                                '[-][error] Message Is Empty. System Will Exit')
                                            self.os._exit(1)
                                    elif choose == 4:
                                        message = input('[+]You have chose Post To All Groups Walls'
                                                        '\n[+]Enter Your Post Text To Start: ')
                                        try:
                                            thread = int(
                                                input(
                                                    '[+]Enter Thread Sleep in seconds (optional set to zero for None) : '))
                                        except KeyboardInterrupt as e:
                                            self.os._exit(1)
                                        except:
                                            pass
                                        if str(message).strip().replace(' ', '').__len__() > 0:
                                            self.Post_To_Groups_Wall(message, thread)
                                        else:
                                            print(
                                                '[-][error] Message Is Empty. System Will Exit')
                                            self.os._exit(1)
                                    elif choose == 5:
                                        message = input('[+]You have Comment On Latest Pages Posts'
                                                        '\n[+]Enter Your Post Text To Start: ')
                                        try:
                                            thread = int(
                                                input(
                                                    '[+]Enter Thread Sleep in seconds (optional set to zero for None) : '))
                                        except KeyboardInterrupt as e:
                                            self.os._exit(1)
                                        except:
                                            pass
                                        if str(message).strip().replace(' ', '').__len__() > 0:
                                            self.Comment_To_Pages_Posts(message, thread)
                                        else:
                                            print(
                                                '[-][error] Message Is Empty. System Will Exit')
                                            self.os._exit(1)
                                    elif choose == 6:
                                        message = input('[+]You have chose Comment On Latest Pages Posts (BOT)'
                                                        '\n[+]Enter Your Post Text To Start: ')
                                        try:
                                            thread = int(
                                                input(
                                                    '[+]Enter Thread Sleep in seconds (optional set to zero for None) : '))
                                        except KeyboardInterrupt as e:
                                            self.os._exit(1)
                                        except:
                                            pass
                                        if str(message).strip().replace(' ', '').__len__() > 0:
                                            self.Coment_To_Pages_Posts_BOT(message, thread)
                                        else:
                                            print(
                                                '[-][error] Message Is Empty. System Will Exit')
                                            self.os._exit(1)
                                    elif choose == 7:
                                        message = input('[+]You have chose Comment On Latest Friends Posts'
                                                        '\n[+]Enter Your Post Text To Start: ')
                                        try:
                                            thread = int(
                                                input(
                                                    '[+]Enter Thread Sleep in seconds (optional set to zero for None) : '))
                                        except KeyboardInterrupt as e:
                                            self.os._exit(1)
                                        except:
                                            pass
                                        if str(message).strip().replace(' ', '').__len__() > 0:
                                            self.Commet_Friends_Posts(message, thread)
                                        else:
                                            print(
                                                '[-][error] Message Is Empty. System Will Exit')
                                            self.os._exit(1)
                                    elif choose == 8:
                                        message = input(
                                            '[+]You have chose Comment On Latest Friends Posts (BOT)'
                                            '\n[+]Enter Your Post Text To Start: ')
                                        try:
                                            thread = int(
                                                input(
                                                    '[+]Enter Thread Sleep in seconds (optional set to zero for None) : '))
                                        except KeyboardInterrupt as e:
                                            self.os._exit(1)
                                        except:
                                            pass
                                        if str(message).strip().replace(' ', '').__len__() > 0:
                                            self.Commet_Friends_Posts_Bot(message, thread)
                                        else:
                                            print(
                                                '[-][error] Message Is Empty. System Will Exit')
                                            self.os._exit(1)
                                    elif choose == 9:
                                        message = input('[+]You have chose Comment On Latest Groups Posts'
                                                        '\n[+]Enter Your Post Text To Start: ')
                                        try:
                                            thread = int(
                                                input(
                                                    '[+]Enter Thread Sleep in seconds (optional set to zero for None) : '))
                                        except KeyboardInterrupt as e:
                                            self.os._exit(1)
                                        except:
                                            pass
                                        if str(message).strip().replace(' ', '').__len__() > 0:
                                            self.Comment_Groups_Posts(message, thread)
                                        else:
                                            print(
                                                '[-][error] Message Is Empty. System Will Exit')
                                            self.os._exit(1)
                                    elif choose == 10:
                                        message = input('[+]You have chose Comment On Latest Groups Posts (BOT)'
                                                        '\n[+]Enter Your Post Text To Start: ')
                                        try:
                                            thread = int(
                                                input(
                                                    '[+]Enter Thread Sleep in seconds (optional set to zero for None) : '))
                                        except KeyboardInterrupt as e:
                                            self.os._exit(1)
                                        except:
                                            pass
                                        if str(message).strip().replace(' ', '').__len__() > 0:
                                            self.Comment_Groups_Posts_Bot(message, thread)
                                        else:
                                            print(
                                                '[-][error] Message Is Empty. System Will Exit')
                                            self.os._exit(1)
                                    elif choose == 11:
                                        message = input('[+]You have chose Comment On All Latest Posts'
                                                        '\n[+]Enter Your Post Text To Start: ')
                                        try:
                                            thread = int(
                                                input(
                                                    '[+]Enter Thread Sleep in seconds (optional set to zero for None) : '))
                                        except KeyboardInterrupt as e:
                                            self.os._exit(1)
                                        except:
                                            pass
                                        if str(message).strip().replace(' ', '').__len__() > 0:
                                            self.Comment_To_All(message, thread)
                                        else:
                                            print(
                                                '[-][error] Message Is Empty. System Will Exit')
                                            self.os._exit(1)
                                    elif choose == 12:
                                        message = input('[+]You have chose Comment On All Latest Posts (BOT)'
                                                        '\n[+]Enter Your Post Text To Start: ')
                                        try:
                                            thread = int(
                                                input(
                                                    '[+]Enter Thread Sleep in seconds (optional set to zero for None) : '))
                                        except KeyboardInterrupt as e:
                                            self.os._exit(1)
                                        except:
                                            pass
                                        if str(message).strip().replace(' ', '').__len__() > 0:
                                            self.Comment_To_All_Bot(message, thread)
                                        else:
                                            print(
                                                '[-][error] Message Is Empty. System Will Exit')
                                            self.os._exit(1)
                                    elif choose == 13:
                                        thread = 2
                                        try:
                                            thread = int(input('[+]You have chose Auto Liker For All Friends'
                                                               '\n[+]Enter Thread Sleep in seconds (optional set to zero for None) : '))
                                        except KeyboardInterrupt as e:
                                            self.os._exit(1)
                                        except:
                                            pass
                                        self.Auto_Liker(thread)
                                    elif choose == 14:
                                        thread = 2
                                        try:
                                            thread = int(
                                                input('[+]You have chose Auto Liker For All Friends (BOT)'
                                                      '\n[+]Enter Thread Sleep in seconds (optional set to zero for None) : '))
                                        except KeyboardInterrupt as e:
                                            self.os._exit(1)
                                        except:
                                            pass
                                        self.Auto_Liker_BOT(thread)
                                    elif choose == 15:
                                        print('[+]You have chose Unfriend All')
                                        try:
                                            thread = int(input(
                                                '[+]Enter Thread Sleep in seconds (optional set to zero for None) : '))
                                            self.Unfriend_all(thread)
                                        except KeyboardInterrupt as e:
                                            self.os._exit(1)
                                        except:
                                            pass
                                            pass
                                        pass
                                    elif choose == 16:
                                        print('[+]You have chose Unlike All Friends')
                                        try:
                                            thread = int(input(
                                                '[+]Enter Thread Sleep in seconds (optional set to zero for None) : '))
                                            self.Unlike_all_friends(thread)
                                        except KeyboardInterrupt as e:
                                            self.os._exit(1)
                                        except:
                                            pass
                                            pass
                                        pass
                                    else:
                                        print(
                                            '[-][error] Message Is Empty. System Will Exit')
                                        self.os._exit(1)
                                        pass
                                    pass
                                else:
                                    print(
                                        '[-][error] You Must Choose Number between 1 and 16 to Start. System Will Exit')
                                    self.os._exit(1)
                                pass
                            except KeyboardInterrupt as e:
                                self.os._exit(1)
                            except Exception as e:
                                print(e)
                                print('[-][error] You Must Choose Number To Start. System Will Exit')
                                pass
                        else:
                            print('[-][Not Logged] Service Stopped System Will Close')
                            return False
                            self.os._exit(1)
                    except KeyboardInterrupt as e:
                        self.os._exit(1)
                    except:
                        print(self.traceback.print_exc())
                        pass
                    pass

                pass
            except Exception as e:
                pass

Facebook().Auto_Bot()
