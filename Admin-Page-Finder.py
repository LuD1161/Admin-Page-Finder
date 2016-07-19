import urllib,re,sys,time
from urllib.request import urlopen

_author_='Aseem Shrey'

links=['adm/','admin/','admin/account','admin/login','admin/home','admin/controlpanel','admin/cp','admin/adminLogin','admin/admin_login','admin/controlpanel','admin/admin-login','admin-login','admin/account','admin/admin','admin','adminitem/','adminitem','adminitems/','adminitems','administrator/','administrator/login','administrator','administration/','administration','adminLogin/','adminlogin','admin_area/admin','admin_area/','admin_area/login','manager/','manager','letmein/','letmein','superuser/','superuser','access/','access','sysadm/','sysadm','superman/','supervisor/','panel','control/','control','member/','member','members/','members','user/','user','cp/','uvpanel/','manage/','manage','management/','management','signin/','signin','log-in/','log-in','log_in/','log_in','sign_in/','sign_in','sign-in/','sign-in','users/','users','accounts/','accounts','wp-login','bb-admin/login','bb-admin/admin','bb-admin/admin','administrator/account','relogin','relogin','check','relogin','blog/wp-login','user/admin','users/admin','registration/','processlogin','checklogin','checkuser','checkadmin','isadmin','authenticate','authentication','auth','authuser','authadmin','cp','modelsearch/login','moderator','moderator/','controlpanel/','controlpanel','admincontrol','adminpanel','fileadmin/','fileadmin','sysadmin','admin1','admin1','admin1','admin2','admin2','yonetim','yonetim','yonetici','yonetici','phpmyadmin/','myadmin/','ur-admin','ur-admin/','Server','Server/','wp-admin/','administr8','administr8/','webadmin/','webadmin','administratie/','admins/','admins','administrivia/','Database_Administration/','useradmin/','sysadmins/','admin1/','system-administration/','administrators/','pgadmin/','directadmin/','staradmin/','ServerAdministrator/','SysAdmin/','administer/','LiveUser_Admin/','sys-admin/','typo3/','panel/','cpanel/','cpanel_file/','platz_login/','rcLogin/','blogindex/','formslogin/','autologin/','support_login/','meta_login/','manuallogin/','simpleLogin/','loginflat/','utility_login/','showlogin/','memlogin/','login-redirect/','sub-login/','wp-login/','login1/','dir-login/','login_db/','xlogin/','smblogin/','customer_login/','UserLogin/','login-us/','acct_login/','bigadmin/','project-admins/','phppgadmin/','pureadmin/','sql-admin/','radmind/','openvpnadmin/','wizmysqladmin/','vadmind/','ezsqliteadmin/','hpwebjetadmin/','newsadmin/','adminpro/','Lotus_Domino_Admin/','bbadmin/','vmailadmin/','Indy_admin/','ccp14admin/','irc-macadmin/','banneradmin/','sshadmin/','phpldapadmin/','macadmin/','administratoraccounts/','admin4_account/','admin4_colon/','radmind-1/','Super-Admin/','AdminTools/','cmsadmin/','SysAdmin2/','globes_admin/','cadmins/','phpSQLiteAdmin/','navSiteAdmin/','server_admin_small/','logo_sysadmin/','power_user/','system_administration/','ss_vms_admin_sm/','bb-admin/','panel-administracion/','instadmin/','memberadmin/','administratorlogin/','adm','admin_login','panel-administracion/login','pages/admin/admin-login','pages/admin/','acceso','admincp/login','admincp/','adminarea/','admincontrol/','affiliate','adm_auth','memberadmin','administratorlogin','modules/admin/','administrators','siteadmin/','siteadmin','adminsite/','kpanel/','vorod/','vorod','vorud/','vorud','adminpanel/','PSUser/','secure/','webmaster/','webmaster','autologin','userlogin','admin_area','cmsadmin','security/','usr/','root/','secret/','admin/login','admin/adminLogin','moderator','moderator','moderator/login','moderator/admin','yonetici','0admin/','0manager/','asadmin/','cgi-bin/login','login1','login_admin/','login_admin','login_out/','login_out','login_user','loginerror/','loginok/','loginsave/','loginsuper/','loginsuper','login','logout/','logout','secrets/','super1/','super1','super_index','super_login','supermanager','superman','superuser','supervise/','supervise/Login','super']

count = 0
nameOfFile = ''
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
head = { 'User-Agent' : user_agent }
print('''
|  ____ ___  _  _ _ _  _   ___  ____ ____ ____   ____ _ _  _ ___  ____ ____ |
|  |__| |  \ |\/| | |\ |   |__] |__| | __ |___   |___ | |\ | |  \ |___ |__/ |
|  |  | |__/ |  | | | \|   |    |  | |__] |___   |    | | \| |__/ |___ |  \ |
|                                                                           |

-- LuD1161
''')

def isUP(url):
    global user_agent,head
    try:
        req = urllib.request.Request(url,headers = head)
        res = urllib.request.urlopen(req)
        if res.getcode() == 200:
            res.close()
            return True
        elif res.getcode() == 302:
            res.close()
            return True
    except Exception as e:
        return False
    finally:
        try:
            res.close()
        except NameError:
            pass

def naming(nameOfFile):
    name = ''
    for c in nameOfFile:
        if c.isalnum():
            name=name+c
    date = time.strftime("%x")
    date = date.replace('/','-')
    nameOfFile=date+'-'+name+'.txt'
    return nameOfFile


