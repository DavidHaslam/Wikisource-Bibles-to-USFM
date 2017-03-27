# Wikisource-Bibles-to-USFM
Python script[s] to capture and convert a Wikisource Bible to ParaTExt/USFM files

NB. If you're viewing this using the [CodeHub](https://github.com/thedillonb/CodeHub) app, some links below might be broken.

Files:

* **wycliffe.py** captures from the Special download pages for [Wycliffe's Bible](https://en.wikisource.org/wiki/Bible_(Wycliffe))
* **wycliffeV.py** captures from the Special download pages for [Wycliffe's Bible](https://en.wikisource.org/wiki/Bible_(Wycliffe))

The second version uses standard book names for **Esther** and **Daniel** rather than those specifically intended for the Greek additions.

This is more compatible with the subsequent stages for making a SWORD module in that it matches the **Vulg** versification.

These scripts do not address all the versification issues involved in preparing to make a SWORD module.

* The **Epistle of Jeremiah** is a separate book, whereas in the Vulgate it is **Baruch 6**
* The **Prayer of Manasseh** is assigned invalidly by Wikisource as **2 Chronicles 37**

These issues are better tackled after the conversion from USFM to OSIS XML.
