#!/usr/bin/env python

import urllib, urllib2
import re
import codecs

WSbase = 'Bible_(Wycliffe)/'
WSbooks = (
    'Genesis', 'Exodus', 'Leviticus', 'Numbers',
    'Deuteronomy', 'Joshua', 'Judges', 'Ruth',
    '1 Kings', '2 Kings', '3 Kings', '4 Kings',
    '1 Paralipomenon', '2 Paralipomenon', '1 Esdras', '2 Esdras',
    '3 Esdras', 'Tobit', 'Judith', 'Esther',
    'Job', 'Psalms', 'Proverbs', 'Ecclesiastes',
    'Songes of Songes', 'Wisdom', 'Syrach', 'Isaiah',
    'Jeremiah', 'Lamentations', 'Preier of Jeremye', 'Baruk',
    'Ezechiel', 'Daniel', 'Osee', 'Joel',
    'Amos', 'Abdias', 'Jonas', 'Mychee',
    'Naum', 'Abacuk', 'Sofonye', 'Aggey',
    'Sacarie', 'Malachie', '1 Machabeis', '2 Machabeis',
    'Matheu', 'Mark', 'Luke', 'John',
    'Dedis of Apostlis', 'Romaynes', '1 Corinthis', '2 Corinthis',
    'Galathies', 'Effesies', 'Filipensis', 'Colosencis',
    '1 Thessalonycensis', '2 Thessalonycensis', '1 Tymothe', '2 Tymothe',
    'Tite', 'Filemon', 'Ebrews', 'James',
    '1 Petre', '2 Petre', '1 Joon', '2 Joon',
    '3 Joon', 'Judas', 'Apocalips', 'Laodicensis'
    )

OSISbook = (
    'Gen', 'Exod', 'Lev', 'Num',
    'Deut', 'Josh', 'Judg', 'Ruth',
    '1Sam', '2Sam', '1Kgs', '2Kgs',
    '1Chr', '2Chr', 'Ezra', 'Neh',
    '1Esd', 'Tob', 'Jdt', 'Esth',
    'Job', 'Ps', 'Prov', 'Eccl',
    'Song', 'Wis', 'Sir', 'Isa',
    'Jer', 'Lam', 'EpJer', 'Bar',
    'Ezek', 'Dan', 'Hos', 'Joel',
    'Amos', 'Obad', 'Jonah', 'Mic',
    'Nah', 'Hab', 'Zeph', 'Hag',
    'Zech', 'Mal', '1Macc', '2Macc',
    'Matt', 'Mark', 'Luke', 'John',
    'Acts', 'Rom', '1Cor', '2Cor',
    'Gal', 'Eph', 'Phil', 'Col',
    '1Thess', '2Thess', '1Tim', '2Tim',
    'Titus', 'Phlm', 'Heb', 'Jas',
    '1Pet', '2Pet', '1John', '2John',
    '3John', 'Jude', 'Rev', 'EpLao'
    )

USFMbook = (
    'GEN', 'EXO', 'LEV', 'NUM',
    'DEU', 'JOS', 'JDG', 'RUT',
    '1SA', '2SA', '1KI', '2KI',
    '1CH', '2CH', 'EZR', 'NEH',
    '1ES', 'TOB', 'JDT', 'EST',
    'JOB', 'PSA', 'PRO', 'ECC',
    'SNG', 'WIS', 'SIR', 'ISA',
    'JER', 'LAM', 'LJE', 'BAR',
    'EZK', 'DAN', 'HOS', 'JOL',
    'AMO', 'OBA', 'JON', 'MIC',
    'NAM', 'HAB', 'ZEP', 'HAG',
    'ZEC', 'MAL', '1MA', '2MA',
    'MAT', 'MRK', 'LUK', 'JHN',
    'ACT', 'ROM', '1CO', '2CO',
    'GAL', 'EPH', 'PHP', 'COL',
    '1TH', '2TH', '1TI', '2TI', 
    'TIT', 'PHM', 'HEB', 'JAS',
    '1PE', '2PE', '1JN', '2JN', 
    '3JN', 'JUD', 'REV', 'LAO'
    );

USFMnumber = (
    '01', '02', '03', '04',
    '05', '06', '07', '08',
    '09', '10', '11', '12',
    '13', '14', '15', '16',
    '82', '68', '69', '17',
    '18', '19', '20', '21',
    '22', '71', '72', '23',
    '24', '25', '74', '73',
    '26', '27', '28', '29',
    '30', '31', '32', '33',
    '34', '35', '36', '37',
    '38', '39', '78', '79',
    '41', '42', '43', '44',
    '45', '46', '47', '48',
    '49', '50', '51', '52',
    '53', '54', '55', '56', 
    '57', '58', '59', '60',
    '61', '62', '63', '64', 
    '65', '66', '67', 'C3'
    );

