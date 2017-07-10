#!/usr/bin/python

import os
from commands import getstatusoutput
import socket

#creating a socket object for connection

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def userip():
	ip=getstatusoutput('hostname -i')
	return ip

client=userip()
clip=str(client)

port=3333

s.connect( ("192.168.205.134",port) )



#creating the main fuction for login TUI 

def main(): 
	ec1=os.system('dialog --ok-label "Login" --extra-label "SignUp" --extra-button --title "Welkins Cloud" --msgbox "\n\n\n\n\nYour current IP is '+userip()[1]+'" 12 40 ')

	s.send(str(ec1))
	if ec1==0:
		ec2=os.system('dialog --backtitle "Welcome to Welkins Cloud" --inputbox "Username:" 10 40 2>cache')
		s.send(str(ec2))
		if ec2==0:
			user=getstatusoutput('cat cache')
			s.send(user[1])
			ec3=os.system('dialog --backtitle "Welcome to Welkins Cloud" --passwordbox "Password:" 10 40 2>cache')
			s.send(str(ec3))
			if ec3==0:
				password=getstatusoutput('cat cache')
				s.send(password[1])
				body(user[1],password[1])
			else:
				main()
		else:
			main()

	else:
		ec2=os.system('dialog --backtitle "Welcome to Welkins Cloud" --inputbox "Enter a username:" 8 40 2>cache')
		s.send(str(ec2))
		if ec2==0:
			user=getstatusoutput('cat cache')
			s.send(user[1])
			ec3=os.system('dialog --backtitle "Welcome to Welkins Cloud" --passwordbox "Enter a password:" 8 40 2>cache')
			s.send(str(ec3))
			if ec3==0:
				password=getstatusoutput('cat cache')
				s.send(password[1])
				body(user[1],password[1])
			else:
				main()
		else:
			main()


#creating the menu list of the cloud services

def body(u,p):
	user=u
	password=p
	b1=os.system('dialog --ok-label "Select" --backtitle "Welcome to Welkins Cloud" --title "Hello "{} --menu "Services we provide:" 15 40 15 1 "Software as a Service" 2 "Storage as a Service" 3 "Infrastructure as a Service" 2>cache'.format(user))
	s.send(str(b1))
	if b1==0:
		opt=getstatusoutput('cat cache')
		s.send(opt[1])
		if opt[1]=='1':
			saas(user,password)
		elif opt[1]=='2':
			staas(user,password)
		elif opt[1]=='3':
			iaas(user,password)
	
	else:
		b2=os.system('dialog --backtitle "Welcome to Welkins Cloud" --title "Hello "{} --yesno "Want to logout ?" 10 40 '.format(user))
		s.send(str(b2))
		if b2==0:
			main()
		else:
			body(user,password)

#creating the saas portal

def saas(u,p):
	user=u
	password=p
	saas1=os.system('dialog --backtitle "Software as a Service" --menu "Select a Software:" 15 40 15 1 "vlc" 2 "firefox" 3 "gedit" 4 "vnc viewer" 2>cache')
	s.send(str(saas1))
	if saas1==0:
		opt1=getstatusoutput('cat cache')
		s.send(opt1[1])
		if opt1[1]=='1':
			getstatusoutput('sshpass -p {} ssh -X -l {} 192.168.43.18 vlc'.format(password,user))
			os.system('dialog --ok-label "Done" --backtitle "Storage as a Service" --msgbox "Successfully launched!!!" 12 40')
			saas(user,password)
		elif opt1[1]=='2':
			getstatusoutput('sshpass -p {} ssh -X -l {} 192.168.43.18 firefox'.format(password,user))
			os.system('dialog --ok-label "Done" --backtitle "Storage as a Service" --msgbox "Successfully launched!!!" 12 40')
			saas(user,password)
		elif opt1[1]=='3':
			getstatusoutput('sshpass -p {} ssh -X -l {} 192.168.43.18 gedit'.format(password,user))
			os.system('dialog --ok-label "Done" --backtitle "Storage as a Service" --msgbox "Successfully launched!!!" 12 40')
			saas(user,password)
		elif opt1[1]=='4':
			getstatusoutput('sshpass -p {} ssh -X -l {} 192.168.43.18 vncviewer'.format(password,user))
			os.system('dialog --ok-label "Done" --backtitle "Storage as a Service" --msgbox "Successfully launched!!!" 12 40')
			saas(user,password)
	else:
		body(user,password)

