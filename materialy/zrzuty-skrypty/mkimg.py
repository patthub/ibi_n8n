from PIL import Image, ImageDraw
S="shots/"; O="site/img/"
# (out, src, crop(orig px) or None, highlight boxes in orig px [(x0,y0,x1,y1)])
d=1.08  # display(2000w) -> orig(2160w)
def box(cx,cy,w,h,f=d): return (int((cx-w/2)*f),int((cy-h/2)*f),int((cx+w/2)*f),int((cy+h/2)*f))
T=2.4   # 900w thumbnails -> orig
items=[
 ("01-start","home.png",None,[box(1235,40,180,40,1)]),
 ("02-pusta-plansza","b_01_empty.png",None,[box(1028,610,190,200)]),
 ("03-szukaj-chat","b_02_search_chat.png",None,[]),
 ("04-on-chat-event","b_03_after_enter.png",None,[box(1720,368,420,56,1)]),
 ("05-wyzwalacz","b_05_canvas_trigger.png",None,[box(1183,612,44,44)]),
 ("06-szukaj-agent","b_06_search_agent.png",None,[box(1730,405,500,90)]),
 ("07-panel-agenta","b_07_agent_panel.png",None,[]),
 ("08-agent-na-planszy","b_08_canvas_agent.png",None,[]),
 ("09-szukaj-gemini","b_09_search_gemini.png",None,[]),
 ("10-klucz-gemini","b_10b_cred_modal.png",None,[]),
 ("11-model-gemini","p_gemini.png",None,[box(985,306,520,46)]),
 ("12-pamiec-lista","b_11a_memory_picker.png",None,[]),
 ("13-agent-model-pamiec","b_11b_canvas.png",None,[]),
 ("14-okno-czatu","b_17_chat.png",None,[]),
 ("15-narzedzia-lista","b_12_tool_picker.png",None,[]),
 ("16-http-pusty","b_13_http_panel.png",None,[]),
 ("17-http-wypelniony","p_tool.png",None,[box(1246,990,50,50), box(1000,245,540,90)]),
 ("18-gotowy-agent","etap3wf000000003.png",None,[]),
 ("19-add-option","b_15_agent_add_option.png",None,[box(455*T/d,326*T/d,230*T/d,22*T/d)]),
 ("20-system-message","p_agent.png",(760,560,1400,1010),[]),
 ("21-import","b_16_menu.png",None,[box(244*T/d,193*T/d,120*T/d,22*T/d)]),
]
for out,src,crop,boxes in items:
    im=Image.open(S+src).convert("RGB")
    dr=ImageDraw.Draw(im)
    for b in boxes: dr.rounded_rectangle(b, radius=14, outline=(230,40,90), width=7)
    if crop: im=im.crop(crop)
    if im.width>1440: im=im.resize((1440,int(im.height*1440/im.width)), Image.LANCZOS)
    im.save(O+out+".png", optimize=True)
print("ok")
