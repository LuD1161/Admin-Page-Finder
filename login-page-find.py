import urllib,re
from urllib.request import urlopen

links={'admin','asadmin/','login','login','login/','login','adm/','admin/','admin/account','admin/login','admin/login','admin/home','admin/controlpanel','admin/controlpanel','admin/cp','admin/adminLogin','admin/adminLogin','admin/admin_login','admin/controlpanel','admin/admin-login','admin-login','admin/account','admin/admin','admin','admin','adminitem/','adminitem','adminitems/','adminitems','administrator/','administrator/login','administrator','administration/','administration','adminLogin/','adminlogin','admin_area/admin','admin_area/','admin_area/login','manager/','manager','letmein/','letmein','superuser/','superuser','access/','access','sysadm/','sysadm','superman/','supervisor/','panel','control/','control','member/','member','members/','members','user/','user','cp/','uvpanel/','manage/','manage','management/','management','signin/','signin','log-in/','log-in','log_in/','log_in','sign_in/','sign_in','sign-in/','sign-in','users/','users','accounts/','accounts','wp-login','bb-admin/login','bb-admin/admin','bb-admin/admin','administrator/account','relogin','relogin','check','relogin','blog/wp-login','user/admin','users/admin','registration/','processlogin','checklogin','checkuser','checkadmin','isadmin','authenticate','authentication','auth','authuser','authadmin','cp','modelsearch/login','moderator','moderator/','controlpanel/','controlpanel','admincontrol','adminpanel','fileadmin/','fileadmin','sysadmin','admin1','admin1','admin1','admin2','admin2','yonetim','yonetim','yonetici','yonetici','phpmyadmin/','myadmin/','ur-admin','ur-admin/','Server','Server/','wp-admin/','administr8','administr8/','webadmin/','webadmin','administratie/','admins/','admins','administrivia/','Database_Administration/','useradmin/','sysadmins/','admin1/','system-administration/','administrators/','pgadmin/','directadmin/','staradmin/','ServerAdministrator/','SysAdmin/','administer/','LiveUser_Admin/','sys-admin/','typo3/','panel/','cpanel/','cpanel_file/','platz_login/','rcLogin/','blogindex/','formslogin/','autologin/','support_login/','meta_login/','manuallogin/','simpleLogin/','loginflat/','utility_login/','showlogin/','memlogin/','login-redirect/','sub-login/','wp-login/','login1/','dir-login/','login_db/','xlogin/','smblogin/','customer_login/','UserLogin/','login-us/','acct_login/','bigadmin/','project-admins/','phppgadmin/','pureadmin/','sql-admin/','radmind/','openvpnadmin/','wizmysqladmin/','vadmind/','ezsqliteadmin/','hpwebjetadmin/','newsadmin/','adminpro/','Lotus_Domino_Admin/','bbadmin/','vmailadmin/','Indy_admin/','ccp14admin/','irc-macadmin/','banneradmin/','sshadmin/','phpldapadmin/','macadmin/','administratoraccounts/','admin4_account/','admin4_colon/','radmind-1/','Super-Admin/','AdminTools/','cmsadmin/','SysAdmin2/','globes_admin/','cadmins/','phpSQLiteAdmin/','navSiteAdmin/','server_admin_small/','logo_sysadmin/','power_user/','system_administration/','ss_vms_admin_sm/','bb-admin/','panel-administracion/','instadmin/','memberadmin/','administratorlogin/','adm','admin_login','panel-administracion/login','pages/admin/admin-login','pages/admin/','acceso','admincp/login','admincp/','adminarea/','admincontrol/','affiliate','adm_auth','memberadmin','administratorlogin','modules/admin/','administrators','siteadmin/','siteadmin','adminsite/','kpanel/','vorod/','vorod','vorud/','vorud','adminpanel/','PSUser/','secure/','webmaster/','webmaster','autologin','userlogin','admin_area','cmsadmin','security/','usr/','root/','secret/','admin/login','admin/adminLogin','moderator','moderator','moderator/login','moderator/admin','yonetici','0admin/','0manager/','aadmin/','cgi-bin/login','login1','login_admin/','login_admin','login_out/','login_out','login_user','loginerror/','loginok/','loginsave/','loginsuper/','loginsuper','login','logout/','logout','secrets/','super1/','super1','super_index','super_login','supermanager','superman','superuser','supervise/','supervise/Login','super'}

count = 0

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
            try:
                user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                head = { 'User-Agent' : user_agent }
                req = urllib.request.Request(temp,headers = head)
                res = urllib.request.urlopen(req)
                data=res.read().decode('utf-8')
                m=rx.search(data)
                if m:
                    print('Found at '+temp)
                    print('Do You wish to continue (Y/N)?')
                    ans=input()
                    if (ans=='N'):
                        print('No. of links checked '+count)
                        break;
                    elif (ans=='n'):
                        print('No. of links checked '+count)
                        break;
                res.close()
                print('Not Found :( , even though I checked '+count+'links ')
            except Exception as e:
                    print(str(e))


print("Enter the link without http:// \n\n")
print("Like this --- www.google.com\n\n")
url = input()
rx = re.compile('Username',re.IGNORECASE)

print('Which type of files do you want to search for ? (Default is both , for default just press enter , will take time )')
print('1. PHP\n2. ASP\n3. JS\n4. CGI\n5. CFM\n6. BRF')
ans=input()
if ans =='':
    for i in range(1,7):
        test(i)
else:
    ans=int(ans)
    if ans > 0 & ans < 7:
        test(ans)
    else:
        print('Please enter a valid option')
