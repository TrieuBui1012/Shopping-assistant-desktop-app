# Import tkinter and webview libraries 
from tkinter import *
import webview 

# define an instance of tkinter 
tk = Tk() 

# size of the window where we show our website 
tk.geometry("800x450") 

# Open website 
webview.create_window('Tiki', 'https://tiki.vn/iphone-15-128gb-hong-p271966786.html?spid=271966792&tclid=a443fe6b-61d3-4c5c-a43b-d4dfa0971088&fsl=true&isOpenStore=false&trackId=6730bf4fdb462360b6c491fb&osName=Windows&deepLink=tikivn%3A%2F%2Fproducts%2F271966786%3Fspid%3D271966792%26utm_source%3Daccesstrade%26utm_medium%3Dtiki-aff%26utm_campaign%3DAFF_NBR_ACT_UNK_TIKIVN-TNWGVSKG_ALL_VN_ALL_UNK_UNK_TAPX.b9c70e87-a6cf-4614-8d2f-52ad0f233df4_TAPU.7e816ab8-b482-4a28-bd38-1b2a6d1159b8%26utm_term%3DTAPM.fub4Jm4op46HsPQ6JEzmaQgpEBFQQdaVIXGg06rc3USCAxeZ_TAPP.1328_TAPT.TI2%26tclid%3Da443fe6b-61d3-4c5c-a43b-d4dfa0971088&clickId=bcca8249-8813-4387-91c3-98363168e7a6&fullUrl=https%3A%2F%2Fti.ki%2Fadd%2FTNWGVSKG%3Futm_term%3DTAPM.fub4Jm4op46HsPQ6JEzmaQgpEBFQQdaVIXGg06rc3USCAxeZ_TAPP.1328_TAPT.TI2%26TIKI_URI%3Dhttps%253A%252F%252Ftiki.vn%252Fiphone-15-128gb-hong-p271966786.html%253Fspid%253D271966792&isFBApp=false&deepLinkData=&hash=TNWGVSKG') 
webview.start() 
