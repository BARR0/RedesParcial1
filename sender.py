from pygame import mixer
from time import sleep

HtoB = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

SOUNDS = {
    '1': {
        '0': '10.mp3',
        '1': '11.mp3'
    },
    '2': {
        '0': '20.mp3',
        '1': '21.mp3'
    },
    '3': {
        '0': '30.mp3',
        '1': '31.mp3'
    }
}

START = 'tindeck.mp3'

def main():
    mixer.init()
    message = input('Enter the message to be sent: ').upper()
    receivers = input('Enter who to send the messages to: ')
    assert(len(message) == len(receivers))
    mixer.music.load(open(START,'rb'))
    mixer.music.play()
    while mixer.music.get_busy():
        sleep(1)
    for i in range(len(receivers)):
        receiver = receivers[i]
        sounds = SOUNDS[receiver]
        print('\nPlaying ' + message[i] + ' for receiver ' + receiver)
        for j in HtoB[message[i]]:
            mixer.music.load(open(sounds[j],'rb'))
            mixer.music.play()
            while mixer.music.get_busy():
                sleep(1)
            print(j, end="")
    print()

if __name__ == "__main__":
    main()
