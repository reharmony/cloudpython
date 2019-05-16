from socket import *
# 네트워크 통신을 위해 socket 생성
# socket은 음성통신에서 전화기 역할
# 네트워크 통신 = 소켓 통신

sock = socket(AF_INET, SOCK_DGRAM)
print('1. 소켓 준비 완료..')
sock.bind(('192.168.0.130',7000)) # 내 주소
print('2. ip/port binding 완료. binding된 port번호는 7000번..')

while True:
    data = input('전송할 테이터 입력>> ')
    sock.sendto(data.encode('utf-8'), ('192.168.0.130',6000)) # 상대방 주소
    print('나 >> ', data)