import mido
import mido.backends.rtmidi # required for pyinstaller to create an exe


def checksum(data):
    # passed the address and data for set or req sysex message, returns the checksum required for the SY300
    return [(0x80 - (sum(data) & 0x7F)) & 0x7F]


def req_sy300(adr, num_bytes):
    # passed the address and the number of bytes to read, returns the sysex message to read the address
    # num_bytes must be less that 255, 3 MSBs of number of bytes assumed zero
    req_header = [0x41, 0x10, 0x00, 0x00, 0x00, 0x13, 0x11]
    msg = req_header + adr + [0x00, 0x00, 0x00] + num_bytes + checksum(adr + num_bytes)
    return mido.Message('sysex', data=msg)


def set_sy300(adr, data):
    # pass in lists of the adr byts, the number of bytes in the message, and the data to be sent
    # returns a list with the checksum ready to be sent as a sysex message
    set_header = [0x41, 0x10, 0x00, 0x00, 0x00, 0x13, 0x12]
    msg = set_header + adr + data + checksum(adr + data)
    return mido.Message('sysex', data=msg)


def get_midi_ports():
    try:
        sy300_in_port = [s for s in mido.get_input_names() if s.find('SY-300')][0]
        sy300_out_port = [s for s in mido.get_output_names() if s.find('SY-300')][0]
    except IndexError:
        return False
    return {'in': sy300_in_port, 'out': sy300_out_port}


if __name__ == '__main__':
    midi_ports = get_midi_ports()
    if midi_ports is False:
        print("Connection Failure: SY300 not connected")
        exit(1)
    else:
        print(f"SYS300 input:{midi_ports['in']}  output: {midi_ports['out']}")
    to_SY300 = mido.open_output(midi_ports['out'])
    to_SY300.send(set_sy300([0x20, 0x00, 0x20, 0x1], [6]))  # set osc 1 waveform to Noise
    print("Message Sent")
    to_SY300.close()