#creating the staas portal

def staas(u,p):
	user=u
	password=p
	staas1=os.system('dialog --backtitle "Storage as a Service" --menu "Select an option:" 15 40 15 1 "Object Storage" 2 "Block Storage" 2>cache')
	s.send(str(staas1))
	if staas1==0:
		opt3=getstatusoutput('cat cache')
		s.send(opt3[1])
		if opt3[1]=='1':
			obj_stor(user,password)
		elif opt3[1]=='2':
			blk_stor(user,password)

	else:
		body(user,password)


#creating the object storage portal

def obj_stor(u,p):
	user=u
	password=p
	obj1=os.system('dialog --backtitle "Storage as a Service" --menu "Select an option:" 15 40 15 1 "Creating a bucket" 2 "Extending a bucket" 3 "Creating a snapshot" 4 "Get a snapshot" 2>cache')
	s.send(str(obj1))
	if obj1==0:
		opt2=getstatusoutput('cat cache')
		s.send(opt2[1])
		if opt2[1]=='1':
			create_bucket(user,password)
		elif opt2[1]=='2':
			extend_bucket(user,password)
		elif opt2[1]=='3':
			create_snap(user,password)
		elif opt2[1]=='4':
			get_snap(user,password)

	else:
		staas(user,password)

#creating the block storage portal

def blk_stor(u,p):
	user=u
	password=p
	blk1=os.system('dialog --backtitle "Storage as a Service" --menu "Select an option:" 15 40 15 1 "Creating a bucket" 2 "Extending a bucket" 3 "Creating a snapshot" 4 "Get a snapshot" 2>cache')
	s.send(str(blk1))
	if blk1==0:
		opt4=getstatusoutput('cat cache')
		s.send(opt4[1])
		if opt4[1]=='1':
			create_iscsi(user,password)
		elif opt4[1]=='2':
			extend_bucket(user,password)
		elif opt4[1]=='3':
			create_snap(user,password)
		elif opt4[1]=='4':
			get_snap(user,password)

	else:
		staas(user,password)

#creating a create bucket portal

def create_bucket(u,p):
	user=u
	password=p
	obj2=os.system('dialog --backtitle "Storage as a Service" --inputbox "Enter size of bucket:" 10 40 2>cache')
	s.send(str(obj2))
	if obj2==0:
		size=getstatusoutput('cat cache')
		s.send(size[1])
		obj3=os.system('dialog --backtitle "Storage as a Service" --inputbox "Enter name of bucket:" 10 40 2>cache')
		s.send(str(obj3))
		if obj3==0:
			name=getstatusoutput('cat cache')
			s.send(name[1])
			obj4=os.system('dialog --backtitle "Storage as a Service" --menu "Choose a mode:" 15 40 15 1 "NFS" 2 "SSHFS" 2>cache')
			s.send(str(obj4))
			if obj4==0:
				mode=getstatusoutput('cat cache')
				s.send(mode[1])
				if mode[1]=='1':
					chck=s.recv(1024)
					if chck=='ok':
						getstatusoutput('mkdir /media/{}'.format(name[1]))
						getstatusoutput('mount 192.168.43.18:/media/{0}  /media/{1}'.format(user,name[1]))
						act=os.system('dialog --ok-label "Done" --backtitle "Storage as a Service" --msgbox "Successfully mounted!!!....go to your desktop" 12 40')
						s.send(str(act))
						if act==0:
							obj_stor(user,password)
					else:
						act=os.system('dialog --ok-label "Try Again" --backtitle "Storage as a Service" --msgbox "Error Occured" 12 40')
						s.send(act)
						if act==0:
							obj_stor(user,password)
				elif mode[2]=='2':
					chck=s.recv(1024)
					if chck=='ok':
						getstatusoutput('mkdir /media/{}'.format(name[1]))
						getstatusoutput('sshpass -p {} sshfs 192.168.43.18:/media/{} /media/{}'.format(password,user,name[1]))
						act=os.system('dialog --ok-label "Done" --backtitle "Storage as a Service" --msgbox "Successfully mounted!!!....go to your desktop" 12 40')
						s.send(act)
						if act==0:
							obj_stor(user,password)
					else:
						act=os.system('dialog --ok-label "Try Again" --backtitle "Storage as a Service" --msgbox "Error Occured" 12 40')
						s.send(act)
						if act==0:
							obj_stor(user,password)

			else:
				obj_stor(user,password)

		else:
			obj_stor(user,password)

	else:
		obj_stor(user,password)

