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
        '0': '10.wav',
        '1': '11.wav',
        'start': '1.mp3'
    },
    '2': {
        '0': '20.wav',
        '1': '21.wav',
        'start': '2.mp3'
    },
    '3': {
        '0': '30.wav',
        '1': '31.wav',
        'start': '3.mp3'
    }
}

START = 'tindeck.mp3'

def play_sound(sfile):
    '''
    Receives a str with the name of the file.
    '''
    mixer.music.load(open('se/' + sfile, 'rb'))
    mixer.music.play()
    while mixer.music.get_busy():
        sleep(0.2)

def main():
    '''
    Main sender method.
    '''
    mixer.init()
    message = input('Enter the message to be sent: ').upper()
    receivers = input('Enter who to send the messages to: ')
    assert(len(message) == len(receivers))
    # play_sound(START)
    for i in range(len(receivers)):
        receiver = receivers[i]
        sounds = SOUNDS[receiver]
        print('\nPlaying ' + message[i] + ' for receiver ' + receiver)
        play_sound(START)
        for j in HtoB[message[i]]:
            print (j, end='', flush=True)
            play_sound(sounds[j])
    print()

if __name__ == "__main__":
    main()
