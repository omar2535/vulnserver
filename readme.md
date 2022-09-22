# Vulnserver

A repository for me to keep my vulnserver scripts. Quick intro by ar33zy [here](https://medium.com/@ar33zy/exploiting-vulnserver-exe-intro-to-windows-exploitation-c4e4f141b7ff)

## Vulnerable functions

- TRUN ( jmp esp )
- GMON ( SEH )
- KSTET ( jmp esp + egghunter )
- GTER ( jmp esp + egghunter )
- HTER ( str2hex payload + jmp esp )
- LTER ( jmp esp + badchars bypass )