"""
articleList = ''
for WSbook in WSbooks:
    articleList += WSbase + '/' + WSbook + '\n'

"""

OSISdoc = ''

for i in range(len(WSbooks)):
    print WSbooks[i]
    url = 'https://en.wikisource.org/wiki/Special:Export'
    vals = {'pages':WSbase+WSbooks[i],
            'curonly':1,
            'wpDownload':0}
    vals = urllib.urlencode(vals)
    request = urllib2.Request(url,vals)
    inputDoc = urllib2.urlopen(request).read().decode('utf-8')
    
    inputDoc = re.sub(r'.*<text .+?>(.+?)</text>.*', r'\1', inputDoc, flags=re.DOTALL|re.IGNORECASE)

    inputDoc = re.sub('  +', ' ', inputDoc)

		# first convert entities within the special download text (extend this if required)
    inputDoc = re.sub(r'&lt;', '<', inputDoc, flags=re.DOTALL|re.IGNORECASE)
    inputDoc = re.sub(r'&gt;', '>', inputDoc, flags=re.DOTALL|re.IGNORECASE)
    # that makes the subsequent code below easier to read 
		
    inputDoc = re.sub(r'{{header.+?}}', '', inputDoc, flags=re.DOTALL|re.IGNORECASE)
    inputDoc = re.sub(r'<div style=.+?/div>', '', inputDoc, flags=re.DOTALL|re.IGNORECASE)
    inputDoc = re.sub(r'{{Other versions.+?}}', '', inputDoc, flags=re.DOTALL|re.IGNORECASE)
    inputDoc = re.sub(r'{{biblecontents.+?}}.*', '', inputDoc, flags=re.DOTALL|re.IGNORECASE)
    inputDoc = re.sub(r'\[\[Category.+?\]\]', '', inputDoc, flags=re.DOTALL|re.IGNORECASE)
    inputDoc = re.sub(r'<section .+?>', '', inputDoc, flags=re.DOTALL|re.IGNORECASE)
    inputDoc = re.sub(r'<onlyinclude>{{{.+?\|\s*(.+?)}}}</onlyinclude>', r'\1', inputDoc, flags=re.DOTALL|re.IGNORECASE)
    inputDoc = re.sub(r'</?onlyinclude> *', '', inputDoc, flags=re.DOTALL|re.IGNORECASE)

#   inputDoc = re.sub(r'\[Note:(.+?) +\]', r'\\f + \1\\f*', inputDoc, flags=re.DOTALL|re.IGNORECASE)
    inputDoc = re.sub(r'<ref>(.+?)</ref>', r'\\f + \1\\f*', inputDoc, flags=re.DOTALL|re.IGNORECASE)
    inputDoc = re.sub(r'\[Note: ', r'', inputDoc, flags=re.DOTALL|re.IGNORECASE)
    inputDoc = re.sub(r'\]\\', r'\\', inputDoc, flags=re.DOTALL|re.IGNORECASE)
    inputDoc = re.sub(r'\[(.+?)\]', r'\\it \1\\it*', inputDoc, flags=re.DOTALL|re.IGNORECASE)
#   inputDoc = re.sub(r'\[(.+?)\]', r'\\add \1\\add*', inputDoc, flags=re.DOTALL|re.IGNORECASE)
    inputDoc = re.sub(r'<references\s*/>', '', inputDoc, flags=re.DOTALL|re.IGNORECASE)

    inputDoc = re.sub(r'==Chapter \d+==', '', inputDoc, flags=re.IGNORECASE)

    inputDoc = re.sub(r'{{chapter\|(\d+)}}\s*', r'\\c \1\n\\p\n', inputDoc, flags=re.IGNORECASE)
    inputDoc = re.sub(r'{{verse\|chapter=\d+\|verse=(\d+)}}\s*', r'\\v \1 ', inputDoc, flags=re.IGNORECASE)

    inputDoc = re.sub(r'==External links==.+', '', inputDoc, flags=re.DOTALL|re.IGNORECASE)

    USFMdoc = codecs.open('wycliffe_'+USFMnumber[i]+'_'+USFMbook[i]+'.usfm', 'w', 'utf-8')
    
    USFMdoc.write('\\id '+USFMbook[i]+'\n')
    USFMdoc.write('\\rem Converted from source text at https://en.wikisource.org/wiki/Bible_(Wycliffe)\n')
    USFMdoc.write('\\h '+WSbooks[i]+'\n')
    USFMdoc.write('\\toc1 '+WSbooks[i]+'\n')
    USFMdoc.write('\\toc2 '+WSbooks[i]+'\n')
    USFMdoc.write('\\mt1 '+WSbooks[i]+'\n')

    for l in inputDoc.split('\n'):
        l = l.strip()
        if l:
            USFMdoc.write(l)
            USFMdoc.write('\n')