#creating the extend bucket portal

def extend_bucket(u,p):

	user=u
	password=p
	obj2=os.system('dialog --backtitle "Storage as a Service" --inputbox "Enter required size :" 10 40 2>cache')
	s.send(str(obj2))
	if obj2==0:
		size=getstatusoutput('cat cache')
		s.send(size[1])
		obj3=os.system('dialog --backtitle "Storage as a Service" --inputbox "Enter name of bucket:" 10 40 2>cache')
		s.send(str(obj3))
		if obj3==0:
			name=getstatusoutput('cat cache')
			s.send(name[1])
			chck=s.recv(1024)
			if chck=='ok':
				act=os.system('dialog --ok-label "Done" --backtitle "Storage as a Service" --msgbox "Successfully extended!!!....go to your desktop" 12 40')
				s.send(act)
				if act==0:
					obj_stor(user,password)
			else:
				act=os.system('dialog --ok-label "Try Again" --backtitle "Storage as a Service" --msgbox "Error Occured" 12 40')
				s.send(act)
				if act==0:
					obj_stor(user,password)

		else:
			obj_stor(user,password)
	else:
		obj_stor(user,password)


#creating the create snapshot portal

def create_snap(u,p):

	user=u
	password=p
	obj2=os.system('dialog --backtitle "Storage as a Service" --inputbox "Enter name of snapshot :" 10 40 2>cache')
	s.send(str(obj2))
	if obj2==0:
		sname=getstatusoutput('cat cache')
		s.send(sname[1])
		obj3=os.system('dialog --backtitle "Storage as a Service" --inputbox "Enter name of bucket:" 10 40 2>cache')
		s.send(str(obj3))
		if obj3==0:
			name=getstatusoutput('cat cache')
			s.send(name[1])
			chck=s.recv(1024)
			if chck=='ok':
				act=os.system('dialog --ok-label "Done" --backtitle "Storage as a Service" --msgbox "Snapshot created !!!" 12 40')
				s.send(act)
				if act==0:
					obj_stor(user,password)
			else:
				act=os.system('dialog --ok-label "Try Again" --backtitle "Storage as a Service" --msgbox "Error Occured" 12 40')
				s.send(act)
				if act==0:
					obj_stor(user,password)

		else:
			obj_stor(user,password)
	else:
		obj_stor(user,password)

#creating the get snapshot portal

def get_snap(u,p):

	user=u
	password=p
	obj2=os.system('dialog --backtitle "Storage as a Service" --inputbox "Enter name of snapshot :" 10 40 2>cache')
	s.send(str(obj2))
	if obj2==0:
		sname=getstatusoutput('cat cache')
		s.send(sname[1])
		chck=s.recv(1024)
		if chck=='ok':
			getstatusoutput('mkdir /media/{}'.format(sname[1]))
			getstatusoutput('mount 192.168.43.18:/media/{0}  /media/{1}'.format(user,sname[1]))
			act=os.system('dialog --ok-label "Done" --backtitle "Storage as a Service" --msgbox "Snapshot created !!!" 12 40')
			s.send(act)
			if act==0:
				obj_stor(user,password)
		else:
			act=os.system('dialog --ok-label "Try Again" --backtitle "Storage as a Service" --msgbox "Error Occured" 12 40')
			s.send(act)
			if act==0:
				obj_stor(user,password)

	else:
		obj_stor(user,password)

#creating the create iscsi block portal

