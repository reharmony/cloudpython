from socket import *
# 네트워크 통신을 위해 socket 생성
# socket은 음성통신에서 전화기 역할
# 네트워크 통신 = 소켓 통신

sock = socket(AF_INET, SOCK_DGRAM)
sock2 = socket(AF_INET, SOCK_DGRAM)
print('1. A채팅 소켓 준비 완료..')
sock2.bind(('192.168.0.130',3333)) # 내 주소
print('2. ip/port binding 완료. binding된 port번호는 3333번..')

while True:
    # 먼저 수신 받음
    data, addr = sock2.recvfrom(1024)  # 최대 수신 데이터 크기 1024
    print('채팅B >>', data.decode('utf-8'))

    # 송신할 데이터 입력 후 전송
    data = input('채팅A >> ')
    sock.sendto(data.encode('utf-8'), ('192.168.0.130',4444)) # 상대방 주소

