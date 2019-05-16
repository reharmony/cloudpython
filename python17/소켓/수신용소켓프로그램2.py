# import socket
from socket import *
# 네트워크 통신을 위해 socket 생성
# socket은 음성통신에서 전화기 역할
# 네트워크 통신 = 소켓 통신

# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock = socket(AF_INET, SOCK_DGRAM)
print('1. 소켓 준비 완료..')
sock.bind(('192.168.0.130',6000))
print('2. ip/port binding 완료. binding된 port번호는 6000번..')

while True:
    data, addr = sock.recvfrom(1024) # 최대 수신 데이터 크기 1024
    print('상대방 >> ', data.decode('utf-8'))