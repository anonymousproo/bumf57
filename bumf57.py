#!/usr/bin/python

import os
import sys, traceback


if os.getuid() != 0:
	print "Sorry. This script requires root user or python2.7"
	sys.exit()
def main():
	try:
		print ('''

					\033[1;32m$$\                                $$$$$$\  $$$$$$$\  $$$$$$$$\ 
					$$ |                              $$  __$$\ $$  ____| \____$$  |
					$$$$$$$\  $$\   $$\ $$$$$$\$$$$\  $$ /  \__|$$ |          \033[1;32m$$  / 
					$$  __$$\ $$ |  $$ |$$  _$$  _$$\ $$$$\     $$$$$$$\     $$  /  
			     	        \033[1;33m$$ |  $$ |$$ |  $$ |$$ / $$ / $$ |$$  _|    \_____$$\   $$  /   
					$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |      $$\   $$ | $$  /    
					$$$$$$$  |\$$$$$$  |$$ | $$ | $$ |$$ |\033[1;33m      \$$$$$$  |$$  / v0.4    
					\_______/  \______/ \__| \__| \__|\__|       \______/ \__/      


				      \033[1;36m[@] [ Author: Mahfuzur Rahman | YTB: Anonymous Pro [@]\033[1;36m
				      \033[1;33m[@] [It has 57 tools inside\033[1;33m
 
''')

		def inicio1():
			
				print (''' 
\033[1;91m 
@@@@@@@@@@@@@@@@@@@@ +Choose the menu from below+ @@@@@@@@@@@@@@@@@@@@
\033[1;m
\033[1;32m 
(1) Magic
(2) Information Gathering
(3) Quite
\033[1;32m
   		      ___________________________________________________________________________________________
		      |                                                                                         |
   		      |  {#} Coded By Anonymous Pro YTB                                                    {#}  |
    		      |  {@} Youtube  - https://www.youtube.com/anonymousproo                              {@}  |
    		      |  {$} Github   - https://github.com/anonymousproo                                   {$}  |
    		      |_________________________________________________________________________________________|

			''')

				opcion0 = raw_input("\033[1;36mAnonymousPro\033[5mpress2\033[5m> \033[1;m")
			
				while opcion0 == "1":
				


					
					



					
					print (''' 
****************** +Commands+ ******************


\033[1;32mback\033[1;m 	\033[1;33mGo back\033[1;m

\033[1;32mgohome\033[1;m	\033[1;33mGo to the main menu\033[1;m

		''')


				def inicio():
					while opcion0 == "2":
						print ('''
\033[1;36m**************************** Choose the menu from below *****************************\033[1;m
\033[1;32m 
1) View All Tools
0) Install All Tools			
\033[1;32m		

			 ''')
						print ("\033[1;32mChoose the menu from the top or press (0) to install all Kali linux tools .\n\033[1;m")

						opcion1 = raw_input("\033[1;36mAnonymousPro\033[5mpress1\033[5m> \033[1;m")
						if opcion1 == "back":
							inicio1()
						elif opcion1 == "gohome":
							inicio1()
						elif opcion1 == "0":
							cmd = os.system("apt-get -f install acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy apktool dex2jar python-distorm3 edb-debugger jad javasnoop jd ollydbg smali valgrind yara android-sdk apktool arduino dex2jar sakis3g smali && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")	
						while opcion1 == "1":
							print ('''
\033[1;32m@[ Information Gathering ]\033[1;32m 
\033[1;32m 		
 1) acccheck						21) enumIAX                                                   41) smtp-user-enum                        
 2) ace-voip						22) exploitdb						     42) snmpcheck	
 3) Amap						23) Fierce					             43) sslcaudit		
 4) Automater						24) Firewalk						     44) SSLsplit		
 5) bing-ip2hosts					25) fragroute						     45) sslstrip		
 6) braa						26) fragrouter						     46) SSLyze		
 7) CaseFile						27) Ghost Phisher					     47) THC-IPV6			
 8) CDPSnarf						28) GoLismero						     48) theHarvester			
 9) cisco-torch						29) goofile						     49) TLSSLed			
10) Cookie Cadger					30) lbd							     50) twofi	
11) copy-router-config					31) Maltego Teeth					     51) URLCrazy				
12) DMitry						32) masscan						     52) Wireshark			
13) dnmap						33) Metagoofil						     53) WOL-E			
14) dnsenum						34) Miranda						     54) Xplico		
15) dnsmap						35) Nmap						     55) iSMTP		
16) DNSRecon						36) ntop						     56) InTrace		
17) dnstracer						37) p0f							     57) hping3		
18) dnswalk						38) Parsero										
19) DotDotPwn						39) Recon-ng										
20) enum4linux						40) SET																										
\033[1;32m 																
															

\033[5m press (0) Install all Information Gathering tools \033[5m 
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mAnonymousPro\033[5mSelectTool\033[5m> \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install acccheck")

							elif opcion2 == "2":
								cmd = os.system("apt-get install ace-voip")

							elif opcion2 == "3":
								cmd = os.system("apt-get install amap")
							elif opcion2 == "4":
								cmd = os.system("apt-get install automater")
							elif opcion2 == "5":
								cmd = os.system("wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
							elif opcion2 == "6":
								cmd = os.system("apt-get install braa")
							elif opcion2 == "7":
								cmd = os.system("apt-get install casefile")
							elif opcion2 == "8":
								cmd = os.system("apt-get install cdpsnarf")
							elif opcion2 == "9":
								cmd = os.system("apt-get install cisco-torch")
							elif opcion2 == "10":
								cmd = os.system("apt-get install cookie-cadger")
							elif opcion2 == "11":
								cmd = os.system("apt-get install copy-router-config")
							elif opcion2 == "12":
								cmd = os.system("apt-get install dmitry")
							elif opcion2 == "13":
								cmd = os.system("apt-get install dnmap")
							elif opcion2 == "14":
								cmd = os.system("apt-get install dnsenum")
							elif opcion2 == "15":
								cmd = os.system("apt-get install dnsmap")
							elif opcion2 == "16":
								cmd = os.system("apt-get install dnsrecon")
							elif opcion2 == "17":
								cmd = os.system("apt-get install dnstracer")
							elif opcion2 == "18":
								cmd = os.system("apt-get install dnswalk")
							elif opcion2 == "19":
								cmd = os.system("apt-get install dotdotpwn")
							elif opcion2 == "20":
								cmd = os.system("apt-get install enum4linux")
							elif opcion2 == "21":
								cmd = os.system("apt-get install enumiax")
							elif opcion2 == "22":
								cmd = os.system("apt-get install exploitdb")
							elif opcion2 == "23":
								cmd = os.system("apt-get install fierce")
							elif opcion2 == "24":
								cmd = os.system("apt-get install firewalk")
							elif opcion2 == "25":
								cmd = os.system("apt-get install fragroute")
							elif opcion2 == "26":
								cmd = os.system("apt-get install fragrouter")
							elif opcion2 == "27":
								cmd = os.system("apt-get install ghost-phisher")
							elif opcion2 == "28":
								cmd = os.system("apt-get install golismero")
							elif opcion2 == "29":
								cmd = os.system("apt-get install goofile")
							elif opcion2 == "30":
								cmd = os.system("apt-get install lbd")
							elif opcion2 == "31":
								cmd = os.system("apt-get install maltego-teeth")
							elif opcion2 == "32":
								cmd = os.system("apt-get install masscan")
							elif opcion2 == "33":
								cmd = os.system("apt-get install metagoofil")
							elif opcion2 == "34":
								cmd = os.system("apt-get install miranda")
							elif opcion2 == "35":
								cmd = os.system("apt-get install nmap")
							elif opcion2 == "36":
								print ('ntop is unavailable')
							elif opcion2 == "37":
								cmd = os.system("apt-get install p0f")
							elif opcion2 == "38":
								cmd = os.system("apt-get install parsero")
							elif opcion2 == "39":
								cmd = os.system("apt-get install recon-ng")
							elif opcion2 == "40":
								cmd = os.system("apt-get install set")
							elif opcion2 == "41":
								cmd = os.system("apt-get install smtp-user-enum")
							elif opcion2 == "42":
								cmd = os.system("apt-get install snmpcheck")
							elif opcion2 == "43":
								cmd = os.system("apt-get install sslcaudit")
							elif opcion2 == "44":
								cmd = os.system("apt-get install sslsplit")
							elif opcion2 == "45":
								cmd = os.system("apt-get install sslstrip")
							elif opcion2 == "46":
								cmd = os.system("apt-get install sslyze")
							elif opcion2 == "47":
								cmd = os.system("apt-get install thc-ipv6")
							elif opcion2 == "48":
								cmd = os.system("apt-get install theharvester")
							elif opcion2 == "49":
								cmd = os.system("apt-get install tlssled")
							elif opcion2 == "50":
								cmd = os.system("apt-get install twofi")
							elif opcion2 == "51":
								cmd = os.system("apt-get install urlcrazy")
							elif opcion2 == "52":
								cmd = os.system("apt-get install wireshark")
							elif opcion2 == "53":
								cmd = os.system("apt-get install wol-e")
							elif opcion2 == "54":
								cmd = os.system("apt-get install xplico")
							elif opcion2 == "55":
								cmd = os.system("apt-get install ismtp")
							elif opcion2 == "56":
								cmd = os.system("apt-get install intrace")
							elif opcion2 == "57":
								cmd = os.system("apt-get install hping3")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()		
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")				
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")


							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mAnonymousPro\033[5mSelectTool\033[5m> \033[1;m")
							if opcion2 == "1":
								cmd = os.system("git clone https://github.com/LionSec/wifresti.git && cp wifresti/wifresti.py /usr/bin/wifresti && chmod +x /usr/bin/wifresti && wifresti")
								print (" ")
							elif opcion2 == "2":
								cmd = os.system("apt-get install squid3")
								print (" ")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()

				inicio()
		inicio1()
	except KeyboardInterrupt:
		print ("Shutdown requested...Goodbye...Don't Forget To Subscribe Anonymous Pro")
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()