def Connection(url):
    global nameOfFile,user_agent,head
    try:
        print('Testing Link '+url+' . . .')
        req = urllib.request.Request(url,headers = head)
        res = urllib.request.urlopen(req)
        respData = res.read()
        respData =respData.decode('utf-8')
        m=rx.search(respData)
        if m:
            print('Found at '+url)
            if nameOfFile == '':
                print('Please specify the name of file to write in')
                nameOfFile = input()
                nameOfFile=naming(nameOfFile)
                file = open(nameOfFile,'a+')
            else:
                print('Writing in file '+nameOfFile)
                file = open(nameOfFile,'a+')
            file.write('200'+url+'\n')
            file.close()
            print('Do you wish to continue (Y/N) ?')
            answer = input()
            answer = answer.lower()
            if answer == 'n':
                formatting(nameOfFile)

    except urllib.error.HTTPError as e:
        if int(e.code) == 404:
            pass
        elif int(e.code) == 401:
            print('This link seems interesting , it needs credentials (maybe default works ;) )')
            print('Should I write this link to file for Brute forcing later (or just for further analysis) ;) (Y/N) ? ')
            answer=input()
            answer=answer.lower()
            if answer == 'y':
                if nameOfFile == '':
                    print('Please specify the name of file')
                    nameOfFile = input()
                    nameOfFile=naming(nameOfFile)
                    file = open(nameOfFile,'a+')
                else:
                    file = open(nameOfFile,'a+')
                file.write('401'+url+'\n')
                file.close()
        elif int(e.code) == 302:
            print('It seems this link follows a redirect')
            print('Do you want this link to be written to file (Y/N) ?')
            answer=input()
            answer=answer.lower()
            if answer == 'y':
                print('Please specify the name of file')
                nameOfFile = input()
                nameOfFile=naming(nameOfFile)
                file = open(nameOfFile,'a+')
                file.write('302'+url+'\n')
                file.close()
        else:
            print (e)

    finally:
        try:
            res.close()
        except NameError:
            pass

def test(choice):
    global count
    for link in links:
        count=count+1
        if link[-1:] == '/':
            temp = 'http://'+url+'/'+link
        else:
            if choice == 1:
                temp = 'http://'+url+'/'+link+'.php'
            elif choice == 2:
                temp = 'http://'+url+'/'+link+'.asp'
            elif choice == 3:
                temp = 'http://'+url+'/'+link+'.js'
            elif choice == 4:
                temp = 'http://'+url+'/'+link+'.cgi'
            elif choice == 5:
                temp = 'http://'+url+'/'+link+'.cfm'
            elif choice == 6:
                temp = 'http://'+url+'/'+link+'.brf'
            print('Testing '+temp+' ...')
            found=Connection(temp)

    if found == 0:
        print('Not Found :( , even though I checked '+count+'links ')


def robots(url):
    global count
    rx=re.compile('Disallow:')
    newDirs = []
    try:
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
        req = urllib.request.Request('http://'+url+'/robots.txt', headers = headers)
        resp = urllib.request.urlopen(req)
        respData = resp.read()
        respData =respData.decode('utf-8')
        for line in respData.splitlines():
            if 'User-agent' in line:
                continue
            if 'Allow' in line:
                continue
            m=rx.search(respData)
            if m:
                newDirs.append(line.replace('Disallow: ',''))
    except Exception as e:
        print(str(e))

    print('No. of directories found in robots.txt file are :'+str(len(newDirs)))
    for i in range(len(newDirs)):
        link = newDirs[i]
        count=count+1
        link = link[1:]
        if link[-1:] == '/':
            temp = 'http://'+url+'/'+link
            Connection(temp)
        else:
            temp = {'http://'+url+'/'+link+'.php','http://'+url+'/'+link+'.asp','http://'+url+'/'+link+'.js','http://'+url+'/'+link+'.cgi','http://'+url+'/'+link+'.cfm','http://'+url+'/'+link+'.bfk'}
            for url in temp:
                Connection(url)

def formatting(nameOfFile):
    lis = []
    if nameOfFile != '':
        ar401 = []
        ar302 = []
        ar200 = []
        data = 'HTTP Code'
        file = open(nameOfFile,'r+')
        data = file.readline().strip('\n')
        while data !='':
            lis.append(data)
            data=file.readline().strip('\n')
        for temp in lis:
            if (temp.find('401')) != -1:
                ar401.append(temp[3:])
            if (temp.find('302')) != -1:
                ar302.append(temp[3:])
            if (temp.find('200')) != -1:
                ar200.append(temp[3:])
    print(str(len(ar401)))
    print(ar401)
    print(str(len(ar302)))
    print(str(len(ar200)))
    file.close()
    file = open(nameOfFile,'w')
    file.write('\n\t--- Possible Links With Login Pages\n\n')
    for name in ar200:
        file.write(name+'\n')
    file.write('\n\t--- Links With Authentication (Might be default login or Brute Force or for Just Analysis ;) )\n\n')
    for name in ar401:
        file.write(name+'\n')
    file.write('\n\t--- Redirection Pages\n\n')
    for name in ar302:
        file.write(name+'\n')
    sys.exit()

print("Enter the link without http:// \n\n")
print("Like this --- www.google.com\n\n")
print("If the link follows a redirect , please put in the final link ")
url = input()
url = url.lower()
rx = re.compile('Username',re.IGNORECASE)
newDirs = []
if (isUP('http://'+url)):
    pass
else:
    print('The server seems down .')
    print('Exiting . . .')
    time.sleep(1)
    sys.exit()

print('Which type of files do you want to search for ? (Default is both , for default just press enter , will take time )')
print('1. PHP\n2. ASP\n3. JS\n4. CGI\n5. CFM\n6. BRF\n7. Exit')
ans=input()
if ans == '7':
    formatting(nameOfFile)
if ans =='':
    for i in range(1,7):
        test(i)
else:
    ans=int(ans)
    if ans > 0 & ans < 7:
        test(ans)
    else:
        print('Please enter a valid option')
robots(url)
sys.exit()
