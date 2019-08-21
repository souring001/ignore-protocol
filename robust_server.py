import socket
import sys

args = sys.argv
argc = len(args)

ip_dst = '192.168.12.***'
ip_src = '192.168.12.***'
port = 2525
buff = 1024*64

if argc > 1:
	if args[1] == '0':
		print('mode: 0')
	elif args[1] == '1':
		temp = ip_dst
		ip_dst = ip_src
		ip_src = temp
		print('mode: 1')
	else:
		print('illegal parameters: 0 or 1')

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((ip_dst, port))
    
    
    for file_num in range(1, 1001):
        data_list = []
        while True:
            batch, addr = s.recvfrom(buff)

            is_len = len(batch) == 7
            is_end = batch == b'__end__'
            if is_len and is_end:
                print('file:', file_num, '__end__')
                break

            data = batch[2:]
            seq = int.from_bytes(batch[0:2], 'big')
            data_list.append(data)
#             print('seq: ', i, 'len:', len(data), data)
        
        file = b''.join(data_list)
        path = 'checkFiles/dst/'+ str(file_num) +'.bin'
        # path = 'mydst/data'+ str(file_num) +'.png'

        with open(path, mode='wb') as f:
            f.write(file)
