# Cottontown rehearsals

Password-protected rehearsal notes for Cottontown chorus, published at https://cottontownchorus.github.io

Every page here is encrypted with [StatiCrypt](https://github.com/robinmoisson/staticrypt). Rehearsal content is only ever committed in encrypted form.

- `tools/build.py`: builds a rehearsal page from its data and rebuilds the archive index, both encrypted
- `tools/*-template.html`: page designs (no rehearsal content)
- `.staticrypt.json`: the public salt, kept stable so "Remember me" works across pages