def create_iscsi(u,p):

	user=u
	password=p
	obj2=os.system('dialog --backtitle "Storage as a Service" --inputbox "Enter size of block :" 10 40 2>cache')
	s.send(str(obj2))
	if obj2==0:
		size=getstatusoutput('cat cache')
		s.send(size[1])
		obj3=os.system('dialog --backtitle "Storage as a Service" --inputbox "Enter name of block:" 10 40 2>cache')
		s.send(str(obj3))
		if obj3==0:
			name=getstatusoutput('cat cache')
			s.send(name[1])
			chck=s.recv(1024)
			if chck=='ok':
				getstatusoutput('yum install iscsi-initiator-utils')
				getstatusoutput('iscsiadm --mode discoverydb --type sendtargets --portal 192.168.43.18 --discover')
				getstatusoutput('iscsiadm --mode node --targetname 192.168.43.18:cloud --portal 192.168.43.18:3260 --login')
				act=os.system('dialog --ok-label "Done" --backtitle "Storage as a Service" --msgbox "Successfully created !!!" 12 40')
				s.send(act)
				if act==0:
					obj_stor(user,password)
			else:
				act=os.system('dialog --ok-label "Try Again" --backtitle "Storage as a Service" --msgbox "Error Occured !!!" 12 40')
				s.send(act)
				if act==0:
					obj_stor(user,password)

		else:
			obj_stor(user,password)
	else:
		obj_stor(user,password)

#creating iaas portal

def iaas(u,p):
	user=u
	password=p
	iaas1=os.system('dialog --backtitle "Infrastructure as a Service" --inputbox "Enter name of instance:" 10 40 2>cache')
	s.send(str(iaas1))
	if iaas1==0:
		name=getstatusoutput('cat cache')
		s.send(name[1])
		iaas2=os.system('dialog --backtitle "Infrastructure as a Service" --inputbox "Enter memory size:" 10 40 2>cache')
		s.send(str(iaas2))
		if iaas2==0:
			size=getstatusoutput('cat cache')
			s.send(size[1])
			iaas3=os.system('dialog --backtitle "Infrastructure as a Service" --inputbox "Enter no. of cpus:" 10 40 2>cache')
			s.send(str(iaas3))
			if iaas3==0:
				cpu=getstatusoutput('cat cache')
				s.send(cpu[1])
				iaas4=os.system('dialog --backtitle "Infrastructure as a Service" --inputbox "Enter disk name:" 10 40 2>cache ')
				s.send(str(iaas4))
				if iaas4==0:
					disk=getstatusoutput('cat cache')
					s.send(disk[1])
					iaas5=os.system('dialog --backtitle "Infrastructure as a Service" --inputbox "Enter size of disk:" 10 40 2>cache ')
					s.send(str(iaas5))
					if iaas5==0:
						size=getstatusoutput('cat cache')
						s.send(size[1])
						iaas6=os.system('dialog --backtitle "Infrastructure as a Service" --menu "Choose os family:" 15 40 15 1 "Linux" 2 "Windows" 2>cache')
						s.send(str(iaas6))
						if iaas6==0:
							chck=getstatusoutput('cat cache')
							if chck[1]=='1':
								s.send('linux')
							else:
								s.send('windows')
							iaas7=os.system('dialog --backtitle "Infrastructure as a Service" --menu "Choose os-variant:" 15 40 15 1 "Redhat" 2 "Kali" 3 "CentOS" 4 "Ubuntu"  2>cache')
							s.send(str(iaas7))
							if iaas7==0:
								chck1=getstatusoutput('cat cache')
								if chck1[1]=='1' and chck[1]=='1':
									s.send('rhel7')
									feed=s.recv(1024)
									if feed=='ok':	
										act=os.system('dialog --ok-label "Done" --backtitle "Infrastructure as a Service" --msgbox "Successfully Launched !!!" 12 40')
										s.send(str(act))
										if act==0:
											body(user,password)
									else:
										act=os.system('dialog --ok-label "Done" --backtitle "infrastructure as a Service" --msgbox "Error Occured !!!" 12 40')
										s.send(str(act))
										if act==0:
											body(user,password)
								elif chck1[1]=='2' and chck[1]=='1':
									s.send('generic')
								elif chck1[1]=='3' and chck[1]=='1':
									s.send('centos')
								elif chck1[1]=='4' and chck[1]=='1':
									s.send('ubuntu')
							else:
								body(user,password)
						else:
							body(user,password)
					else:
						body(user,password)
				else:
					body(user,password)
			else:
				body(user,password)
		else:
			body(user,password)
	else:
		body(user,password)

main()

s.close()
