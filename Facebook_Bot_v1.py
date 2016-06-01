# coding=utf-8


class Facebook:
        try:
            class Auto_Bot:
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
                    def __init__(self):
                        self.Admin_Rights()
                        self.Import_Checker()

                    def Admin_Rights(self):
                        try:
                            import os, sys
                            open('/etc/Mod', 'w+')
                            os.unlink('/etc/Mod')
                        except Exception as e:
                            e = e.args
                            if e[0] == 13:
                                print('[+] Sorry You Need To User Script As Admin Script Will Exit')
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
                        try:
                            __import__('imp').find_module('selenium')
                        except ImportError:
                            import pip
                            pip.main(['install', 'selenium'])
                            pass
                        try:
                            __import__('imp').find_module('pyvirtualdisplay')
                        except ImportError:
                            import pip
                            pip.main(['install', 'pyvirtualdisplay'])
                            pass
                        pass

                class Display:
                    import pyvirtualdisplay, sys, os, ctypes
                    display = ''

                    def stop(self):
                        if self.sys.platform.lower() == 'linux':
                            self.display.stop()
                            pass
                        pass

                    def start(self):
                        if self.sys.platform.lower() == 'linux':
                            self.display = self.pyvirtualdisplay.Display(visible=False, size=(5000, 5400))
                            self.display.start()
                            pass
                        pass
                Installer()
                import time, random, re, string, sys, warnings, os, pip, traceback, math, getpass, pyvirtualdisplay, \
                    pickle, \
                    signal
                from robobrowser import RoboBrowser
                import robobrowser
                from selenium import webdriver
                from selenium.webdriver.common.keys import Keys
                browser = RoboBrowser(
                    user_agent='Mozilla/5.0 (Macintosh; PPC Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0',
                    multiplier=True,
                    allow_redirects=True, history=True, parser='lxml')
                Browser = ''
                keywords = {'who are you ': 'TPCT Bot'}

                def __init__(self):
                    try:
                        self.username = ''
                        self.password = ''
                        self.logged = False
                        self.friends = ''
                        self.Browse_Profile = ''
                        self.group_list = ''
                        self.pages_list = ''
                        self.account_name = ''
                        self.account_url = ''
                        self.Display().start()
                        self.Service_Start()
                    except:
                        pass

                def login(self):
                    try:
                        if self.logged and str(self.username).strip().__len__() > 0 and str(self.password).strip().__len__() > 0:
                            self.browser.open(
                                'https://m.facebook.com/a/language.php?l=en_GB&lref=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Ffl%26refid%3D9%26refsrc%3Dhttps%253A%252F%252Fm.facebook.com%252Flogin%252F%26ref_component%3Dmbasic_footer&index=1&gfid=AQB4NBKfmvzv7Hw1&ref_component=mbasic_footer&ref_page=XLoginController')
                            form = self.browser.get_form('login_form')
                            form['email'] = self.username
                            form['pass'] = self.password
                            self.browser.submit_form(form)
                            if self.browser.find_all('div', {'class': 'z'}):
                                print(
                                    '[-][error] Something went wrong : ' + self.browser.find_all('div', {'class': 'z'})[
                                        0].text)
                                self.sys.exit(1)
                                pass
                            elif str(self.browser.url).__contains__('checkpoint'):
                                print(
                                    '[-][error] Something went wrong : Check your account now it might be blocked')
                                self.sys.exit(1)
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
                                    self.sys.exit(1)
                        else:
                            print('[-][Not Logged] Service Stopped System Will Close')
                        pass
                    except Exception as e:
                        print('[-][Not Logged] Service Stopped ' + self.traceback.print_exc() + ' System Will Close')
                        return False
                        self.sys.exit(1)
                        pass

                def Login(self, username=None, password=None):
                    try:
                        browser = self.RoboBrowser(
                            user_agent='Mozilla/5.0 (Macintosh; PPC Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0',
                            multiplier=True,
                            allow_redirects=True, history=True, parser='lxml')
                        if str(username).strip().__len__() > 0 and str(password).strip().__len__() > 0:
                            browser.open(
                                'https://m.facebook.com/a/language.php?l=en_GB&lref=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Ffl%26refid%3D9%26refsrc%3Dhttps%253A%252F%252Fm.facebook.com%252Flogin%252F%26ref_component%3Dmbasic_footer&index=1&gfid=AQB4NBKfmvzv7Hw1&ref_component=mbasic_footer&ref_page=XLoginController')
                            form = browser.get_form('login_form')
                            form['email'] = username
                            form['pass'] = password
                            browser.submit_form(form)
                            if browser.find_all('div', {'class': 'z'}):
                                print(
                                    '[-][error] Something went wrong : ' + browser.find_all('div', {'class': 'z'})[
                                        0].text)
                                self.sys.exit(1)
                                pass
                            elif str(browser.url).__contains__('checkpoint'):
                                print(
                                    '[-][error] Something went wrong : Check your account now it might be blocked')
                                self.sys.exit(1)
                                pass
                            else:
                                browser.open('https://m.facebook.com/home.php?_rdr')
                                if browser.find('div', {'id': 'header'}):
                                    print('[+][Logged] Service Started successfully')
                                    print('[+][start] Fetching Your Account Name')
                                    browser.open('https://m.facebook.com/profile.php')
                                    user = browser.find_all('strong', {'class': 'bp'})[0].text
                                    print('[+][Welcome] '+user+'')
                                    self.logged = True
                                    self.username = username
                                    self.password = password
                                    print('[+][Done] Fetching Your Account Name')
                                    return True
                                else:
                                    print('[-][Not Logged] Service Stopped System Will Close')
                                    return False
                                    self.sys.exit(1)
                        pass
                    except Exception as e:
                        print('[-][Not Logged] Service Stopped ' + self.traceback.print_exc() + ' System Will Close')
                        return False
                        self.sys.exit(1)
                        pass

                def friend_list_gen(self):  # to get friends list
                    try:
                        if self.logged:
                            friends = {}
                            self.browser.open(
                                'https://m.facebook.com/friends/center/friends/?fb_ref=fbm&ref_component=mbasic_bookmark&ref_page=XMenuController')
                            while 1:
                                try:
                                    if self.browser.find('div', {'id': 'header'}):
                                        for item in self.browser.find_all('a'):
                                            if str(item['href']).__contains__('/friends/hovercard/mbasic/?uid='):
                                                if not str(item).split('>')[1].split('<')[0] in friends:
                                                    friends[str(item).split('>')[1].split('<')[0]] = item['href']
                                                else:
                                                    if not friends[str(item).split('>')[1].split('<')[0]] == item['href']:
                                                        friends[
                                                            str(item).split('>')[1].split('<')[0] + str(
                                                                self.random.randint(0, 999999999))] = item['href']
                                            elif str(item['href']).__contains__('/friends/center/friends/?ppk='):
                                                self.browser.open('http://m.facebook.com' + item['href'])
                                        if not str(self.browser.parsed).__contains__('/friends/center/friends/?ppk='):
                                            break
                                    else:
                                        print('[-][Not Logged] Service Stopped')
                                        self.sys.exit(1)
                                        break
                                    pass
                                except:
                                    break
                                    pass
                            if self.logged and friends.__len__() > 0:
                                print('[+][Log] Friends Number: [' + str(friends.__len__()) + ']')
                                return friends
                            elif self.logged and friends.__len__() == 0:
                                print('[+][Log] Friends Number: [0] Service will stop')
                                self.sys.exit(1)
                            else:
                                pass
                                pass
                        else:
                            print('[-][Not Logged] Service Stopped')
                            pass
                        self.sys.exit(1)
                        pass
                    except:
                        pass

                def group_list_gen(self):  # to get joinned groups
                    try:
                        if self.logged:
                            group_list = {}
                            self.browser.open('https://m.facebook.com/groups')
                            while self.browser.find_all('div')[7].find_all('ul')[0].find_all('a')[len(
                                    self.browser.find_all('div')[7].find_all('ul')[0].find_all(
                                        'a')) - 1].text == 'See All':
                                for a in self.browser.find_all('div')[7].find_all('ul')[0].find_all('a'):
                                    if a.text != 'See All':
                                        if a.text not in group_list or group_list[a.text] != a['href']:
                                            group_list[a.text] = a['href']
                                        elif a.text in group_list or group_list[a.text] != a['href']:
                                            group_list[a.text + str(self.random.randint(0, 9999999))] = a['href']
                                        else:
                                            pass
                                    else:
                                        self.browser.open('https://m.facebook.com' + a['href'])
                                        pass
                                    pass
                                pass
                            for a in self.browser.find_all('div')[7].find_all('ul')[0].find_all('a'):
                                if a.text != 'See All':
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
                        self.sys.exit(1)
                        pass
                    except:
                        pass

                def account_name_gen(self):  # to get account name
                    try:
                        if self.logged:
                            self.browser.open('https://m.facebook.com/profile.php')
                            self.account_url = 'https://m.facebook.com' + \
                                               self.browser.find_all('div', {'id': 'header'})[0].find_all('div')[
                                                   0].find_all(
                                                   'a')[
                                                   2][
                                                   'href']
                            self.account_name = self.browser.find_all('strong', {'class': 'bp'})[0].text
                        else:
                            print('[-][Not Logged] Service Stopped')
                    except:
                        pass

                def pages_list_gen(self):  # to get all liked pages
                    try:
                        if self.logged:
                            pages_list = {}
                            see_more = []
                            m = 11
                            account = str(self.account_url).split('?')[0].split('/')[3]
                            self.browser.open('https://m.facebook.com/' + account + '?v=likes')
                            for div in self.browser.find_all('div', {'id': 'root'})[0].find_all('div')[0].find_all(
                                    'div'):
                                if div.find_all('h4', {'class': 'bv i'}):
                                    for a in div.find_all('a'):
                                        try:
                                            if str(a['href']).split('?')[1] == 'fref=none':
                                                if a.text not in pages_list or pages_list[a.text] != a['href']:
                                                    pages_list[a.text] = a['href']
                                                elif a.text in pages_list or pages_list[a.text] != a['href']:
                                                    pages_list[a.text + str(self.random.randint(0, 9999999))] = a[
                                                        'href']
                                                else:
                                                    pass
                                            else:
                                                if a.text == 'See More':
                                                    see_more.append('https://m.facebook.com' + a['href'])
                                        except:
                                            pass
                                        pass
                                    pass
                                else:
                                    pass
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
                                                    if a.text not in pages_list or pages_list[a.text] != a['href']:
                                                        pages_list[a.text] = a['href']
                                                    elif a.text in pages_list or pages_list[a.text] != a['href']:
                                                        pages_list[a.text + str(self.random.randint(0, 9999999))] = a[
                                                            'href']
                                                    else:
                                                        pass
                                                else:
                                                    pass
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
                        self.sys.exit(1)
                        pass
                    except:
                        pass

                def url_encoder(self, message):  # to encode urls to stop facebook from blocking urls
                    try:
                        urls = self.re.findall(
                            'http[s]?://(?:[a-za-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fa-f][0-9a-fa-f]))+',
                            message)
                        l = [self.string.ascii_lowercase, self.string.ascii_uppercase]
                        ran = l[self.random.randint(0, 1)]
                        for url in urls:
                            encrypted = ''.join(self.random.choice(ran) for _ in range(self.random.randint(7, 34)))
                            self.browser.open(
                                'http://tinyurl.com/create.php?source=indexpage&url=' + url + '&submit=make+tinyurl!&alias=' + encrypted)
                            message = message.replace(url,
                                                      self.browser.find('div', {'id': 'copyinfo'})[
                                                          'data-clipboard-text'])
                            return message
                        return message
                    except:
                        return message
                    pass

                def message_all(self, message=None, sleep_thread=0):  # to send message for all friends
                    try:
                        if self.logged:
                            print('[+][Log][start] Post Message To All Service')
                            self.Browse_Profile = self.webdriver.FirefoxProfile()
                            self.Browse_Profile.set_preference('general.useragent.override',
                                                               'Mozilla/5.0 (Macintosh; PPC Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0')
                            self.Browser = self.webdriver.Firefox(self.Browse_Profile)
                            self.Browser.get('https://m.facebook.com')
                            try:
                                self.Browser.find_element_by_name('email').send_keys(self.username)
                                self.Browser.find_element_by_name('pass').send_keys(self.password)
                                self.Browser.find_element_by_name('login').click()
                                pass
                            except:
                                pass
                            friends = self.friends
                            for friend_name, friend_url in friends.items():
                                self.Browser.get('https://m.facebook.com' + friend_url)
                                for a in self.Browser.find_elements_by_tag_name('a'):
                                    try:
                                        if str(a.get_attribute('href')).endswith('hovercard'):
                                            self.Browser.get(a.get_attribute('href'))
                                            break
                                        else:
                                            pass
                                        pass
                                    except TypeError:
                                        pass
                                    except:
                                        pass
                                for a in self.Browser.find_elements_by_tag_name('a'):
                                    try:
                                        if str(a.get_attribute('href')).__contains__('/messages/thread'):
                                            self.Browser.get(a.get_attribute('href'))
                                            break
                                        else:
                                            pass
                                        pass
                                    except TypeError:
                                        pass
                                    except:
                                        pass
                                try:
                                    message = self.url_encoder(message)
                                    self.Browser.find_element_by_name('body').send_keys(self.url_encoder(message))
                                    self.Browser.find_element_by_name('send').click()
                                    print('[+][Log][success] Post Message To All Service :[' + friend_name + ']')
                                    pass
                                except TypeError:
                                    pass
                                except:
                                    try:
                                        message = self.url_encoder(message)
                                        self.Browser.find_element_by_name('body').send_keys(self.url_encoder(message))
                                        self.Browser.find_element_by_name('Send').click()
                                        print('[+][Log][success] Post Message To All Service :[' + friend_name + ']')
                                        pass
                                    except TypeError:
                                        pass
                                    except:
                                        print('[+][Log][failed] Post Message To All Service :[' + friend_name + ']')
                                        pass
                                    pass
                                self.time.sleep(sleep_thread)
                                pass
                            self.Browser.quit()
                            print('[+][Log][Done] Post Message To All Service')
                            pass
                        else:
                            print('[-][Not Logged] Service Stopped')
                            pass
                        self.Browser.quit()
                        self.sys.exit(1)
                        print('[+][Done] Post To All Friends Messages')
                        pass
                    except Exception as e:
                        pass

                def wall_message_for_all(self, message=None, sleep_thread=0):  # to set message for all friends profiles walls
                    try:
                        if self.logged:
                            print('[+][Log][start] Wall Message Service')
                            self.Browse_Profile = self.webdriver.FirefoxProfile()
                            self.Browse_Profile.set_preference('general.useragent.override',
                                                               'Mozilla/5.0 (Macintosh; PPC Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0')
                            self.Browser = self.webdriver.Firefox(self.Browse_Profile)
                            self.Browser.get('https://m.facebook.com')
                            try:
                                self.Browser.find_element_by_name('email').send_keys(self.username)
                                self.Browser.find_element_by_name('pass').send_keys(self.password)
                                self.Browser.find_element_by_name('login').click()
                                pass
                            except:
                                pass
                            friends = self.friends
                            for friend_name, friend_url in friends.items():
                                self.Browser.get('https://m.facebook.com' + friend_url)
                                for a in self.Browser.find_elements_by_tag_name('a'):
                                    try:
                                        if str(a.get_attribute('href')).endswith('hovercard'):
                                            self.Browser.get(a.get_attribute('href'))
                                            break
                                        else:
                                            pass
                                        pass
                                    except:
                                        pass
                                try:
                                    message = self.url_encoder(message)
                                    self.Browser.find_element_by_name('xc_message').send_keys(self.url_encoder(message))
                                    self.Browser.find_element_by_name('view_post').click()
                                    self.time.sleep(sleep_thread)
                                    print('[+][Log][success] Wall Message Service :[' + friend_name + ']')
                                    pass
                                except:
                                    print('[+][Log][failed] Message Service :[' + friend_name + ']')
                                    pass
                        else:
                            print('[-][Not Logged] Wall Message Service Stopped')
                            pass
                        self.Browser.quit()
                        self.sys.exit(1)
                        print('[+][Done] Post To All Friends Walls')
                        pass
                    except:
                        pass

                def autobot(self, message=None):  # for auto reply
                    try:
                        if self.logged:
                            print('[+][Log][Start] Auto Bot (messages) Service')
                            message_list = {}
                            self.Browse_Profile = self.webdriver.FirefoxProfile()
                            self.Browse_Profile.set_preference('general.useragent.override',
                                                               'Mozilla/5.0 (Macintosh; PPC Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0')
                            self.Browser = self.webdriver.Firefox(self.Browse_Profile)
                            self.Browser.get('https://m.facebook.com')
                            try:
                                self.Browser.find_element_by_name('email').send_keys(self.username)
                                self.Browser.find_element_by_name('pass').send_keys(self.password)
                                self.Browser.find_element_by_name('login').click()
                                pass
                            except:
                                pass
                            while True:
                                message = self.url_encoder(message)
                                self.Browser.get('https://m.facebook.com/messages')
                                for element in self.Browser.find_elements_by_tag_name('table'):
                                    if element.value_of_css_property('background-color') == 'rgba(236, 239, 245, 1)':
                                        if not element.find_element_by_tag_name('a').text in message_list:
                                            message_list[
                                                element.find_element_by_tag_name(
                                                    'a').text] = element.find_element_by_tag_name(
                                                'a').get_attribute('href')
                                            pass
                                        else:
                                            message_list[element.find_element_by_tag_name('a').text + str(
                                                self.random.randint(0, 99999999))] = element.find_element_by_tag_name(
                                                'a').get_attribute('href')
                                    pass
                                for message_name, message_url in message_list.items():
                                    if message_list[message_name] != 'delete':
                                        try:
                                            self.Browser.get(message_url)
                                            self.time.sleep(2)
                                            self.Browser.find_element_by_name('body').send_keys(message)
                                            self.Browser.find_element_by_name('send').click()
                                            message_list[message_name] = 'delete'
                                            print('[+][success] Auto Bot (messages) Service :[' +
                                                  str(message_name).split('(')[
                                                      0] + ']')
                                            pass
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
                            pass
                        else:
                            print('[-][Not Logged] Service Stopped')
                            pass
                        self.sys.exit(1)
                        pass
                    except:
                        pass

                def post_to_groups_wall(self, post=None, sleep_thread=0):  # to post some posts in group
                    try:
                        if self.logged:
                            print('[+][Log][Start] Post To Groups Wall Service')
                            self.Browse_Profile = self.webdriver.FirefoxProfile()
                            self.Browse_Profile.set_preference('general.useragent.override',
                                                               'Mozilla/5.0 (Macintosh; PPC Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0')
                            self.Browser = self.webdriver.Firefox(self.Browse_Profile)
                            self.Browser.get('https://m.facebook.com')
                            try:
                                self.Browser.find_element_by_name('email').send_keys(self.username)
                                self.Browser.find_element_by_name('pass').send_keys(self.password)
                                self.Browser.find_element_by_name('login').click()
                                pass
                            except:
                                pass
                            groups = self.group_list
                            for group_name, group_url in groups.items():
                                try:
                                    self.Browser.get('https://m.facebook.com/' + group_url)
                                    self.time.sleep(1)
                                    self.Browser.find_element_by_name('xc_message').send_keys(self.url_encoder(post))
                                    self.Browser.find_element_by_name('view_post').click()
                                    self.time.sleep(1)
                                    print('[+][Log][success] Post To Groups Wall Service :[' + group_name + ']')
                                    self.time.sleep(sleep_thread)
                                    pass
                                except:
                                    print('[+][Log][failed] Post To Groups Wall Service :[' + group_name + ']')
                                    pass
                                pass
                            print('[+][Log][Done] Post To Groups Wall Service')
                            self.Browser.quit()
                            pass
                        else:
                            print('[-][Not Logged] Service Stopped')
                            pass
                        self.sys.exit(1)
                        pass
                    except:
                        pass

                def post_to_pages_posts(self, post=None, sleep_thread=0):  # to comment in last post in all liked pages
                    try:
                       if self.logged:
                           page = self.pages_list
                           print('[+][Log][Start] Post To Pages Posts Service')
                           for page_name, page_url in page.items():
                               try:
                                   xm = 0
                                   self.browser.open('https://m.facebook.com' + page_url)
                                   for comment_div in self.browser.find_all('div'):
                                       try:
                                           if str(comment_div['id']).startswith('u_'):
                                               if xm < 1:
                                                   for a in comment_div.find_all('a'):
                                                       if str(a.text).lower().__contains__('comment'):
                                                           xm = 1
                                                           a = 'https://m.facebook.com' + a['href']
                                                           self.browser.open(a)
                                                           form = self.browser.get_form(
                                                               self.browser.find_all('form')[0])
                                                           post = self.url_encoder(post)
                                                           form['comment_text'].value = post
                                                           self.browser.submit_form(form, 'https://m.facebok.com' +
                                                                                    self.browser.find_all('form')[0][
                                                                                        'action'])
                                                           self.time.sleep(sleep_thread)
                                                           break
                                                           pass
                                                       pass
                                                   pass
                                               else:
                                                   break
                                       except:
                                           pass
                                   self.time.sleep(1)
                                   print('[+][Log][Success] Post To Pages Posts Service :[' + page_name + ']')
                                   pass
                               except:
                                   print('[+][Log][Failed] Post To Pages Posts Service :[' + page_name + ']')
                                   pass
                               pass
                           print('[+][Log][Done] Post To Pages Posts Service')
                           pass
                       else:
                           print('[-][Not Logged] Service Stopped')
                           pass
                       self.sys.exit(1)
                       pass
                    except:
                        pass

                def auto_liker(self, sleep_thread=2):
                    try:
                        if self.logged and self.friends.__len__() > 0:
                            print('[+][Start] Like Post Service')
                            for friend_name, friend_url in self.friends.items():
                                post_links = []
                                self.browser.open('https://m.facebook.com' + friend_url)
                                for hovera in self.browser.find_all('a'):
                                    if str(hovera['href']).endswith('hovercard'):
                                        self.browser.open('https://m.facebook.com' + hovera['href'])
                                        break
                                        pass
                                    pass
                                for div in self.browser.find_all('div'):
                                    try:
                                        if str(div['id']).startswith('u_'):
                                            for a in div.find_all('a'):
                                                if str(a['href']).__contains__('/a/like.php') and \
                                                                str(a['href']).split('?')[1].split('&')[0] == 'ul':
                                                    post_links.append('https://m.facebook.com' + a['href'])
                                                    pass
                                                pass
                                            pass
                                        else:
                                            pass
                                        pass
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
                        self.sys.exit(1)
                        pass
                    except:
                        pass
                    pass

                def auto_liker_bot(self, sleep_thread=2):
                    try:
                        if self.logged and self.friends.__len__() > 0:
                            print('[+][Start] Like Post (bot) Service')
                            liked = []
                            hovers = {}
                            links = {}
                            poster = {}
                            print('[+][start] Getting Friends Profile Links Service')
                            for friend_name, friend_url in self.friends.items():
                                self.browser.open('https://m.facebook.com' + friend_url)
                                for hovera in self.browser.find_all('a'):
                                    if str(hovera['href']).endswith('hovercard'):
                                        hovers[friend_name] = ('https://m.facebook.com' + hovera['href'])
                                        break
                                        pass
                                    pass
                                pass
                            print('[+][Done] Getting Friends Profile Links Service')
                            while True:
                                for link_name, link_url in hovers.items():
                                    try:
                                        self.browser.open(link_url)
                                        for div in self.browser.find_all('div'):
                                            try:
                                                if str(div['id']).startswith('u_'):
                                                    for a in div.find_all('a'):
                                                        if str(a['href']).__contains__('/a/like.php') and \
                                                                        str(a['href']).split('?')[1].split('&')[
                                                                            0] == 'ul':
                                                            if not 'https://m.facebook.com' + a['href'] in liked:
                                                                self.browser.open('https://m.facebook.com' + a['href'])
                                                                print(
                                                                    '[+][Log][success] Like Post Service : [' + link_name + ']')
                                                                liked.append('https://m.facebook.com' + a['href'])
                                                                self.time.sleep(sleep_thread)
                                                            pass
                                                        pass
                                                    pass
                                                else:
                                                    pass
                                                pass
                                            except Exception as e:
                                                pass
                                    except Exception as m:
                                        pass
                                    pass
                            print('[+][Done] Like Post (bot) Service')
                            pass
                        else:
                            print('[-][Not Logged] Service Stopped')
                            pass
                        self.sys.exit(1)
                        pass
                    except:
                        pass
                    pass

                def watcher(self, number_of_activities=10):
                    try:
                        if self.logged:
                            try:
                                print('[+][Start] Watching Service')
                                self.Browse_Profile = self.webdriver.FirefoxProfile()
                                self.Browse_Profile.set_preference('general.useragent.override',
                                                                   'Mozilla/5.0 (Macintosh; PPC Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0')
                                self.Browser = self.webdriver.Firefox(self.Browse_Profile)
                                self.Browser.maximize_window()
                                self.Browser.get('https://www.facebook.com/login.php')
                                links = {}
                                try:
                                    self.Browser.find_element_by_name('email').send_keys(self.username)
                                    self.Browser.find_element_by_name('pass').send_keys(self.password)
                                    self.Browser.find_element_by_id('loginbutton').click()
                                    pass
                                except:
                                    pass
                                self.time.sleep(5)
                                m = 1
                                x = number_of_activities
                                number_of_activities = int(round(number_of_activities * (0.25)))
                                for _ in range(number_of_activities):
                                    for div in self.Browser.find_elements_by_class_name('fbFeedTickerStory'):
                                        try:
                                            div.send_keys(self.Keys.ARROW_DOWN)
                                            pass
                                        except:
                                            pass
                                        pass
                                    pass
                                pass
                                for a in self.Browser.find_element_by_id('pagelet_ticker').find_elements_by_tag_name(
                                        'a'):
                                    if links.__len__() < x:
                                        if str(a.text).__len__() > 0:
                                            if a.find_element_by_class_name('fwb').text not in links:
                                                print(
                                                    '[+][' + str(
                                                        m) + '][Log][success] Notification : [' + a.find_element_by_class_name(
                                                        'fwb').text +
                                                    '][' + str(a.text).strip().replace("\n",
                                                                                       '') + '] @URL: [' + a.get_attribute(
                                                        'href') + ']')
                                                links[a.find_element_by_class_name('fwb').text] = a.get_attribute(
                                                    'href')
                                                m += 1
                                            elif a.find_element_by_class_name('fwb').text in links or links[
                                                a.find_element_by_class_name('fwb').text] != a.get_attribute('href'):
                                                print(
                                                    '[+][' + str(
                                                        m) + '][Log][success] Notification : [' + a.find_element_by_class_name(
                                                        'fwb').text +
                                                    '][' + str(a.text).strip().replace("\n",
                                                                                       '') + '] @URL: [' + a.get_attribute(
                                                        'href') + ']')
                                                m += 1
                                                links[a.find_element_by_class_name('fwb').text + 'New' + str(
                                                    self.random.randint(0, 99999999))] = a.get_attribute('href')
                                            else:
                                                break
                                                pass
                                print('[+][Done] Watching (Bot) Service')
                            except:
                                pass
                        else:
                            print('[-][Not Logged] Service Stopped')
                            pass
                        self.Browser.close()
                        self.Browser.quit()
                        self.sys.exit(1)
                        pass
                    except:
                        pass
                    pass

                def watcher_bot(self):
                    try:
                        if self.logged:
                            try:
                                print('[+][Start] Watching Service')
                                self.Browse_Profile = self.webdriver.FirefoxProfile()
                                self.Browse_Profile.set_preference('general.useragent.override',
                                                                   'Mozilla/5.0 (Macintosh; PPC Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0')
                                self.Browser = self.webdriver.Firefox(self.Browse_Profile)
                                self.Browser.maximize_window()
                                self.Browser.get('https://www.facebook.com/login.php')
                                links = {}
                                try:
                                    self.Browser.find_element_by_name('email').send_keys(self.username)
                                    self.Browser.find_element_by_name('pass').send_keys(self.password)
                                    self.Browser.find_element_by_id('loginbutton').click()
                                    pass
                                except:
                                    pass
                                self.time.sleep(5)
                                m = 1
                                while 1:
                                    for a in self.Browser.find_element_by_id(
                                            'pagelet_ticker').find_elements_by_tag_name(
                                            'a'):
                                        if str(a.text).__len__() > 0:
                                            if a.find_element_by_class_name('fwb').text not in links:
                                                print(
                                                    '[+][' + str(
                                                        m) + '][Log][success] Notification : [' + a.find_element_by_class_name(
                                                        'fwb').text +
                                                    '][' + str(a.text).strip().replace("\n",
                                                                                       '') + '] @URL: [' + a.get_attribute(
                                                        'href') + ']')
                                                links[a.find_element_by_class_name('fwb').text] = a.get_attribute(
                                                    'href')
                                                m += 1
                                            else:
                                                self.time.sleep(10)
                                                self.Browser.refresh()
                                                break
                                                pass
                                print('[+][Done] Watching (Bot) Service')
                            except:
                                pass
                        else:
                            print('[-][Not Logged] Service Stopped')
                            pass
                        self.Browser.close()
                        self.Browser.quit()
                        self.sys.exit(1)
                        pass
                    except:
                        pass
                    pass

                def Message_To_All(self, message=None, sleep_thread=2):
                    try:
                        self.login()
                        print('[+][start] Friend List Generator Service')
                        self.friends = self.friend_list_gen()
                        print('[+][Done] Friend List Generator Service')
                        self.message_all(message, sleep_thread)
                        pass
                    except:
                        pass

                def Post_To_Groups_Wall(self, Post=None, sleep_thread=2):
                    try:
                        self.login()
                        print('[+][start] Groups List Generator Service')
                        self.group_list = self.group_list_gen()
                        print('[+][Done] Groups List Generator Service')
                        self.Post_To_Groups_Wall(Post, sleep_thread)
                        pass
                    except:
                        pass

                def Wall_Message_To_All(self, message=None, sleep_thread=2):
                    try:
                        self.login()
                        print('[+][start] Friend List Generator Service')
                        self.friends = self.friend_list_gen()
                        print('[+][Done] Friend List Generator Service')
                        self.wall_message_for_all(message, sleep_thread)
                        pass
                    except:
                        pass
                    pass

                def Comment_To_Pages_Posts(self, comment=None, sleep_thread=2):
                    try:
                        self.login()
                        print('[+][start] Pages List Generator Service')
                        self.pages_list = self.pages_list_gen()
                        print('[+][Done] Pages List Generator Service')
                        self.post_to_pages_posts(comment, sleep_thread)
                        pass
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
                    except:
                        pass
                    pass

                def Watcher(self, number_of_activities=10):
                    try:
                        self.watcher(number_of_activities)
                    except:
                        pass

                def Watcher_BOT(self):
                    try:
                        self.watcher_bot()
                    except:
                        pass
                    pass

                def Auto_bot(self, message):
                    try:
                        self.login()
                        self.autobot(message)
                    except:
                        pass
                    pass

                def Service_Start(self):
                    try:
                        print(self.Coder)
                        username = input('[+]Facebook Account Name: ')
                        password = self.getpass.getpass('[+]Facebook Account Password: ')
                        self.Login(username, password)
                        try:
                            choose = int(input('Please Choose One Of this Services To Start:'
                                  '\n[+][1] Message To All'
                                  '\n[+][2] Post To All Friends Walls'
                                  '\n[+][3] Auto Message BOT'
                                  '\n[+][4] Post To All Groups Walls'
                                  '\n[+][5] Comment On Last Pages Posts'
                                  '\n[+][6] Auto Liker For All Friends'
                                  '\n[+][7] Auto Liker For All Friends (BOT)'
                                  '\n[+][8] Watcher'
                                  '\n[+][9] Watcher (BOT)'
                                  '\n[+][Choose] Enter Your Choise: '))
                            if choose > 0 and choose < 10:
                                if choose == 1:
                                    message = input('[+]You have chose Message To All'
                                                    '\n[+]Enter Your Message Text To Start: ')
                                    thread = 2
                                    try:
                                        thread = int(input('[+]Enter Thread Sleep in seconds (optional set to zero for None) : '))
                                    except:
                                        pass
                                    if str(message).strip().replace(' ', '').__len__() > 0:
                                        self.Message_To_All(message, thread)
                                    else:
                                        print(
                                            '[-][error] Message Is Empty. System Will Exit')
                                        self.sys.exit(1)
                                elif choose == 2:
                                    message = input('[+]You have chose Post To All Friends Walls'
                                                    '\n[+]Enter Your Post Text To Start: ')
                                    try:
                                        thread = int(
                                            input('[+]Enter Thread Sleep in seconds (optional set to zero for None) : '))
                                    except:
                                        pass
                                    if str(message).strip().replace(' ', '').__len__() > 0:
                                        self.Wall_Message_To_All(message, thread)
                                    else:
                                        print(
                                            '[-][error] Message Is Empty. System Will Exit')
                                        self.sys.exit(1)
                                elif choose == 3:
                                    message = input('[+]You have chose Auto Bot Message'
                                                    '\n[+]Enter Your Message Text To Start: ')
                                    if str(message).strip().replace(' ', '').__len__() > 0:
                                        self.Auto_bot(message)
                                    else:
                                        print(
                                            '[-][error] Message Is Empty. System Will Exit')
                                        self.sys.exit(1)
                                elif choose == 4:
                                    message = input('[+]You have chose Post To All Groups Walls'
                                                    '\n[+]Enter Your Post Text To Start: ')
                                    try:
                                        thread = int(
                                            input(
                                                '[+]Enter Thread Sleep in seconds (optional set to zero for None) : '))
                                    except:
                                        pass
                                    if str(message).strip().replace(' ', '').__len__() > 0:
                                        self.Post_To_Groups_Wall(message, thread)
                                    else:
                                        print(
                                            '[-][error] Message Is Empty. System Will Exit')
                                        self.sys.exit(1)
                                elif choose == 5:
                                    message = input('[+]You have chose Comment On Last Pages Posts'
                                                    '\n[+]Enter Your Comment Text To Start: ')
                                    thread = 2
                                    try:
                                        thread = int(input(
                                            '[+]Enter Thread Sleep in seconds (optional set to zero for None) : '))
                                    except:
                                        pass
                                    if str(message).strip().replace(' ', '').__len__() > 0:
                                        self.Comment_To_Pages_Posts(message, thread)
                                    else:
                                        print(
                                            '[-][error] Message Is Empty. System Will Exit')
                                        self.sys.exit(1)
                                elif choose == 6:
                                    thread = 2
                                    try:
                                        thread = int(input('[+]You have chose Auto Liker For All Friends'
                                                    '\n[+]Enter Thread Sleep in seconds (optional set to zero for None) : '))
                                    except:
                                        pass
                                    self.Auto_Liker(thread)
                                elif choose == 7:
                                    thread = 2
                                    try:
                                        thread = int(input('[+]You have chose Auto Liker For All Friends (BOT)'
                                                           '\n[+]Enter Thread Sleep in seconds (optional set to zero for None) : '))
                                    except:
                                        pass
                                    self.Auto_Liker_BOT(thread)
                                elif choose == 8:
                                    activity = 10
                                    try:
                                        activity = int(input('[+]You have chose Watcher'
                                                             '\n[+]Enter Number Of Activities To Get: '))
                                    except:
                                        pass
                                    self.Watcher(activity)
                                elif choose == 9:
                                    print('[+]You have chose Watcher')
                                    self.Watcher_BOT()
                                else:
                                    print(
                                        '[-][error] Message Is Empty. System Will Exit')
                                    self.sys.exit(1)
                                    pass
                                pass
                            else:
                                print('[-][error] You Must Choose Number between 1 and 9 to Start. System Will Exit')
                                self.sys.exit(1)
                            pass
                        except:
                            print('[-][error] You Must Choose Number To Start. System Will Exit')
                            self.sys.exit(1)
                            pass
                    except:
                        pass
                    pass

        except Exception as e:
            print('[error] Something Occurred '+str(e))

Facebook().Auto_Bot()
