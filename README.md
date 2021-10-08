## About
Discord currently has a lof interface elements, which are rathes useless for those without nitro. 
They are mostly there to remind you that nitro is a thing.
Unfortunately they can get pretty annoying.
Thee goal of this project is remove as many of them as possible.

## How To
Run the script below in the console
```html
style = `<style>
  
button[aria-label="Open sticker picker"],                           /* Remove sticker picker */
button[aria-label="Send a gift"],                                   /* Remove gift button */
div[role=tablist]>:nth-child(n+7):nth-child(-n+13),                 /* Remove nitro section in options */
.containerExpanded-3MGTRr,                                          /* Remove sticker wave option in new DMs */
#private-channels-1,                                                /* Remove stage channels */
#private-channels-2,                                                /* Remove the nitro tab next to friends */
.closeButton-2GCmT5,                                                /* Remove the X to close DMs */
.optionBox-1b4n4P:nth-child(2),                                     /* Remove the "try it out" avatar pickers*/
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
