import random
import pandas as pd
from generate_mac import generate_mac
from datetime import datetime, timezone

def generator_private_ip():
  x1 = random.choice([172,192,10]) #moved inside loop
  if (int(x1) == 172):
      x2 = random.randint(16,31)            
      x3 = random.randint(0,255)
      x4 = random.randint(0,255)
      return ".".join(map(str,([x1,x2,x3,x4])))

  else:    
      x2 = random.randint(0,255)
      x3 = random.randint(0,255)        
      x4 = random.randint(0,255)
      return ".".join(map(str,([x1,x2,x3,x4])))   

def generator_name_title():
  name0 = ["","","","","","","","","","","","","","","","","","","",""]
  
  name1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        
  name2 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  
  name3 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        
  name4 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        
  name5 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  
  name6 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  
  name7 = ["0","1","2","3","4","5","6","7","8","9"]
  
  name8 = ["0","1","2","3","4","5","6","7","8","9"]
  
  name9 = ["0","1","2","3","4","5","6","7","8","9"]
  
  name10 = ["Alpha","Beta","Gamma","Delta","Epsilon","Zeta","Eta","Theta","Iota","Kappa","Lambda","Mu","Nu","Xi","Omicron","Pi","Rho","Sigma","Tau","Upsilon","Phi","Chi","Psi","Omega"]
  
  name11 = ["Alpha","Beta","Gamma","Delta","Epsilon","Zeta","Eta","Theta","Iota","Kappa","Lambda","Mu","Nu","Xi","Omicron","Pi","Rho","Sigma","Tau","Upsilon","Phi","Chi","Psi","Omega"]
  
  
  # 1 Syllable
  
  name12 = ["B","C","D","G","Gr","Gw","H","J","Jzz","K","Kr","L","M","N","Ph","Pl","Qv","R","Rh","S","T","Th","V","X","Y","Z"]
  
  name13 = ["ahr","al","an","and","ane","arc","arv","aulk","auss","awl","aym","ea","eard","ei","elt","erg","ess","eth","ex","i","ik","ingh","iv","o","ol","oll","or","orght","osch","osk","oth","u","ul","und","ure","uss","ux","yrrc"]
  
  
  # 2 Syllables
  
  name14 = ["Ad","Adv","Alsm","Ar","Arg","Arkh","Auk","Aurgr","Bess","Caldr","Call","Cambr","Carn","Cass","Char","Cord","Cum","Cur","Cyk","Dal","Damm","Delph","Dentr","Drush","Dur","Eb","Eg","Eld","Er","Et","Fried","Gai","Gall","Gamm","Garb","Gast","Gav","Gredd","Haph","Herr","Hy","Ism","Kelb","Klayd","Kol","Kor","Kot","Kub","Lak","Lars","Lav","Lex","Loc","Lyrz","Marl","Modw","Ner","Nes","Nex","Nir","Oct","Ohmn","Omn","Os","Osm","Oud","Ov","Pan","Pass","Phaet","Rask","Rest","Reyl","Rhod","Rol","Ronr","Sap","Sas","Sem","Shur","Son","Tall","Tayb","Tel","Tezl","Them","Threns","Tilv","Trag","Trant","Uix","Vai","Vak","Varn","Veltr","Vett","Vherr","Vianc","Volt","Weyldr","Xix","Zab","Zagr","Zard","Zhok","Zyg"]
  
  name15 = ["a","ak","al","an","and","ane","ank","anx","aph","ard","as","ax","eb","eg","ek","ell","en","ene","ent","er","eum","eus","ex","ia","ian","ias","id","iel","ien","ik","ike","il","in","iom","ion","is","isch","ium","ius","ix","o","ode","ok","ol","olph","on","ook","or","os","ot","ov","owe","u","ul","um","us","uul","uv","yon"]
  
  
  # 3 Syllables
  
  name16 = ["Abb","Aex","Ald","Alm","Alph","Balph","Bell","Ben","Bet","Borg","Cerv","Cort","Cyc","Cyth","Danz","Dec","Deg","Del","Delt","Diad","Drac","Drayk","Eps","Er","Faust","Fel","Gel","Ger","Gerg","Hed","Held","Herm","Herst","Hol","Hyp","Iap","Ill","Inf","Ipl","Khob","Kor","Krypt","Laur","Malth","Mank","Mass","Max","Mitr","Moh","Moj","Om","Orl","Os","Pal","Prod","Reg","Rom","Saph","Sat","Ser","Sig","Sol","Tell","Thass","Ther","Torqu","Trim","Urqu","Val","Vard","Ver","Veth","Vidr","Vitr","Zod","Zuh"]
  
  name17 = ["ad","aestr","ag","ak","al","all","am","an","and","andr","ant","ar","asm","at","athr","av","ebr","ed","ej","ekr","ent","er","err","esw","et","euk","iat","iatr","ic","id","il","ill","im","in","ing","ir","is","off","om","on","or","ot","ovd","ow","ul","ur","urm","ut","uv"]
  
  name18 = ["a","ac","ael","ain","al","an","ar","ax","ei","el","en","er","ex","i","ia","iad","ian","iaz","ict","icz","id","ien","in","ine","io","ion","is","ius","ix","o","on","or","os","oth","ov","um","us","ust"]
  
  
  # 4 Syllables
  
  name19 = ["Ak","Ant","Arc","Bart","Bel","Daed","Eyr","Fed","Ger","Gif","Hext","Hier","Iv","Katr","Ol","Ozm"]
  
  name20 = ["al","asn","eg","ell","erh","err","ig","is","og","ol","on","or","oth","um"]
  
  name21 = ["ad","am","ar","in","iv","ol","om","on","oph","os","ost","ov","ym"]
  
  name22 = ["a","ax","ere","ich","il","ion","is","ius","o","on","or","us"]
  
  
  # Title
  
  name23 = ["Accomplished","Adaptive","Ancient","Augmented","Bureaucratic","Calculating","Compartmentalised","Cybernetic","Devious","Emotionless","Famed","Fleshless","Glitching","High-Performance","Hubristic","Impassive","Infamous","Ingenious","Inhuman","Inquiring","Intuitive","Methodical","Obsessive","Precision","Preeminent","Radical","Reflexive","Schizoid","Secretive","Seditious","Self-Serving","Shrewd","Silent","Transcended","Vat-Grown","Well-Connected"]
  
  name24 = ["Alchemist","Analyser","Appraiser","Archivist","Artisan","Auditor","Calibrator","Cogitator","Compiler","Cyclomancer","Datasmith","Demodulator","Disciple","Emulator","Enginseer","Fabricator","Fulgurite","Genator","Heretek","Interpreter","Lexmechanic","Logician","Magus","Manipulator","Metallurgist","Missionary","Monitor","Multiplexer","Myrmidon","Operator","Peripherant","Prognosticator","Reclaimator","Requisitioner","Secutor","Tech-assassin","Technoshaman","Techsorcist","Transmechanic","Trifactor","Validator"]
  
  name25 = ["Abstracted","Alium","Ancient","Archeotech","Argent","Arithmetic","Asynchronous","Binary","Blessed","Broken","Cardinal","Clockwork","Consecrated","Corrupted","Critical","Cyclic","Default","Diagnostic","Digital","Divine","Electromagnetic","Forbidden","Fragmented","Golden","Graven","Great","Hallowed","Hexadecimal","Hippocrasian","Holy","Incompatible","Infeasible","Integrated","Invalid","Irradiated","Khamrian","Lambent","Latent","Mnemonic","Modular","Numinous","Omnissiah's","Optimised","Partitioned","Probability","Programmable","Radiant","Recursive","Redundant","Sacred","Sanctified","Solex","Universal","Virtual","Xenarite"]
  
  name26 = ["Algorithm","Altar","Anomaly","Archive","Array","Beacon","Cascade","Choir","Chorus","Cloister","Cog","Communion","Configuration","Crucible","Database","Factoria","Forge","Gate","Gestalt","Hierarchy","Host","Interchange","Interface","Key","Litany","Liturgy","Mantle","Matrix","Modulator","Network","Path","Protocol","Prototype","Relic","Reliquary","Revelations","Sacrament","Schematic","Seal","Shrine","Sigil","Simulation","Template","Temple","Testament","Uplink","Variable"]
  
  
  
  name31 = [" "," "," "," "," ","-"," van "," van der "]

  ntp = random.randint(0, 19)
  
  name = ""
  title = ""

  match ntp:
    case 0:
        name = random.choice(name7) + random.choice(name8) + "-" + random.choice(name12) + random.choice(name13)
    case 1:
        name = random.choice(name10) + " " + random.choice(name7) + "-" + random.choice(name12) + random.choice(name13)
    case 2:
        name = random.choice(name14) + random.choice(name15) + " " + random.choice(name7) + random.choice(name8) + "/" + random.choice(name9) + " " + random.choice(name14) + random.choice(name15)
    case 3:
        name = random.choice(name10) + "-" + random.choice(name11) + " " + random.choice(name7) + random.choice(name8)
    case 4:
        name = random.choice(name1) + "-" + random.choice(name2) + " " + random.choice(name3) + random.choice(name7) + random.choice(name4) + "/" + random.choice(name5) + random.choice(name8) + random.choice(name6)
    case 5:
        name = random.choice(name1) + random.choice(name2) + "-" + random.choice(name7) + random.choice(name8) + random.choice(name9)
    case 6:
        name = random.choice(name1) + "-" + random.choice(name7) + random.choice(name8) + random.choice(name9)
    case 7:
        name = random.choice(name14) + random.choice(name15) + "-" + random.choice(name10) + "-" + random.choice(name7)
    case 8:
        name = random.choice(name12) + random.choice(name13) + random.choice(name31) + random.choice(name14) + random.choice(name15)
    case 9:
        name = random.choice(name12) + random.choice(name13) + " " + random.choice(name16) + random.choice(name17) + random.choice(name18)
    case 10:
        name = random.choice(name12) + random.choice(name13) + " " + random.choice(name19) + random.choice(name20) + random.choice(name21) + random.choice(name22)
    case 11:
        name = random.choice(name14) + random.choice(name15) + random.choice(name31) + random.choice(name12) + random.choice(name13)
    case 12:
        name = random.choice(name14) + random.choice(name15) + " " + random.choice(name16) + random.choice(name17) + random.choice(name18)
    case 13:
        name = random.choice(name14) + random.choice(name15) + " " + random.choice(name19) + random.choice(name20) + random.choice(name21) + random.choice(name22)
    case 14:
        name = random.choice(name16) + random.choice(name17) + random.choice(name18) + random.choice(name31) + random.choice(name12) + random.choice(name13)
    case 15:
        name = random.choice(name16) + random.choice(name17) + random.choice(name18) + random.choice(name31) + random.choice(name14) + random.choice(name15)
    case 16:
        name = random.choice(name19) + random.choice(name20) + random.choice(name21) + random.choice(name22) + random.choice(name31) + random.choice(name12) + random.choice(name13)
    case 17:
        name = random.choice(name19) + random.choice(name20) + random.choice(name21) + random.choice(name22) + random.choice(name31) + random.choice(name14) + random.choice(name15)
    case 18:
        name = random.choice(name14) + random.choice(name15) + " " + random.choice(name12) + random.choice(name13) + "-" + random.choice(name12) + random.choice(name13)
    case 19:
        name = random.choice(name16) + random.choice(name17) + random.choice(name18) + " " + random.choice(name12) + random.choice(name13) + "-" + random.choice(name12) + random.choice(name13)

  title = random.choice(name23) + " " + random.choice(name24) + " of the " + random.choice(name25) + " " + random.choice(name26)

  return name, title


data = []
for i in range(200):
  n, t = generator_name_title()
  mac_address = generate_mac.total_random()
  nas_ip_address = generator_private_ip()
  created_at = datetime.now(tz=timezone.utc).isoformat()
  
  entry = {
    "name": n,
    "description": t,
    "mac_address": mac_address,
    "nas_ip_address": nas_ip_address,
    "created_at": created_at,
  }

  data.append(entry)

df = pd.DataFrame(data)
print("Generated DataFrame:")
print(df)

df.to_csv("output.csv", index=False)