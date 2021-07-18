# CONFIG START

CHOICE =

# CONFIG END

import httpx, pyperclip
response = httpx.get('https://git.orz.cx/Discord-Purge-Nitro/style.css')
all_lines = response.content.decode('utf-8').splitlines()
chosen_line = all_lines[CHOICE - 1].split(',')[0]
result = f"document.head.innerHTML += '<style>{chosen_line}{{display:none;}}<style>'"
pyperclip.copy(result); print(result)
