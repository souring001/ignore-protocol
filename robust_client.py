import socket
import math
import sys

args = sys.argv
argc = len(args)

ip_dst = '192.168.12.***'
ip_src = '192.168.12.***'
port = 2525

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
    s.bind((ip_src, port))
    
    for file_num in range(1, 1001):
        data = open('checkFiles/src/'+ str(file_num) +'.bin', 'rb').read()
        # data = open('mysrc/data'+ str(file_num) +'.png', 'rb').read()

        n_byte = len(data)
#         print('Byte:', n_byte)
        batch_size = 51200 #Byte

        for i in range(math.ceil(n_byte/batch_size)):
            batch = data[i*batch_size:(i+1)*batch_size]
            seq = i.to_bytes(2, 'big')
            s.sendto(seq + batch, (ip_dst, port))
#             print('seq: ', i, 'len:', len(batch), batch)

        s.sendto(b'__end__', (ip_dst, port))
        print('file:', file_num, '__end__')