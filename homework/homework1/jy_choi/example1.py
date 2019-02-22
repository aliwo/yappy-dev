rock = '바위'
scissor = '가위'
paper = '보'


print('플레이어 A님, 입력해주세요')
player_a = input()

print('플레이어 B님, 입력해주세요')
player_b = input()

if player_a == rock:
    if player_b == rock:
        print('비겼습니다.')
    elif player_b == scissor:
        print('플레이어 A님이 이겼습니다')
    elif player_b == paper:
        print('플레이어 B님이 이겼습니다')

if player_a == scissor:
    if player_b == rock:
                print('플레이어 B님이 이겼습니다.')
    elif player_b == scissor:
                print('비겼습니다')
    elif player_b == paper:
                print('플레이어 A님이 이겼습니다')

if player_a == paper:
    if player_b == rock:
                print('플레이어 A님이 이겼습니다.')
    elif player_b == scissor:
                print('플레이어 B님이 이겼습니다.')
    elif player_b == paper:
                print('비겼습니다')