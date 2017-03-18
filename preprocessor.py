
"""
Created on Mon Mar 18 11:27:40 2017
@author: ZNevzz
"""
from bs4 import beautiful
import pandas as pd

#read file
filenames=['data_o2.csv']



#snippet
html='<p xmlns:fn=""http://www.w3.org/2005/xpath-functions"" id=""U10478744187zRC"" style="" letter-spacing: -7; ;"">The December quarter result of auto component maker Motherson Sumi Systems Ltd (MSSL) was a pleasant surprise for investors. A 23% rise in consolidated operating profit from a year earlier was driven partly by higher sales, and by lower input costs. Just six months ago, the Street punished this stock on fears of a massive sales pullback after its major customer Volkswagen AG suffered a setback on account of the emission tests scandal in the US.<p id=""U10478744187s9B"" style="" letter-spacing: -7; ;"">
				   
				But those fears have proved to be overdone. The quarters 9% growth in net revenue may have been a tad lower than forecast. This was because domestic sales were hit by Chennai floods and they grew by only 2%. It was also partly the effect of pass-through of low commodity prices.<p id=""U1047874418743B"" style="" letter-spacing: -7; ;"">That said, MSSLs overseas operations made up for it. The European business, which accounts for about two-thirds of consolidated revenue, did well in the December quarter. Two large subsidiaries that make internal and external modules for automobiles, like rear-view mirrors, wiring harnesses, door panels, bumpers, etc. continued to clock stable sales growth across world markets. However, revenue in rupee terms grew at a lower rate than in euro terms, due to the unfavourable currency movement during the quarter.<p id=""U104787441877nG"" style="" letter-spacing: -7; ;"">What has kept the stock ticking, in spite of the recent adversities, is its strong order book that holds the promise of sustained revenue growth in the next few years. That is perhaps why the stock trades at an expensive 17 times the estimated earnings per share of fiscal year 2017. <p id=""U10478744187zeD"" style="" letter-spacing: -7; ;"">Yet, there are risks to this promise. MSSL hopes to diversify into new markets like China, Brazil and America in order to reduce its exposure to Europe. But some of these emerging markets too are now hit by slowdown, and growth in developed markets is yet to prove its sustainability. Any drop in sales volume will have an effect on economies of scale, which in turn may hurt profitability.<p id=""U10478744187BEB"" style="" letter-spacing: -7; ;"">For the December quarter, MSSLs consolidated operating margin of 10% was higher by 120 basis points from a year back, though marginally lower than in the September quarter. Much of this accrued from the stand-alone business, while that of the overseas subsidiaries is slowly getting better. Some analysts also fear that any further large-ticket acquisitions could mar profit growth, until the world auto market shows strong traction"'



