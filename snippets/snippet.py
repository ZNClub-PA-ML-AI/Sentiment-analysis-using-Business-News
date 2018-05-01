# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 08:21:39 2017

@author: ZNevzz
"""
import re
import pandas as pd

## REGEX FILTER ALGO START    
  
text = '''
<p class="xh-highlight">Singed by the choice made by its predecessor, the current committee set up last October to look for a successor to run the Tata Group, has made the eminently safer choice of a chairman who has no other interests in the group apart from the mandated task of running it. In selecting group insider Natarajan Chandrasekaran, chief executive of Tata Consultancy Services Ltd since October 2009 and a TCS lifer, having joined the company straight after completing his Masters in Computer Applications from Regional Engineering College, Trichy, the committee has clearly decided to play safe this time around.</p><p class="xh-highlight">
				   
				The man who could have <a href="http://www.livemint.com/Leisure/fUhDJBr37pN2T6jBFSb1xO/N-Chandrasekaran--A-10billiondollar-smile.html" target="_blank">ended up as a farmer</a> is a professional to the core, someone who was widely seen as the sensible alternative after the violent upheavals even a relative outsider like Mistry subjected the venerable group to over the last three months.</p><p class="xh-highlight"><b>ALSO READ</b> | <b><a href="http://www.livemint.com/Companies/ClQdBjPBMR6VybRSLsCctN/Tata-Sons-may-name-new-chairman-as-early-as-today.html" target="_blank">N Chandrasekaran named new Tata Sons chairman</a></b></p><p class="xh-highlight">Chandrasekaran’s selection also marks the distance the Tata group has travelled. If Mistry was only the second non-Tata family member to head the $103 billion conglomerate, Chandrasekaran will be the first non-Parsi, pointing the way for the future of the community itself. Clearly, the gene pool of eligible Parsis to take over as corporate leaders has dwindled rapidly.</p><p class="xh-highlight">Listed as an avid photographer, a passionate marathoner, and almost inevitably for a Tamil Brahmin as a music aficionado, Chandrasekaran at 53, has age on his side. He will also have the support of Ratan Tata who is unlikely to give him the kind of free hand he gave Mistry. That may be a blessing of course since the skills he will need to manage the group, beset by challenges from within and without, are an order of magnitude different from those he’s needed all these years steering the fortunes of India’s biggest software company.</p><p class="xh-highlight"><b>ALSO READ</b> | <b><a href="http://www.livemint.com/Companies/MeiN5cXyxn0JnLlZwKsy6K/N-Chandrasekaran-Key-facts-about-new-Tata-Sons-chairman.html" target="_blank">N Chandrasekaran: Key facts about new Tata Sons chairman</a></b></p><p class="xh-highlight">The Tata group he takes over is under threat—make no mistake about that. The shadow of Mistry is going to be long and lingering. There is the spate of cases before the National Company Law Tribunal which will need a resolution. There are also polite enquiries from the market regulators which could turn more malevolent. But above all, it is the business issues which are crying out for a resolution. The steel cycle is showing signs of turning so should Chandra, as he’s popularly called, go ahead with his predecessor’s plans to sell off all the group’s steel assets in Europe? Tata Motors Ltd’s ailing domestic cars business is another festering sore that will need careful administering. Looming large over all this will be the future relationship between the Tata Trusts and Tata Sons, the knotty issue which lay at the heart of the ugly fracas witnessed over the last three months.</p>
'''

text = text.strip()

print(text)

## filter functions



text = re.sub('(<p>|<p class="xh-highlight">|</p>)', "", text)
text = re.sub("<i>The writer does not own shares in the above-mentioned companies.</i>","",text)

print("\n",text)

"""

abc…	Letters
123…	Digits
\d	Any Digit
\D	Any Non-digit character
.	Any Character
\.	Period
[abc]	Only a, b, or c
[^abc]	Not a, b, nor c
[a-z]	Characters a to z
[0-9]	Numbers 0 to 9
\w	Any Alphanumeric character
\W	Any Non-alphanumeric character
{m}	m Repetitions
{m,n}	m to n Repetitions
*	Zero or more repetitions
+	One or more repetitions
?	Optional character
\s	Any Whitespace
\S	Any Non-whitespace character
^…$	Starts and ends
(…)	Capture Group
(a(bc))	Capture Sub-group
(.*)	Capture all
(abc|def)	Matches abc or def
"""
    ## REGEX FILTER ALGO END
  
    