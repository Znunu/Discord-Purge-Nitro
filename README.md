## About
Discord currently has a lof interface elements, which are rathes useless for those without nitro. 
They are mostly there to remind you that nitro is a thing.
Unfortunately they can get pretty annoying.
Thee goal of this project is remove as many of them as possible.

## How To
Run the script below in the console
```html
style = `<style>
  
button[aria-label="Open sticker picker"],           /* Remove sticker picker */
button[aria-label="Send a gift"],                   /* Remove gift button */
div[role=tabbar]>:nth-child(n+7):nth-child(-n+12),  /* Remove nitro section in options */
.containerExpanded-3MGTRr,                          /* Remove sticker wave option in new DMs */
.customizationSection-2ns2M6:nth-child(2),          /* Remove banner option in profile customization */
#private-channels-1,                                /* Remove stage channels */
none {display:none !important;}

</style>`
document.head.innerHTML += style
```
If you only wish to remove _some_ elements, that's possible too.
Each line (which ends with a comment) is responsible for removing an element.
The element it removes it described in the comment. 
If you wish to keep the element, delete the line.
For example to only remove gift button you'd have this

```html
style = `<style>
  
button[aria-label="Send a gift"],                   /* Remove gift button */
none {display:none !important;}

</style>`
document.head.innerHTML += style
```
