#!/usr/bin/python

import socket,os,commands,random

#creating a socket object

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=os.system('hostname -i')
hostip=str(host)

port=3333

s.bind( ("192.168.205.134",port) )

#the function calling part of the program		

s.listen(5)

obj,clip=s.accept()

print "Connected!!!"



#creating the login response block on server-side

def main():

	ec1=obj.recv(1024)

	if ec1=='0':
		ec2=obj.recv(1024)
		if ec2=='0':
			user=obj.recv(1024)
			ec3=obj.recv(1024)
			if ec3=='0':
				password=obj.recv(1024)
				body(user,password)
			else:
				main()
		else:
			main()
	
	else:
		ec2=obj.recv(1024)
		if ec2=='0':
			user=obj.recv(1024)
			commands.getstatusoutput('useradd {}'.format(user))
			ec3=obj.recv(1024)
			if ec3=='0':
				password=obj.recv(1024)
				commands.getstatusoutput('echo {} | passwd {} --stdin'.format(password,user))
				body(user,password)
			else:
				main()
		else:
			main()
	
#creating the menu list response block on server-side


def body(u,p):
	user=u
	password=p
	b1=obj.recv(1024)
	if b1=='0':
		opt=obj.recv(1024)
		if opt=='1':
			saas(user,password)
		elif opt=='2':
			staas(user,password)
		elif opt=='3':
			iaas(user,password)

	else:
		b2=obj.recv(1024)
		if b2=='0':
			main()
		else:
			body(user,password)


#creating the saas portal response block on server-side

def saas(u,p):
	user=u
	password=p
	saas1=obj.recv(1024)
	if saas1=='0':
		opt1=obj.recv(1024)
		
	else:
		body(user,password)

#creating the staas portal response block on server-side

def staas(u,p):
	user=u
	password=p
	staas1=obj.recv(1024)
	if staas1=='0':
		opt3=obj.recv(1024)
		if opt3=='1':
			obj_stor(user,password)
		elif opt3=='2':
			blk_stor(user,password)

	else:
		body(user,password)


#creating the object storage portal response block on server-side

def obj_stor(u,p):
	user=u
	password=p
	obj1=obj.recv(1024)
	if obj1=='0':
		opt2=obj.recv(1024)
		if opt2=='1':
			create_bucket(user,password)
		elif opt2=='2':
			extend_bucket(user,password)
		elif opt2=='3':
			create_snap(user,password)
		elif opt2=='4':
			get_snap(user,password)

	else:
		staas(user,password)


#creating the block storage portal response block on server-side

def blk_stor(u,p):
	user=u
	password=p
	blk1=obj.recv(1024)
	if blk1=='0':
		opt4=obj.recv(1024)
		if opt4=='1':
			create_iscsi(user,password)
		elif opt4=='2':
			extend_bucket(user,password)
		elif opt4=='3':
			create_snap(user,password)
		elif opt4=='4':
			get_snap(user,password)

	else:
		staas(user,password)

#creating a bucket portal response block on server-side

def create_bucket(u,p):
	user=u
	password=p
	obj2=obj.recv(1024)
	if obj2=='0':
		size=obj.recv(1024)
		obj3=obj.recv(1024)
		if obj3=='0':   
			name=obj.recv(1024)
			obj4=obj.recv(1024)
			if obj4=='0':
				mode=obj.recv(1024)
				if mode=='1':
					ec1=commands.getstatusoutput('lvcreate --size {} --name {} /dev/cloud'.format(size,name))
					commands.getstatusoutput('sleep 3')
					ec2=commands.getstatusoutput('mkfs.ext4 /dev/cloud/{}'.format(name))
 					commands.getstatusoutput('mkdir /media/{}'.format(user))
 					ec3=commands.getstatusoutput('mount /dev/cloud/{0} /media/{1}'.format(name,user))
					x=open("/etc/exports",mode='a')
					x.write("\n/media/{}	*(rw,no_root_squash)".format(user))
					x.close()
					ec4=commands.getstatusoutput('systemctl restart nfs-server')
					if ec1[0]==0 and ec2[0]==0 and ec3[0]==0 and ec4[0]==0:
						chck='ok'
						obj.send(chck)
						act=obj.recv(1024)
						if act=='0':
							obj_stor(user,password)
						
					else:
						chck='not'
						obj.send(chck)
						act=obj.recv(1024)
						if act==0:
							obj_stor(user,password)
				elif mode=='2':
					ec1=commands.getstatusoutput('lvcreate --size {} --name {} /dev/cloud'.format(size,name))
					ec2=commands.getstatusoutput('mkfs.ext4 /dev/cloud/{}'.format(name))
 					commands.getstatusoutput('mkdir /media/{}'.format(user))
					commands.getstatusoutput('chown {} /media/{}"'.format(user,name))
					commands.getstatusoutput('chmod 700 /media/{}'.format(name))
					ec3=commands.getstatusoutput('mount /dev/cloud/{} /media/{}'.format(name,user))
					if ec1[1]==0 and ec2[1]==0 and ec3[1]==0:
						chck='ok'
						obj.send(chck)
						act=obj.recv(1024)
						if act==0:
							obj_stor(user,password)
						
					else:
						chck='not'
						obj.send(chck)
						act=obj.recv(1024)
						if act==0:
							obj_stor(user,password)
						

			else:
				obj_stor(user,password)

		else:
			obj_stor(user,password)

	else:
		obj_stor(user,password)

#creating a extend bucket response block on server-side

def extend_bucket(u,p):
	user=u
	password=p
	obj2=obj.recv(1024)
	if obj2=='0':
		size=obj.recv(1024)
		obj3=obj.recv(1024)
		if obj3=='0':   
			name=obj.recv(1024)
			ec1=commands.getstatusoutput('lvextend --size +{} /dev/cloud/{}'.format(size,name))
			ec2=commands.getstatusoutput('resize2fs /dev/cloud/{}'.format(size,name))
			if ec1[0]==0 and ec2[0]==0:
				chck='ok'
				s.send(chck)
				act=s.recv(1024)
				if act==0:
					obj_stor(user,password)
			else:
				chck='not'
				s.send(chck)
				act=s.recv(1024)
				if act==0:
					obj_stor(user,password)

		else:
			obj_stor(user,password)
	else:
		obj_stor(user,password)

#creating a create snapshot response block on server-side

def create_snap(u,p):
	user=u
	password=p
	obj2=obj.recv(1024)
	if obj2=='0':
		sname=obj.recv(1024)
		obj3=obj.recv(1024)
		if obj3=='0':   
			name=obj.recv(1024)
			ec1=commands.getstatusoutput('lvcreate -s --name {} --size 20M /dev/cloud/{}'.format(sname,name))
			if ec1[0]==0:
				chck='ok'
				s.send(chck)
				act=s.recv(1024)
				if act==0:
					obj_stor(user,password)
			else:
				chck='not'
				s.send(chck)
				act=s.recv(1024)
				if act==0:
					obj_stor(user,password)

		else:
			obj_stor(user,password)
	else:
		obj_stor(user,password)

#creating a get snapshot response block on server-side

def get_snap(u,p):
	user=u
	password=p
	obj2=obj.recv(1024)
	if obj2=='0':
		sname=obj.recv(1024)
		commands.getstatusoutput('sleep 3')
		ec2=commands.getstatusoutput('mkfs.ext4 /dev/cloud/{}'.format(sname))
 		commands.getstatusoutput('mkdir /media/{}'.format(user))
 		ec3=commands.getstatusoutput('mount /dev/cloud/{0} /media/{1}'.format(sname,user))
		x=open("/etc/exports",mode='a')
		x.write("\n/media/{}	*(rw,no_root_squash)".format(user))
		x.close()
		ec4=commands.getstatusoutput('systemctl restart nfs-server')
		if ec1[0]==0 and ec2[0]==0 and ec3[0]==0 and ec4[0]==0:
			chck='ok'
			s.send(chck)
			act=s.recv(1024)
			if act==0:
				obj_stor(user,password)
		else:
			chck='not'
			s.send(chck)
			act=s.recv(1024)
			if act==0:
				obj_stor(user,password)

	else:
		obj_stor(user,password)


#creating a create iscsi block response block on server-side

def create_iscsi(u,p):
	user=u
	password=p
	obj2=obj.recv(1024)
	if obj2=='0':
		size=obj.recv(1024)
		obj3=obj.recv(1024)
		if obj3=='0':   
			name=obj.recv(1024)
			ec1=commands.getstatusoutput('lvcreate --size {} --name {} /dev/cloud'.format(size,user))
			x=open("/etc/tgt/conf.d/{}.conf".format(user),mode='a')
			x.write("<target cloud>\n\t\tbacking store /dev/cloud/{}\n</target>".format(user))
			x.close()
			ec2=commands.getstatusoutput('systemctl restart tgtd')
			ec3=commands.getstatusoutput('chkconfig tgtd on')
			commands.getstatusoutput('iptables -F')
			if ec1[0]==0 and ec2[0]==0 and ec3[0]==0:
				chck='ok'
				s.send(chck)
				act=s.recv(1024)
				if act==0:
					obj_stor(user,password)
			else:
				chck='not'
				s.send(chck)
				act=s.recv(1024)
				if act==0:
					obj_stor(user,password)

		else:
			obj_stor(user,password)
	else:
		obj_stor(user,password)

#creating iaas portal response block on server-side

def iaas(u,p):
	user=u
	password=p
	iaas1=obj.recv(1024)
	if iaas1=='0':
		name=obj.recv(1024)
		iaas2=obj.recv(1024)
		if iaas2=='0':
			mem=obj.recv(1024)
			iaas3=obj.recv(1024)
			if iaas3=='0':
				cpu=obj.recv(1024)
				iaas4=obj.recv(1024)
				if iaas4=='0':
					disk=obj.recv(1024)
					iaas5=obj.recv(1024)
					if iaas5=='0':
						size=obj.recv(1024)
						iaas6=obj.recv(1024)
						if iaas6=='0':
							os=obj.recv(1024)
							iaas7=obj.recv(1024)
							if iaas7=='0':
								var=obj.recv(1024)
								if os=='linux' and var=='rhel7':
									ec1=commands.getstatusoutput('sudo ln /var/lib/libvirt/images/rhel.img /var/lib/libvirt/images/{}.img'.format(disk))
									port=random.randint(8000,15000)
									ec2=commands.getstatusoutput('sudo virt-install --hvm --name {} --memory {} --vcpus {} --cd-rom /root/Desktop/ --os-type {} --os-variant {} --disk /var/lib/libvirt/images/{}.img,size={} --noautoconsole --graphics vnc,password={},port={} '.format(name,mem,cpu,os,var,disk,size,password,port))
									if ec1[0]==0 and ec2[0]==0:
										obj.send('ok')
										chck=obj.recv(1024)
										if chck=='0':
											body(user,password)
									else:
										obj.send('not')
										chck=obj.recv(1024)
										if chck=='0':
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
	else:
		body(user,password)


main()

obj.close()
